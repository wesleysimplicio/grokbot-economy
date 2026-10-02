<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>एक स्थायी skill जो हर Grok Bot को तैयार, नियतात्मक (deterministic) रास्तों से काम करवाती है और token की बर्बादी रोकती है।</strong><br />
  <em>कमांड अंग्रेज़ी में ही रहती हैं ताकि उन्हें हूबहू कॉपी किया जा सके।</em>
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
  <img src="../assets/banner.png" alt="अमूर्त लागत सीढ़ी: बाईं ओर सस्ते स्क्रिप्ट वाले कदम, दाईं ओर महँगा computer use" width="860" />
</p>

---

## संक्षेप में

`grokbot-economy` Grok Bot के लिए एक skill है। Grok Bot एक LLM डेस्कटॉप सहायक है जिसके पास shell, फ़ाइल पढ़ने की सुविधा, MCP कनेक्टर, प्लगइन, box ब्राउज़र, `browse` CLI और स्क्रीनशॉट से चलने वाले computer use सबएजेंट हैं। यह skill bot से कहती है कि **योजना, समीक्षा और अपवाद LLM से संभालो, और काम कोड से करवाओ**: दोहराया जाने वाला काम स्क्रिप्ट बनता है, बैच CSV/JSON से चलते हैं, ब्राउज़र आख़िरी विकल्प है, पेड क्रेडिट के लिए मालिक की मंज़ूरी ज़रूरी है, और bot-से-bot संदेश छोटे रहते हैं।

skill ख़ुद (`SKILL.md`) टीम की कामकाजी भाषा, ब्राज़ीलियाई पुर्तगाली, में लिखी गई है। यह README 15 भाषाओं में उपलब्ध है।

## इंस्टॉल करें

1. **सबसे आसान:** Grok Bot चैट में उसे skill के रूप में सेव करने को कहें:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **मैन्युअल:** पूरी `SKILL.md` (frontmatter सहित) bot के skill एडिटर में कॉपी करें, या चैट में पेस्ट करके उसे skill के रूप में सेव करने को कहें।
3. **skill फ़ोल्डर पढ़ने वाले एजेंट** (Cursor/Claude शैली):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

फिर इसे `/grokbot-economy` से चलाएँ या रूटीन में इसका ज़िक्र करें। इसके विवरण की वजह से bot इसे हर काम की शुरुआत में, ब्राउज़र खोलने से पहले, कोई काम दोहराने से पहले और दूसरे bots को संदेश भेजते समय लोड करते हैं।

## सिद्धांत

| # | रास्ता | किसके लिए |
|---|---|---|
| 1 | Script/CLI | जिस भी काम की स्क्रिप्ट पहले से है |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | तीसरे पक्ष के तैयार नुस्ख़े |
| 4 | API | बिना कनेक्टर वाली सेवाएँ |
| 5 | `browse` CLI (text/DOM) | बिना API वाली साइटें, टेक्स्ट के रूप में पढ़ी गईं |
| 6 | Computer use (screenshots) | सिर्फ़ साइन-इन, 2FA, captcha, अपवाद, और ऑटोमेशन रोकने वाली साइटें |

- **LLM योजना बनाता है; कोड काम करता है।** जो काम दो बार आए, वह `--dry-run`, idempotency और टेस्ट वाली स्क्रिप्ट बने।
- **ब्राउज़र से पहले चेकलिस्ट:** स्क्रिप्ट? कनेक्टर? प्लगइन? API? क्या `browse` टेक्स्ट से कर सकता है?
- **बैच CSV/JSON + स्क्रिप्ट से**, UI में कभी एक-एक फ़ील्ड नहीं; सिर्फ़ विफलताओं की रिपोर्ट करें।
- **किफ़ायती पढ़ाई:** `rg` + offset/limit से पढ़ना, पूरी फ़ाइल डंप नहीं, दोबारा पढ़ना नहीं, sleep/polling लूप नहीं।
- **पैसे की सुरक्षा:** मालिक की स्पष्ट मंज़ूरी के बिना कभी पेड क्रेडिट (कोटा से ऊपर TTS, क्लिपिंग क्रेडिट, विज्ञापन) ख़र्च न करें; कोटा लॉक फ़ाइलों का सम्मान करें।
- **सुरक्षित फ़ाइल संपादन:** dry-run, कॉपी पर टेस्ट, बैकअप + atomic swap, फ़ाइल लॉक, छोटे diff।
- **Instagram/WhatsApp:** पहले आधिकारिक API; वरना सावधान, इंसानी रफ़्तार वाले, इंसान से मंज़ूर भेजे गए संदेश; कोई anti-bot बचाव टूल नहीं; पहली चेतावनी पर रुकें।
- **bot-से-bot संदेश:** छोटे, फ़ाइल पाथ की ओर इशारा, आइटम एक साथ, सिर्फ़ "ठीक है" वाले संदेश नहीं।
- **सही आकार का मॉडल:** यांत्रिक काम के लिए कम effort, ऊँचा effort सिर्फ़ निर्णय के लिए; लंबे काम बैकग्राउंड में।

## रिपॉज़िटरी में क्या है

| फ़ाइल | क्या |
|---|---|
| [`SKILL.md`](../SKILL.md) | skill (PT-BR): लागत सीढ़ी, चेकलिस्ट, ब्राउज़र टूल के विकल्प, anti-patterns, निर्णय फ़्लोचार्ट, रखरखाव नियम |
| [`CHANGELOG.md`](../CHANGELOG.md) | skill का हर बदलाव, कारण और अनुमानित बचत के साथ |
| [`examples/fluxos.md`](../examples/fluxos.md) | ठोस फ़्लो: स्प्रेडशीट, Drive, समन्वय बोर्ड, वीडियो, बैच, भेजना |
| [`checklists/`](../checklists/) | ब्राउज़र से पहले, नई स्क्रिप्ट, Instagram/WhatsApp भेजना |
| [`scripts/token_log.py`](../scripts/token_log.py) | हर काम के token/लागत का append-only लॉगर (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | मेट्रिक टेम्पलेट (CSV हेडर + उदाहरण) |
| [`tests/`](../tests/) | लॉगर के यूनिट टेस्ट |
| [`assets/banner.png`](../assets/banner.png) | README बैनर |

## मापें

हर काम के token/लागत और इस्तेमाल किया गया रास्ता लॉग करें। अगर सारांश में `browse` या `computer-use` हावी हैं, तो कोई स्क्रिप्ट कम है।

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## योगदान

- कोई सस्ता रास्ता मिला (नई स्क्रिप्ट, कनेक्टर, API, प्लगइन, CLI फ़्लैग)? `SKILL.md` बदलने वाला PR खोलें **और** `CHANGELOG.md` में एक पंक्ति जोड़ें (तारीख़, क्या, क्यों, अनुमानित बचत)। यह सभी bots के लिए स्थायी नियम है।
- `SKILL.md` को छोटा (< ~250 पंक्तियाँ), आदेशात्मक और PT-BR में रखें।
- **सार्वजनिक repo:** कोई token, key, ईमेल, फ़ोन नंबर, क्लाइंट का नाम, फ़ाइल ID, hostname या आंतरिक URL नहीं। `<DRIVE_FILE_ID>` जैसे placeholder इस्तेमाल करें।
- PR खोलने से पहले selftest और यूनिट टेस्ट चलाएँ।

## लाइसेंस

MIT. देखें [LICENSE](../LICENSE)।
