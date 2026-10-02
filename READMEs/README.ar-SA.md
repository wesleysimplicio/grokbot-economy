<h1 align="center" dir="rtl">grokbot-economy</h1>

<p align="center" dir="rtl">
  <strong>Skill دائمة تجعل كل Grok Bot يعمل عبر مسارات جاهزة وحتمية ويتوقف عن إهدار التوكنات.</strong><br />
  <em>تبقى الأوامر بالإنجليزية حتى يمكن نسخها بدقة.</em>
</p>

<p align="center">
<a href="https://github.com/wesleysimplicio/grokbot-economy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/wesleysimplicio/grokbot-economy?style=flat-square" /></a>
<img alt="Grok Bot skill" src="https://img.shields.io/badge/Grok%20Bot-skill-2fe6a0?style=flat-square" />
<img alt="SKILL.md pt-BR" src="https://img.shields.io/badge/SKILL.md-pt--BR-0ea5e9?style=flat-square" />
<a href="../LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" /></a>
</p>

<p align="center">
<a href="../README.md">English</a> | <a href="README.pt-BR.md">Português</a> | <a href="README.es-ES.md">Español</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.ko-KR.md">한국어</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.it-IT.md">Italiano</a> | <a href="README.fr-FR.md">Français</a> | <a href="README.ru-RU.md">Русский</a> | <a href="README.pl-PL.md">Polski</a> | <a href="README.hi-IN.md">हिन्दी</a> | <a href="README.ar-SA.md">العربية</a> | <a href="README.he-IL.md">עברית</a> | <a href="README.ms-MY.md">Bahasa Melayu</a> | <a href="README.id-ID.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img src="../assets/banner.png" alt="سلّم تكلفة تجريدي: خطوات سكربت رخيصة على اليسار، وcomputer use مكلف على اليمين" width="860" />
</p>

---

## الخلاصة

`grokbot-economy` هي skill لـ Grok Bot، وهو مساعد سطح مكتب يعمل بنموذج LLM ولديه shell وقراءة الملفات وموصلات MCP وإضافات ومتصفح داخل الـ box وأداة `browse` CLI ووكلاء فرعيون لـ computer use يعتمدون على لقطات الشاشة. توجّه الـ bot إلى **التخطيط والمراجعة ومعالجة الاستثناءات بالـ LLM، والتنفيذ بالكود**: العمل المتكرر يصبح سكربت، والدفعات تمر عبر CSV/JSON، والمتصفح هو الملاذ الأخير، والأرصدة المدفوعة تحتاج موافقة المالك، ورسائل الـ bots فيما بينها تبقى قصيرة.

الـ skill نفسها (`SKILL.md`) مكتوبة بالبرتغالية البرازيلية، لغة عمل الفريق. هذا الـ README متاح بـ 15 لغة.

## التثبيت

1. **الأسهل:** في محادثة Grok Bot، اطلب منه حفظها كـ skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **يدويًا:** انسخ `SKILL.md` بالكامل (مع الـ frontmatter) إلى محرر الـ skills في الـ bot، أو الصقه في المحادثة واطلب حفظه كـ skill.
3. **الوكلاء الذين يقرؤون مجلدات الـ skills** (بأسلوب Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

بعد ذلك استدعها بـ `/grokbot-economy` أو اذكرها في الروتينات. وصفها يجعل الـ bots تحمّلها في بداية أي مهمة، وقبل فتح المتصفح، وقبل تكرار مهمة، وعند مراسلة bots أخرى.

## المبادئ

| # | المسار | استخدمه لـ |
|---|---|---|
| 1 | Script/CLI | كل ما له سكربت جاهز |
| 2 | MCP | Drive وGmail وGitHub وCalendar... |
| 3 | Plugin/skill | وصفات جاهزة من أطراف ثالثة |
| 4 | API | الخدمات التي لا موصل لها |
| 5 | `browse` CLI (text/DOM) | المواقع التي لا API لها، تُقرأ كنص |
| 6 | Computer use (screenshots) | فقط تسجيل الدخول و2FA وcaptcha والاستثناءات والمواقع التي تحجب الأتمتة |

- **الـ LLM يخطط؛ الكود ينفذ.** المهمة التي تتكرر مرتين تصبح سكربت مع `--dry-run` وidempotency واختبار.
- **قائمة تحقق قبل المتصفح:** سكربت؟ موصل؟ إضافة؟ API؟ هل يستطيع `browse` إنجازها عبر النص؟
- **الدفعات عبر CSV/JSON + سكربت**، وليس حقلًا بحقل في واجهة؛ أبلغ عن الإخفاقات فقط.
- **قراءة اقتصادية:** `rg` + قراءة بـ offset/limit، بلا تفريغ ملفات كاملة، بلا إعادة قراءة، بلا حلقات sleep/polling.
- **ضوابط المال:** لا تنفق أبدًا أرصدة مدفوعة (TTS فوق الحصة، أرصدة القص، الإعلانات) دون موافقة صريحة من المالك؛ احترم ملفات قفل الحصة.
- **تعديل آمن للملفات:** dry-run، الاختبار على نسخ، نسخة احتياطية + استبدال ذري، أقفال ملفات، تغييرات صغيرة.
- **Instagram/WhatsApp:** الـ API الرسمي أولًا؛ وإلا فإرسال متحفظ بوتيرة بشرية وبموافقة بشرية على كل رسالة؛ لا أدوات للتحايل على أنظمة مكافحة الـ bots؛ توقف عند أول تحذير.
- **رسائل الـ bots فيما بينها:** قصيرة، تشير إلى مسارات الملفات، تجمع البنود، بلا رسائل «تم» فقط.
- **نموذج بالحجم المناسب:** جهد منخفض للعمل الآلي، وجهد عالٍ للحكم فقط؛ المهام الطويلة في الخلفية.

## محتويات المستودع

| الملف | المحتوى |
|---|---|
| [`SKILL.md`](../SKILL.md) | الـ skill (PT-BR): سلّم التكلفة، قوائم التحقق، خيارات أدوات المتصفح، الأنماط المضادة، مخطط القرار، قاعدة الصيانة |
| [`CHANGELOG.md`](../CHANGELOG.md) | كل تغيير على الـ skill مع السبب والتوفير المقدّر |
| [`examples/fluxos.md`](../examples/fluxos.md) | تدفقات عملية: جدول البيانات، Drive، لوحة التنسيق، الفيديوهات، الدفعات، الإرسال |
| [`checklists/`](../checklists/) | قبل المتصفح، سكربت جديد، الإرسال عبر Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | مسجّل append-only للتوكنات/التكلفة لكل مهمة (stdlib، `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | قالب المقياس (ترويسة CSV + أمثلة) |
| [`tests/`](../tests/) | اختبارات الوحدة للمسجّل |
| [`assets/banner.png`](../assets/banner.png) | شعار الـ README |

## قِس

سجّل التوكنات/التكلفة لكل مهمة والمسار المستخدم. إذا غلب `browse` أو `computer-use` على الملخص، فهناك سكربت ناقص.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## المساهمة

- وجدت مسارًا أرخص (سكربت جديد، موصل، API، إضافة، خيار CLI)؟ افتح PR يعدّل `SKILL.md` **وأضف** سطرًا إلى `CHANGELOG.md` (التاريخ، ماذا، لماذا، التوفير المقدّر). هذه قاعدة دائمة لكل الـ bots.
- أبقِ `SKILL.md` قصيرًا (أقل من ~250 سطرًا)، بصيغة الأمر، وبالـ PT-BR.
- **مستودع عام:** لا توكنات ولا مفاتيح ولا بريد إلكتروني ولا أرقام هواتف ولا أسماء عملاء ولا معرّفات ملفات ولا أسماء خوادم ولا روابط داخلية. استخدم عناصر نائبة مثل `<DRIVE_FILE_ID>`.
- شغّل الـ selftest واختبارات الوحدة قبل فتح الـ PR.

## الترخيص

MIT. راجع [LICENSE](../LICENSE).
