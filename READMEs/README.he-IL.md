<h1 align="center" dir="rtl">grokbot-economy</h1>

<p align="center" dir="rtl">
  <strong>Skill קבועה שגורמת לכל Grok Bot לעבוד במסלולים מוכנים ודטרמיניסטיים ולהפסיק לשרוף טוקנים.</strong><br />
  <em>הפקודות נשארות באנגלית כדי שאפשר יהיה להעתיק אותן במדויק.</em>
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
  <img src="../assets/banner.png" alt="סולם עלויות מופשט: צעדי סקריפט זולים משמאל, computer use יקר מימין" width="860" />
</p>

---

## בקצרה

`grokbot-economy` היא skill עבור Grok Bot, עוזר שולחני מבוסס LLM עם shell, קריאת קבצים, מחברי MCP, תוספים, דפדפן ב-box, ה-CLI ‏`browse` ותת-סוכני computer use המונעים בצילומי מסך. היא מורה ל-bot **לתכנן, לבדוק ולטפל בחריגים בעזרת ה-LLM, ולבצע בעזרת קוד**: עבודה חוזרת הופכת לסקריפט, אצוות עוברות דרך CSV/JSON, הדפדפן הוא המוצא האחרון, קרדיטים בתשלום דורשים אישור של הבעלים, והודעות בין bots נשארות קצרות.

ה-skill עצמה (`SKILL.md`) ושאר המאגר כתובים באנגלית. רק ה-README הזה מתורגם, ל-15 שפות.

## התקנה

1. **הכי פשוט:** בצ'אט עם Grok Bot, בקשו לשמור אותה כ-skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **ידנית:** העתיקו את כל `SKILL.md` (כולל ה-frontmatter) לעורך ה-skills של ה-bot, או הדביקו בצ'אט ובקשו לשמור כ-skill.
3. **סוכנים שקוראים תיקיות skills** (בסגנון Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

לאחר מכן הפעילו אותה עם `/grokbot-economy` או הזכירו אותה בשגרות. התיאור שלה גורם ל-bots לטעון אותה בתחילת כל משימה, לפני פתיחת הדפדפן, לפני חזרה על משימה וכששולחים הודעה ל-bots אחרים.

## עקרונות

| # | מסלול | מתי להשתמש |
|---|---|---|
| 1 | Script/CLI | כל מה שכבר יש לו סקריפט |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | מתכונים מוכנים של צד שלישי |
| 4 | API | שירותים בלי מחבר |
| 5 | `browse` CLI (text/DOM) | אתרים בלי API, שנקראים כטקסט |
| 6 | Computer use (screenshots) | רק התחברות (אדם משלים את ה-2FA), חריגים וממשקים בלי API או DOM שניתן לסקריפט; captcha/חסימת anti-bot → עוצרים ומעבירים לאדם, או משתמשים ב-API הרשמי |

- **ה-LLM מתכנן; הקוד מבצע.** משימה שהופיעה פעמיים הופכת לסקריפט עם `--dry-run`, אידמפוטנטיות ובדיקה.
- **צ'קליסט לפני הדפדפן:** סקריפט? מחבר? תוסף? API? האם `browse` יכול לעשות זאת דרך טקסט?
- **אצוות דרך CSV/JSON + סקריפט**, אף פעם לא שדה אחר שדה בממשק; מדווחים רק על כשלים.
- **קריאה חסכונית:** `rg` + קריאה עם offset/limit, בלי לשפוך קבצים שלמים, בלי לקרוא שוב, בלי לולאות sleep/polling.
- **מעקות כסף:** לעולם לא לבזבז קרדיטים בתשלום (TTS מעבר למכסה, קרדיטים לקליפים, פרסומות) בלי אישור מפורש של הבעלים; לכבד קובצי נעילת מכסה.
- **עריכת קבצים בטוחה:** dry-run, בדיקה על עותקים, גיבוי + החלפה אטומית, נעילות, שינויים קטנים.
- **Instagram/WhatsApp:** קודם ה-API הרשמי; אחרת שליחה זהירה, בקצב אנושי ובאישור אנושי לכל הודעה; בלי כלים לעקיפת מנגנוני anti-bot; עוצרים באזהרה הראשונה.
- **הודעות בין bots:** קצרות, מפנות לנתיבי קבצים, מאחדות פריטים, בלי הודעות של "קיבלתי" בלבד.
- **מודל בגודל הנכון:** מאמץ נמוך לעבודה מכנית, מאמץ גבוה רק לשיקול דעת; משימות ארוכות ברקע.

## תוכן המאגר

| קובץ | מה |
|---|---|
| [`SKILL.md`](../SKILL.md) | ה-skill: סולם עלויות, צ'קליסטים, אפשרויות כלי דפדפן, אנטי-דפוסים, תרשים החלטה, כלל תחזוקה |
| [`CHANGELOG.md`](../CHANGELOG.md) | כל שינוי ב-skill, עם הסיבה והחיסכון המשוער |
| [`examples/flows.md`](../examples/flows.md) | תהליכים מעשיים: גיליון, Drive, לוח תיאום, סרטונים, אצוות, שליחות |
| [`checklists/`](../checklists/) | לפני הדפדפן, סקריפט חדש, שליחה ב-Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | לוגר append-only של טוקנים/עלות לכל משימה (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | תבנית המדד (כותרת CSV + דוגמאות) |
| [`tests/`](../tests/) | בדיקות יחידה ללוגר |
| [`assets/banner.png`](../assets/banner.png) | באנר ה-README |

## מדדו

רשמו טוקנים/עלות לכל משימה ואת המסלול שבו השתמשתם. אם `browse` או `computer-use` שולטים בסיכום, חסר סקריפט.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## תרומה

- מצאתם מסלול זול יותר (סקריפט חדש, מחבר, API, תוסף, דגל CLI)? פתחו PR שמשנה את `SKILL.md` **והוסיפו** שורה ל-`CHANGELOG.md` (תאריך, מה, למה, חיסכון משוער). זה כלל קבוע לכל ה-bots.
- שמרו על `SKILL.md` קצר (פחות מ-~250 שורות), בלשון ציווי ובאנגלית.
- **מאגר ציבורי:** בלי טוקנים, מפתחות, כתובות מייל, מספרי טלפון, שמות לקוחות, מזהי קבצים, שמות שרתים או כתובות פנימיות. השתמשו בממלאי מקום כמו `<DRIVE_FILE_ID>`.
- הריצו את ה-selftest ואת בדיקות היחידה לפני פתיחת ה-PR.

## רישיון

MIT. ראו [LICENSE](../LICENSE).
