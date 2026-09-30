#!/usr/bin/env python3
"""Offline README consistency check; Python standard library only."""
import argparse
import re
from pathlib import Path
CATEGORIES = ("AI", "阅读与影音", "游戏与串流", "自托管与效率工具")
HEADING = re.compile(r"^## (.+?)（(\d+)\s*个）$")
ROW = re.compile(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]*)\s*\|\s*(.*?)\s*\|$")
DETAIL = re.compile(r"^### (\d+)\. \[([^\]]+)\]\(([^)]+)\)$")
STAR = re.compile(r"^⭐\s+([^\s]+)\s+｜\s*.+$")
NUMBER = re.compile(r"(?:0|[1-9]\d*|[1-9]\d{0,2}(?:,\d{3})+)", re.ASCII)

def repo_key(url):
    match = re.fullmatch(r"https://github\.com/([a-z0-9-]+)/([a-z0-9_.-]+)/?", url, re.I | re.ASCII)
    if not match:
        return None
    owner, repo = (part.casefold() for part in match.groups())
    repo = repo[:-4] if repo.endswith(".git") else repo
    return f"{owner}/{repo}" if repo not in ("", ".", "..") else None

def check(text):
    errors, rows, details, sections, totals = [], [], [], {}, []
    side, category, current, fence, intro, markers = "表", None, None, None, True, 0
    def error(line, project, message):
        errors.append(f"L{line} [{project}] {message}")
    def item(line, label, url):
        key = repo_key(url)
        if key is None:
            error(line, label, f"项目 URL 非 GitHub 仓库根地址：{url}")
        elif label.casefold() != key:
            error(line, label, f"项目标签与仓库 URL 不符：{key}")
        return dict(line=line, label=label, url=url, key=key, category=category, stars=[])
    for line, raw in enumerate(text.splitlines(), 1):
        value = raw.strip()
        fm = re.match(r"^(`{3,}|~{3,})", value)
        if fence:
            if re.fullmatch(re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*", value):
                fence = None
            continue
        if fm:
            fence = (fm[1][0], len(fm[1]))
            continue
        if value == "# 项目详解":
            side, category, current, intro = "详解", None, None, False
            markers += 1
            continue
        if value.startswith("## "):
            category, current, intro = None, None, False
            hm = HEADING.fullmatch(value)
            name = hm[1].removesuffix(" · 详解") if hm else ""
            category = next((c for c in CATEGORIES if name == c or name.endswith(" " + c)), None)
            if category:
                detail_heading = hm[1].endswith(" · 详解")
                if detail_heading != (side == "详解"):
                    error(line, category, "分类标题的表/详解位置错误")
                sections.setdefault((side, category), []).append((line, int(hm[2])))
            elif hm or any(c in value for c in CATEGORIES):
                error(line, value, "分类标题或声明数量格式错误")
            continue
        if intro:
            totals.extend((line, int(n)) for n in re.findall(r"(\d+)\s*个项目", value))
        if side == "表" and value.startswith("|"):
            if value == "| 项目 | 星数 | 一句话简介 |" or re.fullmatch(r"[|:\-\s]+", value):
                continue
            rm = ROW.fullmatch(value)
            if not rm:
                error(line, category or "表项", "表项格式错误（须含项目链接、星数和简介）")
                continue
            record = item(line, rm[1], rm[2])
            if not category:
                error(line, rm[1], "表项缺少有效分类标题")
            number = rm[3].strip()
            if not NUMBER.fullmatch(number):
                error(line, rm[1], f"表星数格式错误：{number!r}")
            else:
                record["stars"] = [int(number.replace(",", ""))]
            if not rm[4].strip():
                error(line, rm[1], "一句话简介为空")
            rows.append(record)
        elif side == "详解" and value.startswith("###"):
            current = None
            dm = DETAIL.fullmatch(value)
            if not dm:
                error(line, category or "详解", "详解标题格式错误（须含编号和项目链接）")
                continue
            current = item(line, dm[2], dm[3])
            current["number"] = int(dm[1])
            if not category:
                error(line, dm[2], "详解缺少有效分类标题")
            details.append(current)
        elif value.startswith("⭐"):
            sm = STAR.fullmatch(value)
            if current is None:
                error(line, category or "星数", "星数不属于有效详解条目")
            else:
                valid = sm and NUMBER.fullmatch(sm[1])
                current["stars"].append(int(sm[1].replace(",", "")) if valid else None)
                if not valid:
                    error(line, current["label"], "详解星数格式错误")
    if fence:
        error(1, "README", "代码围栏未闭合")
    if markers != 1:
        error(1, "README", f"项目详解分界标题应有一次，实际 {markers}")
    for name in CATEGORIES:
        for kind, entries in (("表", rows), ("详解", details)):
            headings = sections.get((kind, name), [])
            if len(headings) != 1:
                error(headings[0][0] if headings else 1, name, f"{kind}分类标题应有一次，实际 {len(headings)}")
            actual = sum(e["category"] == name for e in entries)
            for line, declared in headings:
                if declared != actual:
                    error(line, name, f"{kind}声明 {declared} 项，实际 {actual} 项")
    if len(totals) != 1:
        error(1, "README", f"导语须有一次总项目数，实际 {len(totals)} 次")
    elif totals[0][1] != len(rows) or totals[0][1] != len(details):
        error(totals[0][0], "README", f"导语总数 {totals[0][1]}；表 {len(rows)}；详解 {len(details)}")
    maps = []
    for kind, entries in (("表", rows), ("详解", details)):
        index = {}
        for entry in entries:
            key = entry["key"]
            if key in index and key is not None:
                error(entry["line"], entry["label"], f"{kind}仓库重复，首次见 L{index[key]['line']}")
            if key is not None:
                index.setdefault(key, entry)
        maps.append(index)
    table, detail = maps
    for pos, entry in enumerate(details, 1):
        if entry["number"] != pos:
            error(entry["line"], entry["label"], f"编号应为 {pos}，实际 {entry['number']}")
        if len(entry["stars"]) != 1:
            error(entry["line"], entry["label"], f"详解须恰有一个星数，实际 {len(entry['stars'])}")
    for key in sorted(table.keys() | detail.keys()):
        a, b = table.get(key), detail.get(key)
        if a is None or b is None:
            entry = a or b
            error(entry["line"], entry["label"], "缺少" + ("表项" if a is None else "详解"))
        else:
            for field, name in (("category", "分类"), ("label", "标签"), ("stars", "星数")):
                if a[field] != b[field]:
                    error(a["line"], a["label"], f"两处{name}不一致（详解 L{b['line']}）：{a[field]!r} / {b[field]!r}")
    if len(rows) == len(details) and table.keys() == detail.keys() and [e["key"] for e in rows] != [e["key"] for e in details]:
        pos = next(i for i, (a, b) in enumerate(zip(rows, details)) if a["key"] != b["key"])
        a, b = rows[pos], details[pos]
        error(a["line"], a["label"], f"项目顺序不一致：同位置详解 L{b['line']} 为 {b['label']}")
    return errors, rows, details

def self_test(text, rows, details):
    lines = text.splitlines()
    a, b, d, nxt = rows[0], rows[1], details[0], details[1]
    ri, di = a["line"] - 1, d["line"] - 1
    si = next(i for i in range(di + 1, nxt["line"] - 1) if lines[i].strip().startswith("⭐"))
    cases = {
        "删表项": {ri: ""}, "错星数": {ri: lines[ri].replace(f"| {a['stars'][0]:,} |", f"| {a['stars'][0] + 1:,} |")},
        "重复仓库": {b["line"] - 1: lines[ri]}, "追加重复仓库": {ri: lines[ri] + "\n" + lines[ri]},
        "跳号": {di: lines[di].replace("### 1.", "### 2.", 1)},
        "缺详解": {i: "" for i in range(di, nxt["line"] - 1)}, "无星数": {si: ""},
        "坏表格式": {ri: lines[ri].replace("](", "] (", 1)}, "非法表星数": {ri: lines[ri].replace(f"| {a['stars'][0]:,} |", "| N/A |")},
        "坏URL路径": {ri: lines[ri].replace(a["url"], a["url"] + "/tree/main")},
        "坏URL查询": {di: lines[di].replace(d["url"], d["url"] + "?tab=readme")},
        "坏详解星数": {si: "⭐ 1,23 ｜ Python"}, "重复星数": {si: lines[si] + "\n" + lines[si]},
        "坏详解标题": {di: lines[di].replace("](", "] (", 1)},
        "错标签": {di: lines[di].replace(f"[{d['label']}]", "[wrong/project]", 1)},
        "交换表顺序": {ri: lines[b["line"] - 1], b["line"] - 1: lines[ri]},
    }
    other = next(e for e in rows if e["category"] != a["category"])
    cases["跨分类"] = {ri: "", other["line"] - 1: lines[other["line"] - 1] + "\n" + lines[ri]}
    passed = True
    for name, changes in cases.items():
        mutated = "\n".join(changes.get(i, line) for i, line in enumerate(lines))
        errors, _, _ = check(mutated)
        print(f"SELF-TEST {'PASS' if errors else 'FAIL'} {name}" + (f"：{errors[0]}" if errors else "：故障未检出"))
        passed &= bool(errors)
    accepted = text + "\n```markdown\n" + lines[ri] + "\n" + lines[di] + "\n```\n"
    normalized = text.replace(a["url"], a["url"].upper() + ".git/")
    for name, sample in (("忽略代码围栏", accepted), ("规范URL大小写/git/尾斜杠", normalized)):
        errors, _, _ = check(sample)
        print(f"SELF-TEST {'FAIL' if errors else 'PASS'} {name}")
        passed &= not errors
    return passed

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "README.md")
    parser.add_argument("--self-test", action="store_true", help="Run in-memory mutation tests after checking the file")
    args = parser.parse_args()
    try:
        errors, rows, details = check(text := args.path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as exc:
        print(f"ERROR {args.path}: {exc}")
        return 1
    for message in errors:
        print("ERROR " + message)
    if errors:
        return 1
    print(f"PASS {args.path}: 表 {len(rows)} 项 / 详解 {len(details)} 项，四分类、链接、顺序、编号及星数一致")
    return 0 if not args.self_test or self_test(text, rows, details) else 1

if __name__ == "__main__":
    raise SystemExit(main())
