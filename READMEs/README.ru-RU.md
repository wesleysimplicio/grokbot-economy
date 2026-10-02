<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Постоянная skill, которая заставляет каждого Grok Bot работать по готовым детерминированным путям и перестать сжигать токены.</strong><br />
  <em>Команды остаются на английском, чтобы их можно было скопировать без изменений.</em>
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
  <img src="../assets/banner.png" alt="Абстрактная лестница затрат: дешёвые шаги через скрипты слева, дорогой computer use справа" width="860" />
</p>

---

## Коротко

`grokbot-economy` — это skill для Grok Bot, настольного LLM-ассистента с shell, чтением файлов, MCP-коннекторами, плагинами, браузером в box, CLI `browse` и субагентами computer use, управляемыми скриншотами. Она велит боту **планировать, проверять и разбирать исключения с помощью LLM, а выполнять кодом**: повторяющаяся работа становится скриптом, пакеты идут через CSV/JSON, браузер — последнее средство, платные кредиты требуют согласия владельца, а сообщения между ботами остаются короткими.

Сама skill (`SKILL.md`) и остальная часть репозитория написаны на английском. Переведён только этот README: 14 переводов плюс английский оригинал.

## Установка

1. **Проще всего:** в чате Grok Bot попросите сохранить её как skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Вручную:** скопируйте весь `SKILL.md` (вместе с frontmatter) в редактор skills бота или вставьте его в чат и попросите сохранить как skill.
3. **Агенты, читающие папки со skills** (в стиле Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Затем вызывайте её через `/grokbot-economy` или упоминайте в рутинах. Благодаря описанию боты загружают её в начале любой задачи, перед открытием браузера, перед повтором задачи и при написании другим ботам.

## Принципы

| # | Путь | Для чего |
|---|---|---|
| 1 | Script/CLI | всё, для чего уже есть скрипт |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | готовые сторонние рецепты |
| 4 | API | сервисы без коннектора |
| 5 | `browse` CLI (text/DOM) | сайты без API, читаемые как текст |
| 6 | Computer use (screenshots) | только вход (2FA завершает человек), исключения, UI без API и без DOM для скриптов; капча/антибот-блокировка → остановиться и передать человеку или использовать официальный API |

- **LLM планирует; код выполняет.** Задача, встреченная дважды, становится скриптом с `--dry-run`, идемпотентностью и тестом.
- **Чек-лист перед браузером:** скрипт? коннектор? плагин? API? справится ли `browse` через текст?
- **Пакеты через CSV/JSON + скрипт**, никогда поле за полем в UI; сообщайте только об ошибках.
- **Экономное чтение:** `rg` + чтение с offset/limit, без вывода файлов целиком, без повторного чтения, без циклов sleep/polling.
- **Финансовые ограничители:** никогда не тратьте платные кредиты (TTS сверх квоты, кредиты на клипы, рекламу) без явного согласия владельца; соблюдайте файлы блокировки квоты.
- **Безопасная правка файлов:** dry-run, тесты на копиях, бэкап + атомарная замена, блокировки, маленькие диффы.
- **Instagram/WhatsApp:** сначала официальный API; иначе осторожные отправки в человеческом темпе с одобрением человека; никаких инструментов обхода антибот-защиты; остановка при первом предупреждении.
- **Сообщения между ботами:** короткие, со ссылками на пути к файлам, пункты сгруппированы, без сообщений-подтверждений «ок».
- **Модель по размеру задачи:** низкое усилие для механической работы, высокое — только для решений; долгие задачи в фоне.

## Содержимое репозитория

| Файл | Что |
|---|---|
| [`SKILL.md`](../SKILL.md) | Сама skill: лестница затрат, чек-листы, инструменты браузера, антипаттерны, схема принятия решений, правило сопровождения |
| [`CHANGELOG.md`](../CHANGELOG.md) | Каждое изменение skill с причиной и оценкой экономии |
| [`examples/flows.md`](../examples/flows.md) | Конкретные сценарии: таблица, Drive, доска координации, видео, пакеты, отправки |
| [`checklists/`](../checklists/) | Перед браузером, новый скрипт, отправка в Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Append-only логгер токенов/стоимости по задачам (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Шаблон метрики (заголовок CSV + примеры) |
| [`tests/`](../tests/) | Юнит-тесты логгера |
| [`assets/banner.png`](../assets/banner.png) | Баннер README |

## Измеряйте

Записывайте токены/стоимость по задаче и использованный путь. Если в сводке преобладают `browse` или `computer-use`, не хватает скрипта.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Участие

- Нашли более дешёвый путь (новый скрипт, коннектор, API, плагин, флаг CLI)? Откройте PR с изменением `SKILL.md` **и** добавьте строку в `CHANGELOG.md` (дата, что, почему, оценка экономии). Это постоянное правило для всех ботов.
- Держите `SKILL.md` коротким (< ~250 строк), в повелительном наклонении и на английском.
- **Публичный репозиторий:** никаких токенов, ключей, e-mail, телефонов, имён клиентов, ID файлов, hostname или внутренних URL. Используйте плейсхолдеры вроде `<DRIVE_FILE_ID>`.
- Перед открытием PR запустите selftest и юнит-тесты.

## Лицензия

MIT. См. [LICENSE](../LICENSE).
