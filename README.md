# GitHub 星标项目手册

**先看表，再翻详解**：开头四张表一眼扫过 65 个项目是干嘛的；想深入了解某个项目，再往下翻对应条目的详细说明。

**后续维护按此模板**：每个新项目在对应分类的一览表填写仓库链接、查询时星数和一句话定位；在详解末尾记录核验日期、当时的仓库所属账号及类型、仓库 ID、创建日期和许可标识，再依据项目官方 README 写清用途、主要功能、适用范围与已知限制，并保留来源链接。所属账号不当作最初作者，未核实内容明确标注；链接失效时保留最近一次说明并注明检查结果。个人使用感受仅在实际体验后记录；公开手册只收录第三方收藏项目。

- 星数为 2026-09-22 查询值（一览表与详解同源）
- 本次公开 stars 快照读取于 2026-09-22 14:07（UTC+8）；星数会动态变化
- 仓库身份信息核验于 2026-09-24：所属账号、仓库 ID、创建日期和许可标识来自当时可访问的 GitHub 仓库资料；所属账号不一定是项目最初创建者，许可标识也不替代许可文件
- 本轮还据项目官方 README 补充了 8 个原先较短的详解；其余功能说明沿用 2026-09-22 清单，未逐项重新核实

## 🤖 AI（27 个）

| 项目 | 星数 | 一句话简介 |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 289,823 | 给编程 AI 的软件开发方法论技能包 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 264,870 | AI agent 工作流的性能优化与治理系统 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 247,845 | 会自我改进、常驻云端的 AI 智能体 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 209,214 | 开源的终端 AI 编程智能体 |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 232,616 | DeepSeek 官方「一切皆插件」的 agent 框架 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 98,210 | 面向 AI 编程 agent 的生产级工程技能库 |
| [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus) | 87,476 | 自托管的个人 AI 工作空间全家桶 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 88,765 | 编码 agent 的自托管开发者控制中心 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 82,829 | 字节开源的长时程超级 agent 调度框架 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 84,488 | 给 AI agent 一键装上互联网能力的 CLI |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 52,060 | 跨平台多模型 AI 桌面客户端 |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 49,832 | 开源中文书《深入理解 AI Agent》全书仓库 |
| [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 35,668 | 终端里的 DeepSeek 原生编程 agent |
| [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | 33,658 | LLM 角色扮演 / 小说共创前端 |
| [ai-shifu/ChatALL](https://github.com/ai-shifu/ChatALL) | 16,501 | 并发向多个 AI 机器人发问，同屏对比 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 115,822 | 让 AI agent 通过浏览器访问和自动化操作网站 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 267,321 | 面向真实工程的 AI 编程技能集合 |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 23,266 | 编程 AI 代理的控制面板，手机/网页/桌面四端遥控 |
| [dimthink/PriceAI](https://github.com/dimthink/PriceAI) | 3,301 | AI 订阅卡网与中转 API 比价雷达：聚合订阅与 API 渠道，展示价格、库存、来源和风险边界。 |
| [Mars-Sea/dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) | 304 | DeepSeek Harness 的非官方 Command Code provider：模型目录、计划/推理、图像、搜索与多账号支持。 |
| [dingminhua/dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy) | 32 | 把本机登录的国内/国际 WorkBuddy 模型接入 DSH，提供只读积分概览与模型管理。 |
| [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 16,562 | DeepSeek Harness（dsh）插件精选列表。 |
| [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | 28,355 | 基于 DeepSeek Harness 的 Windows/macOS 开源桌面客户端，集成本地 Web UI、Host 与插件系统。 |
| [88lin/workbuddy-auto-signin](https://github.com/88lin/workbuddy-auto-signin) | 679 | WorkBuddy 每日签到积分自动领取脚本：纯 Python，读取本机登录态并支持定时运行。 |
| [corrinehu/dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect) | 161 | 将 WorkBuddy 与 WorkBuddy AI 模型接入 DSH，支持双供应商、只读积分与模型管理。 |
| [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere) | 1,120 | 跨设备的开源 Agent 工作台：连接工作设备，在桌面、手机和 Web 管理会话、文件与终端。 |
| [blader/humanizer](https://github.com/blader/humanizer) | 51,158 | 适用于支持 skills 的 agent 的 Markdown 技能：改写 AI 腔文本而不改变原意，并保留事实细节。 |

## 📖 阅读与影音（17 个）

| 项目 | 星数 | 一句话简介 |
|---|---|---|
| [lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | 53,823 | 开源桌面音乐软件，支持自定义音源 |
| [gedoor/legado](https://github.com/gedoor/legado) | 47,083 | 阅读 3.0 安卓阅读器 ⚠️ 作者已发侵权公告 |
| [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | 30,148 | 自定义规则的番剧采集观看 App |
| [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader) | 28,257 | 全平台电子书管理与阅读器 |
| [AZeC4/TelegramGroup](https://github.com/AZeC4/TelegramGroup) | 23,280 | Telegram 群组 / 频道 / 机器人导航合集 |
| [XIU2/Yuedu](https://github.com/XIU2/Yuedu) | 12,320 | 「阅读」App 自用书源分享 |
| [listen1/listen1_chrome_extension](https://github.com/listen1/listen1_chrome_extension) | 12,100 | 聚合七家音乐平台的浏览器扩展 |
| [listen1/listen1_desktop](https://github.com/listen1/listen1_desktop) | 11,405 | Listen 1 音乐聚合的桌面版 |
| [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | 9,036 | 洛雪音乐第三方音源导入链接集合 |
| [aoaostar/legado](https://github.com/aoaostar/legado) | 6,440 | 「阅读」App 书源与配套资源集合站 |
| [Macrohard0001/lx-ikun-music-sources](https://github.com/Macrohard0001/lx-ikun-music-sources) | 2,473 | LX Music 与 IKUN Music 音源收集 |
| [best-fan/iptv-sources](https://github.com/best-fan/iptv-sources) | 747 | 每日自动更新的电视直播源 |
| [lyswhut/lx-music-mobile](https://github.com/lyswhut/lx-music-mobile) | 18,377 | 基于 React Native 的移动端音乐软件 |
| [cwuom/NeriPlayer](https://github.com/cwuom/NeriPlayer) | 3,498 | 多源在线播放+本地管理的原生安卓音乐播放器 |
| [Moriafly/SaltPlayerSource](https://github.com/Moriafly/SaltPlayerSource) | 7,377 | 椒盐音乐播放器官方仓库（安卓包发布与反馈） |
| [chthollyphile/folia-major](https://github.com/chthollyphile/folia-major) | 2,893 | 以全屏沉浸式歌词为核心的多平台音乐播放器，支持在线/本地音乐、歌词匹配与动画主题。 |
| [ZWolken/Light-Novel-Yuedu-Source](https://github.com/ZWolken/Light-Novel-Yuedu-Source) | 441 | 轻小说阅读书源合集，含日轻、国轻、日语原版及合集；README 明示项目处在半维护周期。 |

## 🎮 游戏与串流（8 个）

| 项目 | 星数 | 一句话简介 |
|---|---|---|
| [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 150,160 | 安卓投屏与电脑键鼠控制 |
| [AlkaidLab/foundation-sunshine](https://github.com/AlkaidLab/foundation-sunshine) | 6,938 | 游戏串流主机端（Sunshine 增强版） |
| [qiin2333/moonlight-vplus](https://github.com/qiin2333/moonlight-vplus) | 3,769 | Moonlight 安卓串流客户端增强版 |
| [DSPBluePrints/FactoryBluePrints](https://github.com/DSPBluePrints/FactoryBluePrints) | 2,440 | 戴森球计划社区工厂蓝图仓库 |
| [mcthesw/game-save-manager](https://github.com/mcthesw/game-save-manager) | 1,142 | 图形化开源游戏存档管理器 |
| [alkaidjin/Maa-Assistant-Browndust2](https://github.com/alkaidjin/Maa-Assistant-Browndust2) | 67 | BrownDust2 手游日常自动化助手 |
| [GodRaymond233/ok-bd2](https://github.com/GodRaymond233/ok-bd2) | 103 | 基于 ok-script 的 BrownDust2 自动化助手 |
| [MadestSamurai/bd2-infinite-gacha](https://github.com/MadestSamurai/bd2-infinite-gacha) | 10 | BrownDust II Windows 无限抽抽乐助手：按 A/B 目标与停止条件刷新，命中后保留结果确认。 |

## 🛠️ 自托管与效率工具（13 个）

| 项目 | 星数 | 一句话简介 |
|---|---|---|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 146,258 | Clash Meta 图形代理客户端 |
| [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 46,455 | 思源笔记，可自托管的开源知识库 |
| [waydabber/BetterDisplay](https://github.com/waydabber/BetterDisplay) | 33,746 | Mac 显示器深度管理工具 |
| [jiangrui1994/CloudSaver](https://github.com/jiangrui1994/CloudSaver) | 9,317 | 网盘资源搜索与一键转存（自部署） |
| [Nevcairiel/LAVFilters](https://github.com/Nevcairiel/LAVFilters) | 9,154 | Windows 视频解码滤镜套装 |
| [floccusaddon/floccus](https://github.com/floccusaddon/floccus) | 8,477 | 跨浏览器跨设备私密书签同步 |
| [Ponphil/LitePan](https://github.com/Ponphil/LitePan) | 1,260 | 多网盘聚合挂载与媒体库整理 |
| [MAXeaglet/commandcode-proxy](https://github.com/MAXeaglet/commandcode-proxy) | 668 | 将 Command Code API 转换为 OpenAI/Anthropic 兼容端点的单文件零依赖反代。 |
| [Patrick-mufeng/cmdgo-bridge](https://github.com/Patrick-mufeng/cmdgo-bridge) | 14 | 把 Command Code Go 套餐包装为 OpenAI 兼容本地桥，含 OAuth、多账号池与 Web 控制台。 |
| [linguo2625469/workbuddy2api-panel](https://github.com/linguo2625469/workbuddy2api-panel) | 660 | 腾讯 CodeBuddy 的 OpenAI 兼容多账号网关增强分支，附 Web 管理面板与任务自动化。 |
| [Sliverkiss/workbuddy2api](https://github.com/Sliverkiss/workbuddy2api) | 1,428 | 将 CodeBuddy 账号包装为 OpenAI 兼容网关，支持 OAuth、多账号轮转、熔断与流式响应。 |
| [MetaCubeX/ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid) | 46,527 | Clash.Meta 的 Android 图形界面，支持 Android 5.0+ 及多架构构建。 |
| [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | 2,275 | 本地优先的桌面小组件：追踪多款 AI 编程工具的 token 用量、花费与限额，并支持多设备同步。 |

---

# 项目详解

## 🤖 AI · 详解（27 个）

### 1. [obra/superpowers](https://github.com/obra/superpowers)

⭐ 289,823 ｜ Shell

> **身份快照（2026-09-24）**：仓库所属账号 [obra](https://github.com/obra)（个人账号）；GitHub 仓库 ID `1073224795`；仓库创建于 2025-10-09；GitHub 许可标识：`MIT`。

给编程 AI 的一整套软件开发方法论技能包，解决「AI 上来就乱写代码」的问题。它让 AI 先反问需求、梳理出规格说明分块给你确认，设计签核后再生成实现计划，然后进入子代理驱动的开发流程——每个工程任务由子代理执行、被检查复核，AI 可以连续自主工作数小时不跑偏。支持 Claude Code、Codex、Cursor、OpenCode 等十余种接入方式，技能按场景自动触发。

### 2. [affaan-m/ECC](https://github.com/affaan-m/ECC)

⭐ 264,870 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [affaan-m](https://github.com/affaan-m)（个人账号）；GitHub 仓库 ID `1136590548`；仓库创建于 2026-01-18；GitHub 许可标识：`MIT`。

面向 Claude Code、Codex、Cursor 等编程 AI 的性能优化与治理系统。核心做四件事：把规则、技能、子代理分层管理（技能按需加载、上下文互相隔离）；强制测试驱动开发流程，让 AI 产出的不只是代码而是证据链（计划、失败测试、通过测试、审查发现）；用统一的本地 Markdown 格式在不同 AI 工具之间共享持久记忆；把 AI 工具本身作为攻击面做安全扫描。官方主页 ecc.tools。

### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

⭐ 247,845 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [NousResearch](https://github.com/NousResearch)（组织账号）；GitHub 仓库 ID `1024554267`；仓库创建于 2025-07-22；GitHub 许可标识：`MIT`。

会自我改进、常驻云端的个人 AI 智能体。内置学习闭环：从经验中自动创建技能、主动把知识写入持久记忆、可全文检索自己过去的会话、越用越了解你。一个网关进程同时接入 Telegram、Discord、Slack、WhatsApp 等聊天软件，支持语音和跨平台会话延续；内置定时任务（日报、备份、周审计，自然语言配置）；可跑在 5 美元的 VPS 上——人在 Telegram 里遥控云端干活。

### 4. [anomalyco/opencode](https://github.com/anomalyco/opencode)

⭐ 209,214 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [anomalyco](https://github.com/anomalyco)（组织账号）；GitHub 仓库 ID `975734319`；仓库创建于 2025-04-30；GitHub 许可标识：`MIT`。

开源的终端 AI 编程智能体（the open source coding agent），在命令行里用 AI 写代码。安装渠道覆盖最全（npm、brew、scoop 等几乎全部包管理器），另有桌面应用（Beta）。官方主页 opencode.ai，README 提供 21 种语言版本。

### 5. [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

⭐ 232,616 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [deepseek-ai](https://github.com/deepseek-ai)（组织账号）；GitHub 仓库 ID `1333065091`；仓库创建于 2026-08-13；GitHub 许可标识：`MIT`。

DeepSeek 官方开源的智能体框架（命令名 `dsh`），架构核心是「一切皆插件」，底层由 Cordis 插件系统驱动。装好 Node.js 后一条命令即可在本地浏览器启动 Web UI。处于开发者预览阶段，官方明示后续会有破坏性变更。MIT 协议。

### 6. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

⭐ 98,210 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [addyosmani](https://github.com/addyosmani)（个人账号）；GitHub 仓库 ID `1158722119`；仓库创建于 2026-02-15；GitHub 许可标识：`MIT`。

把资深工程师的工作流与质量门禁打包成技能库，喂给 AI 编程代理。8 个斜杠命令映射完整开发生命周期：先规格（/spec）、再计划（/plan）、一次一片地写（/build）、测试即证明（/test）、审查（/review）、性能（/webperf）、简化（/code-simplify）、发布（/ship）。可装入 Claude Code、Cursor、Codex 等 70+ 种 AI 工具。官方主页 skills.addy.ie。

### 7. [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus)

⭐ 87,476 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [odysseus-dev](https://github.com/odysseus-dev)（组织账号）；GitHub 仓库 ID `1255180606`；仓库创建于 2026-05-31；GitHub 许可标识：`AGPL-3.0`。

自托管的个人 AI 工作空间全家桶：一套 Docker Compose（默认端口 7000）集成聊天、智能体、深度研究、文档写作、邮件分诊、笔记与日历。支持本地或 API 模型、MCP 工具、记忆系统；深度研究功能能多步联网查资料、读原文、出报告；邮件模块对接 IMAP/SMTP 做收件箱自动分诊、摘要、回复草稿。官方主页 odysseus-dev.github.io/odysseus。

### 8. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)

⭐ 88,765 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [OpenHands](https://github.com/OpenHands)（组织账号）；GitHub 仓库 ID `771302083`；仓库创建于 2024-03-13；GitHub 许可标识：`MIT`。

编码 AI 的自托管控制中心（主打形态 Agent Canvas）：把编程 AI 变成全天候在线的工程团队指挥台。可以跑 OpenHands、Claude Code、Codex 等任意兼容智能体；后端灵活——本地、Docker、虚拟机或云端，切换不丢上下文；支持自动化工作流（如 GitHub issue 自动拆解成任务、报告自动发 Slack）。官方主页 openhands.dev。

### 9. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

⭐ 82,829 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [bytedance](https://github.com/bytedance)（组织账号）；GitHub 仓库 ID `979115477`；仓库创建于 2025-05-07；GitHub 许可标识：`MIT`。

字节跳动开源的长时程超级智能体调度框架（DeerFlow），编排子代理、记忆与沙箱完成从几分钟到几小时的复杂任务，能力靠可扩展技能延伸。2.0 版为彻底重写（1.x 的深度研究框架维护在旧分支），集成了字节自研的 InfoQuest 搜索与爬取工具集。官方主页 deerflow.tech。

### 10. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

⭐ 84,488 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [Panniantong](https://github.com/Panniantong)（个人账号）；GitHub 仓库 ID `1165277268`；仓库创建于 2026-02-24；GitHub 许可标识：`MIT`。

给 AI 智能体一键装上「读遍全网」能力的命令行工具，解决 AI 上网抓瞎的问题：读 YouTube 拿不到字幕、搜推特要付费 API、Reddit 被 403 拦、小红书要登录、网页抓回来一堆没法读的 HTML。一个 CLI 覆盖 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书等平台的读取与搜索，零 API 费用，安装只需把 install.md 丢给 AI 自动完成。

### 11. [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

⭐ 52,060 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [CherryHQ](https://github.com/CherryHQ)（组织账号）；GitHub 仓库 ID `805155266`；仓库创建于 2024-05-24；GitHub 许可标识：`AGPL-3.0`。

跨平台多模型 AI 桌面客户端（Windows/Mac/Linux），一个软件统一访问各家大模型：云服务（OpenAI、Gemini、Anthropic）、网页服务、本地模型（Ollama、LM Studio）都能接。内置 300+ 预配置助手、多模型同屏对话、文档/PDF/图片处理、AI 翻译、WebDAV 备份、MCP 支持，开箱即用。官方主页 cherryai.com。

### 12. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

⭐ 49,832 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [bojieli](https://github.com/bojieli)（个人账号）；GitHub 仓库 ID `1053118194`；仓库创建于 2025-09-09；GitHub 许可标识：`Apache-2.0`。

开源中文技术书《深入理解 AI Agent：设计原理与工程实践》（李博杰著）全书仓库：正文、编译好的 PDF/EPUB、按章配套代码与上百个可动手跑的实验。围绕「Agent = LLM + 上下文 + 工具」核心公式，10 章从原理讲到工程实战，已有 14 种语言翻译，在线阅读站支持全文搜索。书稿已升级至 2.0 版。

### 13. [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)

⭐ 35,668 ｜ Go

> **身份快照（2026-09-24）**：仓库所属账号 [esengine](https://github.com/esengine)（个人账号）；GitHub 仓库 ID `1216785679`；仓库创建于 2026-04-21；GitHub 许可标识：`MIT`。

终端里的 DeepSeek 原生编程智能体，可长时间挂着自主干活：围绕缓存稳定性设计，长时运行仍然可控、可读、可撤销。单个 Go 二进制文件，一个本地引擎四种入口（终端、桌面应用、浏览器、编辑器）；带计划模式、权限体系、工作区沙箱和每轮检查点。配置驱动，DeepSeek 预置，任意 OpenAI 兼容端点均可接入。官方主页 reasonix.io。

### 14. [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern)

⭐ 33,658 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [SillyTavern](https://github.com/SillyTavern)（组织账号）；GitHub 仓库 ID `599524116`；仓库创建于 2023-02-09；GitHub 许可标识：`AGPL-3.0`。

面向高级用户的本地 LLM 前端，角色扮演与小说共创的主力工具。本地安装的交互界面，统一对接文本大模型、图像生成与语音合成；核心能力：角色卡系统（设定 AI 行为与人格、对话持久化）、World Info 世界观构建、多角色群聊、内置文档知识库（RAG）；扩展生态覆盖生图、TTS、翻译、自动摘要、联网搜索。支持 Windows/Mac/Linux/Android（Termux）/Docker。官方文档 docs.sillytavern.app。

### 15. [ai-shifu/ChatALL](https://github.com/ai-shifu/ChatALL)

⭐ 16,501 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [ai-shifu](https://github.com/ai-shifu)（组织账号）；GitHub 仓库 ID `625187946`；仓库创建于 2023-04-08；GitHub 许可标识：`Apache-2.0`。

中文名「齐叨」。把同一个问题并发发给多个 AI 机器人（ChatGPT、Claude、文心一言、ChatGLM 等，部分走网页端、部分走 API），同屏对比各家回答帮你挑最优。适合想找最佳答案的重度用户、直观对比模型优劣的研究者、调试提示词找最优基础模型的开发者。官方主页 chatall.ai。

### 16. [browser-use/browser-use](https://github.com/browser-use/browser-use)

⭐ 115,822 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [browser-use](https://github.com/browser-use)（组织账号）；GitHub 仓库 ID `881458615`；仓库创建于 2024-10-31；GitHub 许可标识：`MIT`。

该仓库提供 Python 浏览器智能体库，可连接本地或云端浏览器，由用户选择的语言模型执行网页任务，例如检索和表单操作。README 还区分了供既有代理使用的 CLI 与托管 Agent API；云浏览器和托管服务需单独配置，部分服务按使用量计费。登录限制和验证码由目标网站决定，项目文档不保证每个任务都能完成。

### 17. [mattpocock/skills](https://github.com/mattpocock/skills)

⭐ 267,321 ｜ Shell

> **身份快照（2026-09-24）**：仓库所属账号 [mattpocock](https://github.com/mattpocock)（个人账号）；GitHub 仓库 ID `1148788086`；仓库创建于 2026-02-03；GitHub 许可标识：`MIT`。

这是 Matt Pocock 分享的工程类 agent skills 集合，README 称这些工作流文件小巧、可组合并可自行调整。可通过 Claude Code 插件安装只读版本，或用 skills.sh 复制到项目中编辑；原生 Codex 插件仍列在路线图，setup skill 可配置 issue tracker、标签和文档存放位置。

### 18. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

⭐ 23,266 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [pingdotgg](https://github.com/pingdotgg)（组织账号）；GitHub 仓库 ID `1153130349`；仓库创建于 2026-02-08；GitHub 许可标识：`MIT`。

「agent harness 控制面板」：把电脑上的编程 AI 代理统一装进一个控制台，配 iOS/Android 手机 App、Web 端与 Electron 桌面端，随时随地远程操控。直接用你现有的订阅——Claude Code、Codex、Cursor、Grok Build、OpenCode 装好登录即可被接管；`npx t3@latest` 免安装试用（需 Node.js 22+）。开源开放，官方明示方向跑偏随时可 fork 自建。官方主页 t3.codes。

### 19. [dimthink/PriceAI](https://github.com/dimthink/PriceAI)

⭐ 3,301 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [dimthink](https://github.com/dimthink)（个人账号）；GitHub 仓库 ID `1233142602`；仓库创建于 2026-05-08；GitHub 许可标识未识别。

PriceAI 的 README 将项目定位为 AI 订阅与 API 价格信息整理工具，覆盖官方订阅地区价、第三方卡网、官方 API 和中转站报价，并列出来源、库存、倍率及更新时间。README 明确称项目不销售、不代收款、也不替渠道担保；部分价格和库存仍需返回原站核验，第三方渠道不能视为官方服务。

### 20. [Mars-Sea/dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider)

⭐ 304 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [Mars-Sea](https://github.com/Mars-Sea)（个人账号）；GitHub 仓库 ID `1334118559`；仓库创建于 2026-08-14；GitHub 许可标识：`MIT`。

这是 DeepSeek Harness 的非官方 Command Code LLM provider 插件，提供 live model catalog、计划感知选择、推理档位、图片输入、网页搜索、设置页/终端配置和多账号轮换。

### 21. [dingminhua/dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy)

⭐ 32 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [dingminhua](https://github.com/dingminhua)（个人账号）；GitHub 仓库 ID `1349641014`；仓库创建于 2026-08-28；GitHub 许可标识：`MIT`。

独立 DSH bundle 插件，把本机登录的国内版与国际版 WorkBuddy AI 接入两个并行 provider，提供只读积分概览、模型目录刷新、模型勾选与账号切换。

### 22. [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)

⭐ 16,562 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin)（组织账号）；GitHub 仓库 ID `1333175049`；仓库创建于 2026-08-13；GitHub 许可标识：`CC0-1.0`。

DeepSeek Harness（dsh）插件精选列表。

### 23. [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop)

⭐ 28,355 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [anywhere-labs](https://github.com/anywhere-labs)（组织账号）；GitHub 仓库 ID `1333321333`；仓库创建于 2026-08-13；GitHub 许可标识：`MIT`。

基于 DeepSeek Harness 的 Windows/macOS 开源桌面客户端，把本地 Web UI、Host 服务和插件系统集成到原生桌面应用，并提供窗口、托盘、终端、更新与工作配置。

### 24. [88lin/workbuddy-auto-signin](https://github.com/88lin/workbuddy-auto-signin)

⭐ 679 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [88lin](https://github.com/88lin)（个人账号）；GitHub 仓库 ID `1338741785`；仓库创建于 2026-08-18；GitHub 许可标识：`MIT`。

自包含的 Python 脚本，每天自动领取 WorkBuddy 签到积分与成长中心奖励；读取本机登录态，不内置密钥，支持 Windows/macOS/Linux 定时运行。

### 25. [corrinehu/dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect)

⭐ 161 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [corrinehu](https://github.com/corrinehu)（个人账号）；GitHub 仓库 ID `1337545070`；仓库创建于 2026-08-17；GitHub 许可标识：`MIT`。

这是把本机 WorkBuddy 或 WorkBuddy AI 已登录账号中的模型接入 DeepSeek Harness 的插件，国内版与国际版分别显示模型分组和账号积分。README 提供模型目录刷新、可见性设置、图片输入及只读积分信息；图片和推理档位能力依模型而异，未声明的档位可手动检测但会发送请求并可能消耗积分，检测结果不保证改变模型实际表现。

### 26. [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere)

⭐ 1,120 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [anywhere-labs](https://github.com/anywhere-labs)（组织账号）；GitHub 仓库 ID `1246211773`；仓库创建于 2026-05-22；GitHub 许可标识：未标出。

跨设备开源 Agent 工作台，连接运行 Codex、Claude Code 或 DSH 的工作设备，在桌面、手机和 Web 查看会话、回复请求、管理文件与终端；支持 Cloud 或自托管。

### 27. [blader/humanizer](https://github.com/blader/humanizer)

⭐ 51,158 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [blader](https://github.com/blader)（个人账号）；GitHub 仓库 ID `1136666433`；仓库创建于 2026-01-18；GitHub 许可标识：`MIT`。

Markdown 形式的 agent skill，改写 AI 腔文本但不改变含义；逐项标出模式、检查事实细节，可按指定文风重写，并保持代码、数据、frontmatter 与链接目标不变。

## 📖 阅读与影音 · 详解（17 个）

### 28. [lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop)

⭐ 53,823 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [lyswhut](https://github.com/lyswhut)（个人账号）；GitHub 仓库 ID `202367615`；仓库创建于 2019-08-14；GitHub 许可标识：`Apache-2.0`。

洛雪音乐桌面版，开源免费的音乐播放软件（Windows/macOS/Linux），本清单里好几个音源仓库都是给它供源的。支持自定义音源、浏览器调起播放（Scheme URL）、自部署数据同步服务实现多端同步、开放 API 供第三方软件调用。官方文档 lyswhut.github.io/lx-music-doc；移动版是独立项目 lx-music-mobile。

### 29. [gedoor/legado](https://github.com/gedoor/legado)

⭐ 47,083 ｜ Kotlin

> **身份快照（2026-09-24）**：仓库所属账号 [gedoor](https://github.com/gedoor)（个人账号）；GitHub 仓库 ID `187961907`；仓库创建于 2019-05-22；GitHub 许可标识：未标出。

原清单记录其为“阅读 3.0”安卓阅读器。2026-09-24 查看官方 README 时，页面已改为侵权公告，并附阅文集团知识产权保护公告链接；现行 README 不再提供功能、安装和书源说明。这里保留项目原用途以便辨认，不据此判断软件当前可用性。

### 30. [Predidit/Kazumi](https://github.com/Predidit/Kazumi)

⭐ 30,148 ｜ Dart

> **身份快照（2026-09-24）**：仓库所属账号 [Predidit](https://github.com/Predidit)（个人账号）；GitHub 仓库 ID `798049841`；仓库创建于 2024-05-09；GitHub 许可标识：`GPL-3.0`。

自定义规则的番剧采集与在线观看应用：用最多五行 XPath 规则就能构建一个采集源，支持规则导入分享。播放体验齐全——弹幕、倍速、硬件加速、Anime4K 实时超分、外部播放器、DLNA 投屏、「一起看」；带追番列表、跨设备同步、番剧下载。全平台覆盖：Android、Windows、macOS、Linux、iOS（侧载）、鸿蒙（侧载）。官方主页 kazumi.app。

### 31. [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader)

⭐ 28,257 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [koodo-reader](https://github.com/koodo-reader)（组织账号）；GitHub 仓库 ID `245049028`；仓库创建于 2020-03-05；GitHub 许可标识：`AGPL-3.0`。

全平台电子书管理与阅读器。格式覆盖广（EPUB、PDF、mobi、azw3、txt、漫画压缩包、docx 等）；云同步支持 WebDAV、OneDrive、Google Drive 等十余种通道；AI 能力可接自定义模型做翻译、词典、摘要；笔记可导出到 Notion/Obsidian/Readwise，生词自动同步 Anki 与欧路词典。隐私优先：无追踪、不上传阅读数据。支持 Windows/Mac/Linux/Android/iOS/Web。官方主页 koodoreader.com。

### 32. [AZeC4/TelegramGroup](https://github.com/AZeC4/TelegramGroup)

⭐ 23,280 ｜ 纯数据仓库

> **身份快照（2026-09-24）**：仓库所属账号 [AZeC4](https://github.com/AZeC4)（个人账号）；GitHub 仓库 ID `121010586`；仓库创建于 2018-02-10；GitHub 许可标识：未标出。

Telegram 群组/频道/机器人导航合集，收录上万个群的清单与搜索机器人推荐，配套网站 dianbaodaohang.com。注意：仓库内容含较多推广返利链接（机场、AI 导航等营销板块），使用时自行甄别；作者也提醒电报账号建议用中文名防风控封号。

### 33. [XIU2/Yuedu](https://github.com/XIU2/Yuedu)

⭐ 12,320 ｜ 纯数据仓库

> **身份快照（2026-09-24）**：仓库所属账号 [XIU2](https://github.com/XIU2)（个人账号）；GitHub 仓库 ID `212751942`；仓库创建于 2019-10-04；GitHub 许可标识：`GPL-3.0`。

作者 XIU2 分享的「阅读」App（上一条的 gedoor/legado）自用书源：一部分网上搜集，一部分自己写的规则。README 把「阅读」的原理讲得清楚——它本质是个空壳阅读器，靠书源规则解析小说网站的搜索、目录、正文页。作者明示书源较少、维护不积极，推荐搭配其他综合书源库使用。配套分享站 yuedu.xiu2.xyz。

### 34. [listen1/listen1_chrome_extension](https://github.com/listen1/listen1_chrome_extension)

⭐ 12,100 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [listen1](https://github.com/listen1)（个人账号）；GitHub 仓库 ID `57430416`；仓库创建于 2016-04-30；GitHub 许可标识：`MIT`。

Listen 1 浏览器扩展：一个扩展聚合网易云音乐、QQ 音乐、酷狗、酷我、bilibili、咪咕、千千音乐七个平台，解决「想听的歌因版权散落各平台」的问题。新版本支持自动切换播放源——一首歌在当前平台不可用时自动搜其他平台找可用的。Chrome/Firefox/Edge 商店均可安装。官方主页 listen1.github.io/listen1。

⚠️ **更新停滞（2026-09-03 记录）**：仓库最近一次代码提交在 2025-06，已一年余未更新；介意维护状态的可改用桌面版或洛雪音乐。

### 35. [listen1/listen1_desktop](https://github.com/listen1/listen1_desktop)

⭐ 11,405 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [listen1](https://github.com/listen1)（个人账号）；GitHub 仓库 ID `59187489`；仓库创建于 2016-05-19；GitHub 许可标识：`MIT`。

Listen 1 的跨平台桌面版（Windows/Mac/Linux），聚合平台与扩展版一致（七家音乐平台），带收藏与自建歌单。与浏览器扩展共享核心代码，是两个入口选一个用即可的关系。

### 36. [pdone/lx-music-source](https://github.com/pdone/lx-music-source)

⭐ 9,036 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [pdone](https://github.com/pdone)（个人账号）；GitHub 仓库 ID `888865009`；仓库创建于 2024-11-15；GitHub 许可标识：未标出。

洛雪音乐第三方音源导入链接集合：收录 SixYin、Huibq、Flower、LX、ikun、Grass、JuheApi、QDY 八个音源的最新版导入地址，每个都提供原始链接与加速链接（照顾访问 GitHub 受限的用户）。给洛雪音乐桌面版/移动版供源的「源头」仓库之一。

### 37. [aoaostar/legado](https://github.com/aoaostar/legado)

⭐ 6,440 ｜ HTML

> **身份快照（2026-09-24）**：仓库所属账号 [aoaostar](https://github.com/aoaostar)（个人账号）；GitHub 仓库 ID `571581970`；仓库创建于 2022-11-28；GitHub 许可标识：未标出。

「阅读」App 的书源与配套资源集合站（与阅读 App 本体同名但是**不同的仓库**，这是资源包不是软件）：全量书源自动同步（一次同步近 4000 条）、另收录多个知名书源包、订阅源、净化规则、主题与在线朗读引擎。Git 仓库本身不能一键导入，需到配套网站 legado.aoaostar.com 用协议链接一键导入。

### 38. [Macrohard0001/lx-ikun-music-sources](https://github.com/Macrohard0001/lx-ikun-music-sources)

⭐ 2,473 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [Macrohard0001](https://github.com/Macrohard0001)（个人账号）；GitHub 仓库 ID `1007594203`；仓库创建于 2025-06-24；GitHub 许可标识未识别。

LX Music 与 IKUN Music 音源收集导航：音源导入链接、付费音源服务的价格方案与购买入口、第三方在线解析服务列表、相关音乐软件项目导航。明示仅供个人学习交流，风险自担、严禁未授权商用。

### 39. [best-fan/iptv-sources](https://github.com/best-fan/iptv-sources)

⭐ 747 ｜ 纯数据仓库

> **身份快照（2026-09-24）**：仓库所属账号 [best-fan](https://github.com/best-fan)（个人账号）；GitHub 仓库 ID `1072634970`；仓库创建于 2025-10-09；GitHub 许可标识：未标出。

每日自动更新的中国 IPTV 电视直播源仓库：每天凌晨自动采集、验证有效性、生成标准 M3U8 播放列表，直接导入播放器就能用。频道分类齐全——央视（CCTV-1 到 CCTV-17 含 4K）、37 个省级卫视、付费频道，每类都有带分辨率与流畅度标注的版本。

### 40. [lyswhut/lx-music-mobile](https://github.com/lyswhut/lx-music-mobile)

⭐ 18,377 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [lyswhut](https://github.com/lyswhut)（个人账号）；GitHub 仓库 ID `367595430`；仓库创建于 2021-05-15；GitHub 许可标识：`Apache-2.0`。

洛雪音乐移动版是基于 React Native 的音乐软件，README 当前列出的支持平台为 Android 5 及以上，并把 GitHub Releases 标为原始发布地址，其他下载渠道属于第三方转载。文档链接到更新日志、常见问题及独立同步服务；同时提醒默认设置和界面操作不以新手友好为目标，建议用户先自行调整软件设置。

### 41. [cwuom/NeriPlayer](https://github.com/cwuom/NeriPlayer)

⭐ 3,498 ｜ Kotlin

> **身份快照（2026-09-24）**：仓库所属账号 [cwuom](https://github.com/cwuom)（个人账号）；GitHub 仓库 ID `1034573460`；仓库创建于 2025-08-08；GitHub 许可标识：`GPL-3.0`。

原生 Android 音乐播放器：多源在线播放、本地曲库管理、歌词体验与自建同步服务做进同一个原生应用。歌词支持卡拉OK式逐字渲染（GLSL 着色器），带 WebDAV/WebSocket 自建同步、一起听、USB 独占输出，隐私优先无广告。

### 42. [Moriafly/SaltPlayerSource](https://github.com/Moriafly/SaltPlayerSource)

⭐ 7,377 ｜ 多平台

> **身份快照（2026-09-24）**：仓库所属账号 [Moriafly](https://github.com/Moriafly)（个人账号）；GitHub 仓库 ID `390549311`；仓库创建于 2021-07-29；GitHub 许可标识：`MIT`。

椒盐音乐（Salt Player）的官方仓库——2020 年开发至今的多平台本地音乐播放器，用户超百万；本仓库承载问题反馈（issue）与官方安卓安装包发布，与洛雪同属本地曲库播放器阵营，以本地管理见长。

### 43. [chthollyphile/folia-major](https://github.com/chthollyphile/folia-major)

⭐ 2,893 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [chthollyphile](https://github.com/chthollyphile)（个人账号）；GitHub 仓库 ID `1105953775`；仓库创建于 2025-11-28；GitHub 许可标识：`AGPL-3.0`。

以全屏沉浸式歌词播放为核心的在线音乐播放器，支持网易云、酷狗、Navidrome 和本地音乐，智能匹配歌词/封面与 AI 配色，提供多种歌词动画及 Electron/Web 多平台版本。

### 44. [ZWolken/Light-Novel-Yuedu-Source](https://github.com/ZWolken/Light-Novel-Yuedu-Source)

⭐ 441 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [ZWolken](https://github.com/ZWolken)（个人账号）；GitHub 仓库 ID `505834041`；仓库创建于 2022-06-21；GitHub 许可标识：`MIT`。

该仓库整理了供“阅读”App 导入的轻小说书源 JSON，分为日轻、国轻、日语原版及合并合集，并提供下载、网络导入和订阅说明。README 明确标注项目处于半维护周期，不保证书源有效；部分来源需登录或可能搜索异常，维护者也无法保证 issue 及时处理，因此旧书源可能无法正常使用。

## 🎮 游戏与串流 · 详解（8 个）

### 45. [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)

⭐ 150,160 ｜ C

> **身份快照（2026-09-24）**：仓库所属账号 [Genymobile](https://github.com/Genymobile)（组织账号）；GitHub 仓库 ID `111583593`；仓库创建于 2017-11-21；GitHub 许可标识：`Apache-2.0`。

安卓投屏控制的事实标准：通过 USB 或无线把手机屏幕镜像到电脑，用电脑键鼠直接控制手机。无需 root、无需在手机上装任何 App，延迟 35~70ms，支持 30~120fps。功能：音频转发、录制、息屏镜像、双向剪贴板、相机镜像、手柄支持、OTG 模式等。支持 Linux/Windows/macOS，手机需 Android 5.0+ 并开启 USB 调试。

### 46. [AlkaidLab/foundation-sunshine](https://github.com/AlkaidLab/foundation-sunshine)

⭐ 6,938 ｜ C++

> **身份快照（2026-09-24）**：仓库所属账号 [AlkaidLab](https://github.com/AlkaidLab)（组织账号）；GitHub 仓库 ID `597942169`；仓库创建于 2023-02-06；GitHub 许可标识：`GPL-3.0`。

Sunshine 增强版——自托管游戏串流的主机端（把你的电脑变成串流服务器，配合 Moonlight 客户端在别的设备上玩）。相对上游 LizardByte/Sunshine 的增强：HDR 全链路（HDR10+/HDR Vivid 动态元数据）、虚拟显示器驱动、7.1.4 环绕声、NVENC/AMF 编码优化、Tauri 2 现代控制面板（扫码配对、实时监控）、文件夹共享。专精 Windows 游戏串流体验。官方主页 alkaidlab.com。

### 47. [qiin2333/moonlight-vplus](https://github.com/qiin2333/moonlight-vplus)

⭐ 3,769 ｜ Kotlin

> **身份快照（2026-09-24）**：仓库所属账号 [qiin2333](https://github.com/qiin2333)（个人账号）；GitHub 仓库 ID `632255125`；仓库创建于 2023-04-25；GitHub 许可标识：`GPL-3.0`。

Moonlight 安卓客户端功能增强版（Moonlight V+），与原版串流协议完全兼容。相对官方版的增强：解锁 144/165Hz 高刷、最高 800Mbps 码率、HDR 校准文件自动加载；按键深度自定义（轮盘、连发、手柄瞄准、陀螺仪体感）、触控笔与多点触控；悬浮球、扫码配对、性能覆盖层（帧率/延迟/丢包实时显示）、7.1.4 空间音频。部分功能需搭配 Foundation Sunshine 主机端使用。Android 5.0+。

### 48. [DSPBluePrints/FactoryBluePrints](https://github.com/DSPBluePrints/FactoryBluePrints)

⭐ 2,440 ｜ 纯数据仓库

> **身份快照（2026-09-24）**：仓库所属账号 [DSPBluePrints](https://github.com/DSPBluePrints)（组织账号）；GitHub 仓库 ID `523449876`；仓库创建于 2022-08-10；GitHub 许可标识：未标出。

游戏《戴森球计划》的社区工厂蓝图仓库：从小马蓝图群与 CIDT 设科院贡献的蓝图合集。从 Releases 下载蓝图包放进游戏蓝图目录即可用；仓库集成自动更新脚本，更新只需双击 update.bat。蓝图默认 CC BY-NC-SA 4.0 协议。

### 49. [mcthesw/game-save-manager](https://github.com/mcthesw/game-save-manager)

⭐ 1,142 ｜ Rust

> **身份快照（2026-09-24）**：仓库所属账号 [mcthesw](https://github.com/mcthesw)（个人账号）；GitHub 仓库 ID `452249835`；仓库创建于 2022-01-26；GitHub 许可标识：`AGPL-3.0`。

图形化的开源游戏存档管理器：备份、恢复、管理各游戏的存档，支持存档描述与备注、云备份（WebDAV）、定时备份、恢复前自动删除旧档、托盘快捷操作。Rust + Tauri 技术栈，后台占用极小。官网 help.sworld.club。

### 50. [alkaidjin/Maa-Assistant-Browndust2](https://github.com/alkaidjin/Maa-Assistant-Browndust2)

⭐ 67 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [alkaidjin](https://github.com/alkaidjin)（个人账号）；GitHub 仓库 ID `1344394238`；仓库创建于 2026-08-24；GitHub 许可标识：`AGPL-3.0`。

手游《BrownDust2》（棕色尘埃 2）的日常自动化小助手，基于 MAA（明日方舟assistant 的通用自动化框架）开发：自动清日常、收资源，游戏内文字识别用 PaddleOCR 移动端模型。个人维护的小型工具，从 Releases 下载即用。

### 51. [GodRaymond233/ok-bd2](https://github.com/GodRaymond233/ok-bd2)

⭐ 103 ｜ Python

> **身份快照（2026-09-24）**：仓库所属账号 [GodRaymond233](https://github.com/GodRaymond233)（个人账号）；GitHub 仓库 ID `1282340509`；仓库创建于 2026-06-27；GitHub 许可标识：`GPL-3.0`。

基于 ok-script 的《BrownDust II》（棕色尘埃 2）自动化助手，和 Maa-Assistant-Browndust2 同属游戏日常自动化工具。

### 52. [MadestSamurai/bd2-infinite-gacha](https://github.com/MadestSamurai/bd2-infinite-gacha)

⭐ 10 ｜ C#

> **身份快照（2026-09-24）**：仓库所属账号 [MadestSamurai](https://github.com/MadestSamurai)（个人账号）；GitHub 仓库 ID `1375308124`；仓库创建于 2026-09-18；GitHub 许可标识：`MIT`。

适用于 BrownDust II Windows 客户端的独立无限抽抽乐助手，读取卡池与账号进度，按 A/B 目标和停止条件刷新、跳过动画，命中后保留结果供确认。

## 🛠️ 自托管与效率工具 · 详解（13 个）

### 53. [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

⭐ 146,258 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [clash-verge-rev](https://github.com/clash-verge-rev)（组织账号）；GitHub 仓库 ID `721767116`；仓库创建于 2023-11-21；GitHub 许可标识：`GPL-3.0`。

基于 Tauri 的 Clash Meta（mihomo）图形代理客户端，Windows/macOS/Linux 全平台，是原 Clash Verge 的社区延续版。分正式版（Stable，日常使用）与滚动构建版（AutoBuild，尝鲜用）。README 自带推广板块为第三方机场广告，与项目无关，安装请只走 GitHub Releases。官方主页 clashverge.dev。

### 54. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)

⭐ 46,455 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [siyuan-note](https://github.com/siyuan-note)（组织账号）；GitHub 仓库 ID `291438522`；仓库创建于 2020-08-30；GitHub 许可标识：`AGPL-3.0`。

思源笔记：隐私优先、块级引用的开源笔记系统，可自托管成个人知识库。核心特色：内容块级引用与双向链接、Markdown 所见即所得、SQL 查询嵌入、数学公式/流程图/甘特图/五线谱、网页剪藏、PDF 批注；支持百万字大文档。大多数功能免费（含商用）。部署方式齐全：安装包、Docker、NAS 应用市场均可。官方主页 b3log.org/siyuan。

### 55. [waydabber/BetterDisplay](https://github.com/waydabber/BetterDisplay)

⭐ 33,746 ｜ —

> **身份快照（2026-09-24）**：仓库所属账号 [waydabber](https://github.com/waydabber)（个人账号）；GitHub 仓库 ID `420628737`；仓库创建于 2021-10-24；GitHub 许可标识：未标出。

Mac 显示器深度管理工具（BetterDisplay Pro）：把显示器变成完全可缩放屏幕、DDC 亮度色彩控制（兼容显示器可超 100% 亮度提亮、也能完全调暗至黑）、创建虚拟屏幕、显示器画中画、热断开重连、多屏亮度归一同步、HDR 与高刷虚拟屏。版本线覆盖 macOS Mojave 至最新系统。官方主页 betterdisplay.pro。

### 56. [jiangrui1994/CloudSaver](https://github.com/jiangrui1994/CloudSaver)

⭐ 9,317 ｜ Vue

> **身份快照（2026-09-24）**：仓库所属账号 [jiangrui1994](https://github.com/jiangrui1994)（个人账号）；GitHub 仓库 ID `904513119`；仓库创建于 2024-12-17；GitHub 许可标识：`MIT`。

网盘资源搜索与一键转存的自部署工具（Vue 3 + Express，Docker 一键部署）：多资源订阅源关键词搜索、豆瓣热门榜单、搜索结果一键转存至 115/夸克/天翼/123 云盘，带多用户权限系统。⚠️ 项目涉及网盘 Cookie 等敏感凭据，官方强烈要求**私有化部署**、不要用任何第三方在线站点；开源仓库停留在 V0.2.5，新版本仅通过 Docker 镜像提供。

### 57. [Nevcairiel/LAVFilters](https://github.com/Nevcairiel/LAVFilters)

⭐ 9,154 ｜ C++

> **身份快照（2026-09-24）**：仓库所属账号 [Nevcairiel](https://github.com/Nevcairiel)（个人账号）；GitHub 仓库 ID `10289758`；仓库创建于 2013-05-25；GitHub 许可标识：`GPL-2.0`。

基于 ffmpeg 的 Windows DirectShow 解码滤镜套装：装上之后各类 DirectShow 播放器几乎能播所有格式（MKV、AVI、MP4/MOV、TS/M2TS、FLV、蓝光原盘等）。自动流选择策略智能（视频选最高画质、音频按首选语言与声道数排序、字幕四种模式）。是 Windows 影音播放器生态的底层积木。

### 58. [floccusaddon/floccus](https://github.com/floccusaddon/floccus)

⭐ 8,477 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [floccusaddon](https://github.com/floccusaddon)（组织账号）；GitHub 仓库 ID `60434915`；仓库创建于 2016-06-04；GitHub 许可标识：`MPL-2.0`。

跨浏览器跨设备的私密书签同步工具：同步的是浏览器**原生书签**（不导入第三方体系），数据走你自己的服务器——支持 Nextcloud、Linkwarden、Google Drive、Dropbox、任意 Git 服务器或 WebDAV。覆盖所有支持扩展的浏览器（Firefox/Chrome/Edge/Brave/Vivaldi 等），移动端有独立 App 补足。可建多个同步配置档，方向（单向/双向）、间隔、文件夹均可控。官方主页 floccus.org。

### 59. [Ponphil/LitePan](https://github.com/Ponphil/LitePan)

⭐ 1,260 ｜ Go

> **身份快照（2026-09-24）**：仓库所属账号 [Ponphil](https://github.com/Ponphil)（个人账号）；GitHub 仓库 ID `1246231570`；仓库创建于 2026-05-22；GitHub 许可标识未识别。

多网盘聚合挂载与媒体库整理工具（Go 版重写中，开发阶段）：多网盘多账号统一管理、跨盘秒传、生成 .strm 直连对接 Emby/Jellyfin 并自动刮削（nfo/海报）、TMDB 识别目录整理——整理、STRM、刮削、刷库可串联自动联动。支持 WebDAV 与 FUSE 本地挂载、302 直链、离线下载。Docker Compose 部署（端口 5211）。⚠️ 官方警告：Docker 勿用 latest 镜像（那是旧 Python 版），应使用 Beta 标签。官方主页 litepan.top。

### 60. [MAXeaglet/commandcode-proxy](https://github.com/MAXeaglet/commandcode-proxy)

⭐ 668 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [MAXeaglet](https://github.com/MAXeaglet)（个人账号）；GitHub 仓库 ID `1261552113`；仓库创建于 2026-06-06；GitHub 许可标识：`MIT`。

单文件、零外部依赖的 Command Code 反向代理，将 API 转换为 OpenAI/Anthropic 兼容端点，支持 Responses/Chat、流式、工具调用、多模态、重试与隐私日志。

### 61. [Patrick-mufeng/cmdgo-bridge](https://github.com/Patrick-mufeng/cmdgo-bridge)

⭐ 14 ｜ TypeScript

> **身份快照（2026-09-24）**：仓库所属账号 [Patrick-mufeng](https://github.com/Patrick-mufeng)（个人账号）；GitHub 仓库 ID `1353617210`；仓库创建于 2026-09-01；GitHub 许可标识：`MIT`。

把 Command Code Go 套餐接入任意 Agent 工具的本地 OpenAI 兼容桥，含 OAuth 登录、请求级多账号池、官方模型目录同步与 Web 控制台，Node ≥20。

### 62. [linguo2625469/workbuddy2api-panel](https://github.com/linguo2625469/workbuddy2api-panel)

⭐ 660 ｜ Go

> **身份快照（2026-09-24）**：仓库所属账号 [linguo2625469](https://github.com/linguo2625469)（个人账号）；GitHub 仓库 ID `1366969284`；仓库创建于 2026-09-12；GitHub 许可标识：`MIT`。

基于 Sliverkiss/workbuddy2api 的增强分支，把腾讯 CodeBuddy 账号包装为 OpenAI 兼容多账号网关，增加 Web 面板、OAuth、账号池治理、定时任务与成长任务。

### 63. [Sliverkiss/workbuddy2api](https://github.com/Sliverkiss/workbuddy2api)

⭐ 1,428 ｜ Go

> **身份记录**：2026-09-22 清单记载的仓库所属账号为 `Sliverkiss`；仓库 ID、创建日期和许可标识未取得。2026-09-24 核验时，原仓库地址返回 404；原因未确认，以下项目说明保留此前记录。

非官方的 CodeBuddy OpenAI 兼容上游网关，通过 OAuth 获取凭证，支持 token 刷新、账号池调度、冷却/熔断、会话粘性和流式响应。

### 64. [MetaCubeX/ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid)

⭐ 46,527 ｜ Kotlin

> **身份快照（2026-09-24）**：仓库所属账号 [MetaCubeX](https://github.com/MetaCubeX)（组织账号）；GitHub 仓库 ID `500719319`；仓库创建于 2022-06-07；GitHub 许可标识：`GPL-3.0`。

这是 Clash.Meta 的 Android 图形界面客户端，README 标注 Android 5.0+（推荐 7.0+）及四种架构：armeabi-v7a、arm64-v8a、x86、x86_64。文档列出内核、SDK、CMake 等构建依赖，并说明服务启停和 clash://、clashmeta:// 配置导入；自行构建需配置 SDK 与签名。

### 65. [Javis603/token-monitor](https://github.com/Javis603/token-monitor)

⭐ 2,275 ｜ JavaScript

> **身份快照（2026-09-24）**：仓库所属账号 [Javis603](https://github.com/Javis603)（个人账号）；GitHub 仓库 ID `1243377527`；仓库创建于 2026-05-19；GitHub 许可标识：`MIT`。

本地优先的桌面小组件：追踪多款 AI 编程工具（如 Claude Code、Codex、Cursor、OpenCode 和 OpenClaw）的 token 用量、花费与限额，并支持多设备同步。

## 维护约定

- **一览表**（本文件开头）：项目名称即链接、星数、一句话简介；整库刷新时星数同步更新
- **详解条目**（本文件下方）：新收藏项目入列时在对应分类末尾追加；功能描述以官方 README 为准，一次写清、长期不随星数变动；星数随整库刷新同步
- **身份快照**：新增或整库核验时记录查询日期、当时的仓库所属账号、GitHub 仓库 ID、创建日期与许可标识；“所属账号”不冒充最初创建者。链接失效时保留原说明，注明最后核验结果及无法确认的原因；README 是文字记录，不等于源码备份
- **单文件就地换版**：本 README 即清单本体，整库刷新就地进行（星数查询值换日期），后续变更在新的提交记录中追踪；每个条目含项目名、仓库链接、一句话定位；分类互斥不重复

