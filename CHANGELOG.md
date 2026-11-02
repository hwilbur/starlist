# 维护记录

[返回项目手册](README.md)

## 2026-11-02 · 文档结构整理

- 分类表的 78 个“查看介绍”跳转保留，原项目链接不变。
- README 聚焦项目资料；历次整理过程、清单调整及维护约定移至本文件。
- 所有项目介绍、身份与功能证据、日期、来源、星数、分类和稳定锚点保持不变。
- `scripts/check_readme.py` 是维护用的离线一致性检查，不是项目资料或运行依赖；阅读手册无需运行它。本轮保留原脚本，使用说明见下方维护约定。

## 原有整理记录

**后续维护按此模板**：每个新增项目填写仓库链接、星数和一句话定位；详解分别记录星数快照日期、身份核验日期与功能核验日期。依据官方 README 写清用途、主要功能、必要配套和限制，并附含完整提交 SHA 的固定来源链接；README 不足时补官方文档或源码。所属账号不当作最初作者，未核实内容明确标注；链接失效时保留最近说明与有日期的检查结果。个人使用感受仅在实际体验后记录；公开手册只收录第三方项目信息。

- **星标与清单核对（2026-11-02，UTC+8）**：本次逐页读取 Stars 三页，共 76 个唯一仓库。四个主清单已回读核对：AI 39、阅读与影音 17、游戏与串流 9、自托管与效率工具 11，重复 0 项、漏分 0 项；与本手册当前分类逐项对应。
- **本轮增量**：补入 CloudDrive2 相关仓库 cloud-fs/cloud-fs.github.io；su-kaka/gcli2api 更名为 su-kaka/agy2api，稳定仓库 ID 不变，不计为新增项目；aimod-cc/Agent2API 使用当前大小写。corrinehu/dsh-workbuddy-connect 本次已不在星标中，原址返回 404，转入历史保留；连同原有 Sliverkiss/workbuddy2api，历史条目共 2 项。
- **星数快照（2026-11-02）**：76 个当前项目使用本次 GitHub Stars 网页快照，表与详解同步。星数随时间变化，网页可能有缓存；历史条目保留各自原有星数和日期。
- **身份与功能核验**：本轮补充 CloudDrive2 相关仓库的身份与用途证据，核对 agy2api 更名和功能变化、bd2-infinite-gacha 归档迁移状态，以及 Maa-Assistant-Browndust2 的 PC 端定位；其余条目沿用原有身份与功能记录，刷新星数不改变旧证据日期。
- **验证范围**：当前仓库收录、分类、星数、表与详解一致性及上述差异项的官方资料。安装、部署、账号、模型及设备兼容性未实测。

<details>
<summary>此前维护记录：2026-10-14</summary>

- **星标与清单核对（2026-10-14，UTC+8）**：逐页读取公开 Stars 三页，共 76 个唯一仓库；四个 GitHub Lists 原合计 73 项，重复 0 项、漏分 3 项。整理后为 AI 40、阅读与影音 17、游戏与串流 9、自托管与效率工具 10，各项目只进入一个主清单。
- **整理后回读核对（2026-10-14）**：逐页回读四个清单，共 76 个唯一仓库，重复 0 项、漏分 0 项，归属与本手册四个当前分类一致；四个清单均已补充分类说明。
- **本轮增量**：相较 2026-09-30 手册补入 8 项：gcli2api、dsh-market、agent2api、ViVe、WorkBuddy-Daily、LangGPT、BD2-L2D-Viewer、RikkaHub。原有 Sliverkiss/workbuddy2api 在当前 Stars 中缺席，2026-10-14 原址 API 仍返回 404，移至历史保留。
- **星数快照（2026-10-14）**：76 个当前项目取自本次 GitHub Stars 网页，表与详解同步；网页可能存在缓存，数值随时间变化。历史条目仍使用 2026-09-22 的 1,428 星。
- **身份与功能核验**：新增 8 项核对于 2026-10-14，固定版本来源附在各条目。其余 68 个当前项目沿用条目原有的身份、功能说明与核验日期；无单独功能日期的内容仍为此前记录，分类与星数更新不改变其证据日期。
- **验证范围**：本轮验证仓库收录、分类、星数和手册内部一致性；新增功能说明依据项目官方文档。安装、部署、账号、模型及设备兼容性均未实测。

</details>

## 分类规则与本次排查

分类结论：保留四个主清单，并补充用途细分。主要问题是把部署方式、项目用途和关联平台混作分类依据；以主要用途决定主清单，平台及部署方式作为说明信息。

- **AI**：AI 智能体、客户端、知识库、技能、提示词、模型接入及用量工具；自托管 AI 仍归 AI。
- **阅读与影音**：阅读器、书源、音乐、音源、视频、直播和播放解码；通用网盘与资源导航归通用工具。
- **游戏与串流**：游戏专用助手、蓝图、存档、角色动画、视觉小说翻译及游戏串流；通用设备显示与控制归通用工具。
- **自托管与效率工具**：通用笔记、书签、资源导航、网盘、网络代理、显示和系统工具。
- **历史保留**：当前星标中缺席的历史项目，保留旧说明、旧星数与日期，并分别记录访问结果；不把取消星标等同于仓库失效。

<details>
<summary>2026-10-14 清单调整明细：3 项补分，9 项迁移</summary>

- [su-kaka/gcli2api](https://github.com/su-kaka/gcli2api)：未分清单 → AI。主要用途是 AI 模型协议转换与网关。
- [thebookisclosed/ViVe](https://github.com/thebookisclosed/ViVe)：未分清单 → 自托管与效率工具。主要用途是 Windows 系统功能控制。
- [Jelosus2/BD2-L2D-Viewer](https://github.com/Jelosus2/BD2-L2D-Viewer)：未分清单 → 游戏与串流。主要用途是游戏角色动画查看。
- [N0VI028/JS-Slash-Runner](https://github.com/N0VI028/JS-Slash-Runner)：游戏与串流 → AI。服务 SillyTavern 的 LLM 角色交互与脚本扩展。
- [HIllya51/LunaTranslator](https://github.com/HIllya51/LunaTranslator)：自托管与效率工具 → 游戏与串流。主要面向视觉小说文本提取、翻译与学习。
- [MAXeaglet/commandcode-proxy](https://github.com/MAXeaglet/commandcode-proxy)：自托管与效率工具 → AI。服务 AI 模型的 API 兼容网关。
- [Patrick-mufeng/cmdgo-bridge](https://github.com/Patrick-mufeng/cmdgo-bridge)：自托管与效率工具 → AI。服务 AI 模型的 API 兼容网关。
- [linguo2625469/workbuddy2api-panel](https://github.com/linguo2625469/workbuddy2api-panel)：自托管与效率工具 → AI。服务 AI 模型的 API 兼容网关。
- [Javis603/token-monitor](https://github.com/Javis603/token-monitor)：自托管与效率工具 → AI。主要追踪 AI 工具用量、费用与限额。
- [Nevcairiel/LAVFilters](https://github.com/Nevcairiel/LAVFilters)：自托管与效率工具 → 阅读与影音。主要为影音播放器提供分离与解码。
- [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)：游戏与串流 → 自托管与效率工具。通用 Android 显示与控制，游戏只是使用场景之一。
- [AZeC4/TelegramGroup](https://github.com/AZeC4/TelegramGroup)：阅读与影音 → 自托管与效率工具。通用群组、频道和机器人导航。

同一用途的多个项目保留独立条目，例如 DSH 的两款 WorkBuddy 接入插件，以及两款 WorkBuddy 签到脚本；功能相近不等于重复仓库。当前清单没有跨清单重复项，以上调整沿用全部 76 个星标。

</details>

## 维护约定

- **分类与收录**：当前项目只进入一个主清单，以主要用途分类；AI 专用网关、插件与用量工具归 AI，部署方式与平台仅作为说明。当前四清单的集合应覆盖公开 Stars，交集应为空；当前星标中缺席的项目单独放入历史保留，并注明访问结果；取消星标本身不代表项目失效。
- **一览表**：项目名称即仓库链接、星数、一句话定位；与详解对应，同步关键维护状态或使用限制，历史提醒保留日期。刷新星数时两处同时更新，并明确该批快照范围。
- **详解条目**：新增项目加入对应用途细分；功能核验时更新用途、功能、必要配套与限制，并记录核验日期和固定官方来源。星数、身份、功能分开记录，局部功能更新保留其他条目的旧证据日期。
- **身份快照**：新增或整库核验时记录查询日期、当时的仓库所属账号、GitHub 仓库 ID、创建日期与许可标识；“所属账号”不冒充最初创建者。README 徽章、API 标识和许可文件出现差异时分别记录。链接失效时保留原说明，注明最后检查日期和无法确认的原因；README 是文字记录，不等于源码备份。
- **单 README 就地维护**：本 README 是唯一清单本体；四个当前分类互斥，历史保留独立统计，检查脚本不另存项目数据。更新在一个聚焦提交中追踪，原版本可从提交历史恢复。
- **一致性检查**：Python 3 标准库脚本 [scripts/check_readme.py](scripts/check_readme.py) 离线核对分类数量、唯一仓库链接、表与详解对应及顺序、连续编号和两处星数。运行 `python -X utf8 scripts/check_readme.py`；运行 `python -X utf8 scripts/check_readme.py --self-test` 验证缺项、错误星数、重复链接、跳号等内存故障样例。脚本不联网、不修改手册；公开 Stars 的覆盖、GitHub Lists 当前归属及来源真实性另需在线核对。
