<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>すべての Grok Bot に既製の決定的な手順で作業させ、トークンの浪費をやめさせる恒久的な skill。</strong><br />
  <em>コマンドは正確にコピーできるよう英語のままにしています。</em>
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
  <img src="../assets/banner.png" alt="抽象的なコストの階段：左は安価なスクリプト処理、右は高価な computer use" width="860" />
</p>

---

## 概要

`grokbot-economy` は Grok Bot 向けの skill です。Grok Bot は shell、ファイル読み取り、MCP コネクタ、プラグイン、box 内ブラウザ、`browse` CLI、スクリーンショット駆動の computer use サブエージェントを備えた LLM デスクトップアシスタントです。この skill は bot に **計画・レビュー・例外処理は LLM で、実行はコードで** 行うよう指示します。繰り返す作業はスクリプト化し、バッチは CSV/JSON で処理し、ブラウザは最後の手段とし、有料クレジットはオーナーの承認を必須にし、bot 間のメッセージは短く保ちます。

skill 本体（`SKILL.md`）とリポジトリのその他のファイルは英語です。翻訳されているのはこの README だけで、英語の原文に加えて 14 の翻訳があります。

## インストール

1. **最も簡単な方法：** Grok Bot のチャットで skill として保存するよう頼みます：

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **手動：** `SKILL.md` 全体（frontmatter を含む）を bot の skill エディタにコピーするか、チャットに貼り付けて skill として保存するよう頼みます。
3. **skill フォルダを読むエージェント**（Cursor/Claude 形式）：

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

その後は `/grokbot-economy` で呼び出すか、ルーティンで言及します。説明文により、bot はあらゆるタスクの開始時、ブラウザを開く前、タスクを繰り返す前、他の bot にメッセージを送るときにこの skill を読み込みます。

## 原則

| # | 手段 | 用途 |
|---|---|---|
| 1 | Script/CLI | すでにスクリプトがあるものすべて |
| 2 | MCP | Drive、Gmail、GitHub、Calendar など |
| 3 | Plugin/skill | 既製のサードパーティ製レシピ |
| 4 | API | コネクタのないサービス |
| 5 | `browse` CLI (text/DOM) | API のないサイト（テキストとして読む） |
| 6 | Computer use (screenshots) | サインイン（2FA は人間が完了）、例外、API やスクリプト可能な DOM のない UI のみ。captcha/アンチボットのブロック → 停止して人間に引き継ぐか、公式 API を使う |

- **LLM が計画し、コードが実行する。** 2 回出てきたタスクは `--dry-run`、冪等性、テスト付きのスクリプトにする。
- **ブラウザ前チェックリスト：** スクリプトは？コネクタは？プラグインは？API は？`browse` でテキストとして処理できるか？
- **バッチは CSV/JSON + スクリプトで。** UI で 1 項目ずつ入力しない。失敗だけを報告する。
- **節約した読み方：** `rg` + offset/limit での読み取り。ファイル全体をダンプしない、再読しない、sleep/ポーリングのループをしない。
- **お金のガードレール：** オーナーの明示的な承認なしに有料クレジット（クォータ超過の TTS、クリッピングクレジット、広告）を使わない。クォータのロックファイルを守る。
- **安全なファイル編集：** dry-run、コピーでのテスト、バックアップ + アトミックな置き換え、ロック、小さな差分。
- **Instagram/WhatsApp：** まず公式 API。なければ人間のペースで、人間が承認した控えめな送信のみ。アンチボット回避ツールは使わない。最初の警告で停止する。
- **bot 間メッセージ：** 短く、ファイルパスを示し、項目をまとめ、「了解」だけのメッセージは送らない。
- **適切なサイズのモデル：** 機械的な作業は低い effort、高い effort は判断のときだけ。長いジョブはバックグラウンドで。

## リポジトリの内容

| ファイル | 内容 |
|---|---|
| [`SKILL.md`](../SKILL.md) | skill 本体：コストの階段、チェックリスト、ブラウザツールの選択肢、アンチパターン、判断フローチャート、メンテナンスルール |
| [`CHANGELOG.md`](../CHANGELOG.md) | skill へのすべての変更（理由と推定節約量つき） |
| [`examples/flows.md`](../examples/flows.md) | 具体的なフロー：スプレッドシート、Drive、調整ボード、動画、バッチ、送信 |
| [`checklists/`](../checklists/) | ブラウザ前、新しいスクリプト、Instagram/WhatsApp 送信 |
| [`scripts/token_log.py`](../scripts/token_log.py) | タスクごとのトークン/コストの追記専用ロガー（stdlib、`--selftest`） |
| [`templates/token-log.csv`](../templates/token-log.csv) | メトリクスのテンプレート（CSV ヘッダー + 例） |
| [`tests/`](../tests/) | ロガーの単体テスト |
| [`assets/banner.png`](../assets/banner.png) | README のバナー |

## 計測する

タスクごとにトークン/コストと使った手段を記録します。集計で `browse` や `computer-use` が多い場合は、スクリプトが不足しています。

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## コントリビュート

- もっと安い手段（新しいスクリプト、コネクタ、API、プラグイン、CLI フラグ）を見つけたら、`SKILL.md` を変更する PR を開き、**さらに** `CHANGELOG.md` に 1 行（日付、内容、理由、推定節約量）を追加してください。これはすべての bot に対する恒久的なルールです。
- `SKILL.md` は短く（約 250 行未満）、命令形で、英語で保ってください。
- **公開リポジトリ：** トークン、キー、メールアドレス、電話番号、顧客名、ファイル ID、ホスト名、内部 URL は書かないこと。`<DRIVE_FILE_ID>` のようなプレースホルダーを使ってください。
- PR を開く前に selftest と単体テストを実行してください。

## ライセンス

MIT。[LICENSE](../LICENSE) を参照してください。
