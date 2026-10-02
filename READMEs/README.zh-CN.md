<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>一个永久性的 skill，让每个 Grok Bot 都通过现成的确定性路径工作，不再浪费 token。</strong><br />
  <em>命令保留英文，便于原样复制。</em>
</p>

<p align="center">
<a href="https://github.com/wesleysimplicio/grokbot-economy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/wesleysimplicio/grokbot-economy?style=flat-square" /></a>
<img alt="Grok Bot skill" src="https://img.shields.io/badge/Grok%20Bot-skill-2fe6a0?style=flat-square" />
<img alt="SKILL.md English" src="https://img.shields.io/badge/SKILL.md-English-0ea5e9?style=flat-square" />
<a href="../LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" /></a>
</p>

<p align="center">
<a href="../README.md">English</a> | <a href="README.pt-BR.md">Português</a> | <a href="README.es-ES.md">Español</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.ko-KR.md">한국어</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.it-IT.md">Italiano</a> | <a href="README.fr-FR.md">Français</a> | <a href="README.ru-RU.md">Русский</a> | <a href="README.pl-PL.md">Polski</a> | <a href="README.hi-IN.md">हिन्दी</a> | <a href="README.ar-SA.md">العربية</a> | <a href="README.he-IL.md">עברית</a> | <a href="README.ms-MY.md">Bahasa Melayu</a> | <a href="README.id-ID.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img src="../assets/banner.png" alt="抽象的成本阶梯：左边是便宜的脚本步骤，右边是昂贵的 computer use" width="860" />
</p>

---

## 简介

`grokbot-economy` 是为 Grok Bot 编写的 skill。Grok Bot 是一个 LLM 桌面助手，具备 shell、文件读取、MCP 连接器、插件、box 浏览器、`browse` CLI，以及基于截图的 computer use 子代理。这个 skill 要求 bot **用 LLM 来规划、审查和处理异常，用代码来执行**：重复的工作写成脚本，批量任务通过 CSV/JSON 处理，浏览器是最后手段，付费额度必须经所有者批准，bot 之间的消息保持简短。

skill 本身（`SKILL.md`）和仓库的其余内容均为英文。只有本 README 翻译成 15 种语言。

## 安装

1. **最简单：** 在 Grok Bot 聊天中让它保存为 skill：

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **手动：** 把整个 `SKILL.md`（包括 frontmatter）复制到 bot 的 skill 编辑器，或粘贴到聊天中并让它保存为 skill。
3. **读取 skill 文件夹的代理**（Cursor/Claude 风格）：

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

之后用 `/grokbot-economy` 调用，或在例行任务中提及。它的描述会让 bot 在任何任务开始时、打开浏览器之前、重复任务之前以及给其他 bot 发消息时加载它。

## 原则

| # | 路径 | 适用于 |
|---|---|---|
| 1 | Script/CLI | 已经有脚本的一切任务 |
| 2 | MCP | Drive、Gmail、GitHub、Calendar 等 |
| 3 | Plugin/skill | 现成的第三方方案 |
| 4 | API | 没有连接器的服务 |
| 5 | `browse` CLI (text/DOM) | 没有 API 的网站（按文本读取） |
| 6 | Computer use (screenshots) | 仅限登录（由人完成 2FA）、异常情况、没有 API 或可脚本化 DOM 的界面；遇到验证码/反机器人拦截 → 停止并交给人处理，或使用官方 API |

- **LLM 规划，代码执行。** 出现两次的任务就写成带 `--dry-run`、幂等性和测试的脚本。
- **打开浏览器前的检查清单：** 有脚本吗？有连接器吗？有插件吗？有 API 吗？`browse` 能按文本完成吗？
- **批量任务用 CSV/JSON + 脚本**，绝不在 UI 里逐个字段填写；只报告失败项。
- **节省地读取：** 用 `rg` 加 offset/limit 读取，不整份输出文件，不重复读取，不写 sleep/轮询循环。
- **费用护栏：** 未经所有者明确同意，绝不使用付费额度（超出配额的 TTS、剪辑额度、广告）；遵守配额锁文件。
- **安全地修改文件：** dry-run、在副本上测试、备份 + 原子替换、文件锁、小改动。
- **Instagram/WhatsApp：** 优先使用官方 API；否则只做保守的、按人类节奏、经人工批准的发送；不使用任何反机器人规避工具；出现第一个警告就停止。
- **bot 之间的消息：** 简短，指向文件路径，合并事项，不发只有“收到”的消息。
- **合适规模的模型：** 机械性工作用低 effort，只有需要判断时才用高 effort；长任务放到后台。

## 仓库内容

| 文件 | 说明 |
|---|---|
| [`SKILL.md`](../SKILL.md) | skill 本体：成本阶梯、检查清单、浏览器工具选择、反模式、决策流程图、维护规则 |
| [`CHANGELOG.md`](../CHANGELOG.md) | skill 的每次变更，附原因和预计节省 |
| [`examples/flows.md`](../examples/flows.md) | 具体流程：电子表格、Drive、协作看板、视频、批量、发送 |
| [`checklists/`](../checklists/) | 打开浏览器前、新脚本、Instagram/WhatsApp 发送 |
| [`scripts/token_log.py`](../scripts/token_log.py) | 按任务记录 token/成本的只追加日志工具（stdlib，`--selftest`） |
| [`templates/token-log.csv`](../templates/token-log.csv) | 指标模板（CSV 表头 + 示例） |
| [`tests/`](../tests/) | 日志工具的单元测试 |
| [`assets/banner.png`](../assets/banner.png) | README 横幅 |

## 度量

按任务记录 token/成本和所用路径。如果汇总中 `browse` 或 `computer-use` 占多数，说明缺少脚本。

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## 贡献

- 发现了更便宜的路径（新脚本、连接器、API、插件、CLI 参数）？提交修改 `SKILL.md` 的 PR，**并**在 `CHANGELOG.md` 中加一行（日期、内容、原因、预计节省）。这是对所有 bot 的永久规则。
- 保持 `SKILL.md` 简短（少于约 250 行）、使用祈使句、使用英文。
- **公开仓库：** 不得包含 token、密钥、邮箱、电话号码、客户名称、文件 ID、主机名或内部 URL。使用 `<DRIVE_FILE_ID>` 之类的占位符。
- 提交 PR 前运行 selftest 和单元测试。

## 许可证

MIT。参见 [LICENSE](../LICENSE)。
