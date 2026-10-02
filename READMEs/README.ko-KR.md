<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>모든 Grok Bot이 미리 준비된 결정적 경로로 일하고 토큰 낭비를 멈추게 하는 영구 skill.</strong><br />
  <em>명령어는 그대로 복사할 수 있도록 영어로 둡니다.</em>
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
  <img src="../assets/banner.png" alt="추상적인 비용 사다리: 왼쪽은 저렴한 스크립트 단계, 오른쪽은 비싼 computer use" width="860" />
</p>

---

## 요약

`grokbot-economy`는 Grok Bot을 위한 skill입니다. Grok Bot은 shell, 파일 읽기, MCP 커넥터, 플러그인, box 브라우저, `browse` CLI, 스크린샷 기반 computer use 서브에이전트를 갖춘 LLM 데스크톱 어시스턴트입니다. 이 skill은 bot에게 **계획, 검토, 예외 처리는 LLM으로, 실행은 코드로** 하라고 지시합니다. 반복 작업은 스크립트가 되고, 배치는 CSV/JSON으로 처리하며, 브라우저는 최후의 수단이고, 유료 크레딧은 소유자의 승인이 필요하며, bot 간 메시지는 짧게 유지합니다.

skill 자체(`SKILL.md`)와 저장소의 나머지 파일은 영어로 작성되어 있습니다. 이 README만 15개 언어로 번역됩니다.

## 설치

1. **가장 쉬운 방법:** Grok Bot 채팅에서 skill로 저장해 달라고 요청하세요:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **수동:** `SKILL.md` 전체(frontmatter 포함)를 bot의 skill 편집기에 복사하거나, 채팅에 붙여 넣고 skill로 저장해 달라고 요청하세요.
3. **skill 폴더를 읽는 에이전트** (Cursor/Claude 방식):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

그다음 `/grokbot-economy`로 호출하거나 루틴에서 언급하세요. 설명 덕분에 bot은 모든 작업을 시작할 때, 브라우저를 열기 전, 작업을 반복하기 전, 다른 bot에게 메시지를 보낼 때 이 skill을 불러옵니다.

## 원칙

| # | 경로 | 용도 |
|---|---|---|
| 1 | Script/CLI | 이미 스크립트가 있는 모든 작업 |
| 2 | MCP | Drive, Gmail, GitHub, Calendar 등 |
| 3 | Plugin/skill | 미리 만들어진 서드파티 레시피 |
| 4 | API | 커넥터가 없는 서비스 |
| 5 | `browse` CLI (text/DOM) | API가 없는 사이트(텍스트로 읽기) |
| 6 | Computer use (screenshots) | 로그인(2FA는 사람이 완료), 예외, API나 스크립트 가능한 DOM이 없는 UI에만. captcha/안티봇 차단 → 멈추고 사람에게 넘기거나 공식 API 사용 |

- **LLM은 계획하고 코드는 실행한다.** 두 번 나온 작업은 `--dry-run`, 멱등성, 테스트를 갖춘 스크립트로 만든다.
- **브라우저 전 체크리스트:** 스크립트? 커넥터? 플러그인? API? `browse`로 텍스트 기반 처리가 가능한가?
- **배치는 CSV/JSON + 스크립트로**, UI에서 필드 하나씩 입력하지 않는다. 실패만 보고한다.
- **절약형 읽기:** `rg` + offset/limit 읽기, 파일 전체 덤프 금지, 다시 읽기 금지, sleep/폴링 루프 금지.
- **비용 가드레일:** 소유자의 명시적 승인 없이 유료 크레딧(할당량 초과 TTS, 클리핑 크레딧, 광고)을 쓰지 않는다. 할당량 잠금 파일을 지킨다.
- **안전한 파일 편집:** dry-run, 사본에서 테스트, 백업 + 원자적 교체, 잠금, 작은 diff.
- **Instagram/WhatsApp:** 공식 API 우선. 없으면 사람 속도로, 사람이 승인한 신중한 전송만. 안티봇 우회 도구 금지. 첫 경고에서 멈춘다.
- **bot 간 메시지:** 짧게, 파일 경로를 가리키고, 항목을 묶고, "확인"만 담은 메시지는 보내지 않는다.
- **적절한 크기의 모델:** 기계적인 작업은 낮은 effort, 높은 effort는 판단이 필요할 때만. 긴 작업은 백그라운드로.

## 저장소 구성

| 파일 | 내용 |
|---|---|
| [`SKILL.md`](../SKILL.md) | skill 본문: 비용 사다리, 체크리스트, 브라우저 도구 선택지, 안티패턴, 의사결정 흐름도, 유지보수 규칙 |
| [`CHANGELOG.md`](../CHANGELOG.md) | skill의 모든 변경 사항(이유와 예상 절감량 포함) |
| [`examples/flows.md`](../examples/flows.md) | 구체적인 흐름: 스프레드시트, Drive, 조정 보드, 영상, 배치, 전송 |
| [`checklists/`](../checklists/) | 브라우저 전, 새 스크립트, Instagram/WhatsApp 전송 |
| [`scripts/token_log.py`](../scripts/token_log.py) | 작업별 토큰/비용 추가 전용 로거(stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | 지표 템플릿(CSV 헤더 + 예시) |
| [`tests/`](../tests/) | 로거 단위 테스트 |
| [`assets/banner.png`](../assets/banner.png) | README 배너 |

## 측정하기

작업별 토큰/비용과 사용한 경로를 기록하세요. 요약에서 `browse`나 `computer-use`가 많다면 스크립트가 빠져 있다는 뜻입니다.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## 기여하기

- 더 저렴한 경로(새 스크립트, 커넥터, API, 플러그인, CLI 플래그)를 찾았나요? `SKILL.md`를 수정하는 PR을 열고 **동시에** `CHANGELOG.md`에 한 줄(날짜, 내용, 이유, 예상 절감량)을 추가하세요. 모든 bot에 적용되는 영구 규칙입니다.
- `SKILL.md`는 짧게(약 250줄 미만), 명령형으로, 영어로 유지하세요.
- **공개 저장소:** 토큰, 키, 이메일, 전화번호, 고객 이름, 파일 ID, 호스트명, 내부 URL을 넣지 마세요. `<DRIVE_FILE_ID>` 같은 플레이스홀더를 사용하세요.
- PR을 열기 전에 selftest와 단위 테스트를 실행하세요.

## 라이선스

MIT. [LICENSE](../LICENSE)를 참고하세요.
