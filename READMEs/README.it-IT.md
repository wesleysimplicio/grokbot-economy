<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Una skill permanente che fa lavorare ogni Grok Bot su percorsi pronti e deterministici e smettere di bruciare token.</strong><br />
  <em>I comandi restano in inglese per poterli copiare esattamente.</em>
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
  <img src="../assets/banner.png" alt="Scala dei costi astratta: passi economici via script a sinistra, computer use costoso a destra" width="860" />
</p>

---

## In breve

`grokbot-economy` è una skill per Grok Bot, un assistente desktop basato su LLM con shell, lettura di file, connettori MCP, plugin, un browser nel box, la CLI `browse` e subagenti di computer use guidati da screenshot. Dice al bot di **pianificare, revisionare e gestire le eccezioni con l'LLM, ed eseguire con il codice**: il lavoro ripetuto diventa uno script, i batch passano da CSV/JSON, il browser è l'ultima risorsa, i crediti a pagamento richiedono l'OK del proprietario e i messaggi tra bot restano brevi.

La skill (`SKILL.md`) e il resto del repository sono in inglese. Solo questo README è tradotto, in 15 lingue.

## Installazione

1. **Il modo più semplice:** in una chat di Grok Bot, chiedi di salvarla come skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manuale:** copia tutto `SKILL.md` (frontmatter incluso) nell'editor delle skill del bot, oppure incollalo in chat e chiedi di salvarlo come skill.
3. **Agenti che leggono cartelle di skill** (stile Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Poi richiamala con `/grokbot-economy` o citala nelle routine. La sua descrizione fa sì che i bot la carichino all'inizio di ogni attività, prima di aprire il browser, prima di ripetere un'attività e quando scrivono ad altri bot.

## Principi

| # | Percorso | Usalo per |
|---|---|---|
| 1 | Script/CLI | tutto ciò che ha già uno script |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | ricette pronte di terze parti |
| 4 | API | servizi senza connettore |
| 5 | `browse` CLI (text/DOM) | siti senza API, letti come testo |
| 6 | Computer use (screenshots) | solo login (una persona completa il 2FA), eccezioni, UI senza API né DOM automatizzabile; captcha/blocco anti-bot → fermati e passa a una persona, o usa l'API ufficiale |

- **L'LLM pianifica; il codice esegue.** Un'attività vista due volte diventa uno script con `--dry-run`, idempotenza e test.
- **Checklist prima del browser:** script? connettore? plugin? API? `browse` ci riesce leggendo il testo?
- **Batch con CSV/JSON + script**, mai campo per campo in una UI; segnala solo i fallimenti.
- **Lettura economica:** `rg` + letture con offset/limit, niente dump completi, niente riletture, niente loop di sleep/polling.
- **Limiti di spesa:** mai spendere crediti a pagamento (TTS oltre la quota, crediti di clipping, annunci) senza l'OK esplicito del proprietario; rispetta i file di blocco quota.
- **Modifiche sicure ai file:** dry-run, test su copie, backup + sostituzione atomica, lock, diff piccoli.
- **Instagram/WhatsApp:** prima l'API ufficiale; altrimenti invii prudenti, a ritmo umano e approvati da una persona; nessuno strumento di elusione anti-bot; fermati al primo avviso.
- **Messaggi tra bot:** brevi, con percorsi di file, elementi raggruppati, niente messaggi di solo «ok».
- **Modello della taglia giusta:** sforzo basso per il lavoro meccanico, alto solo per le decisioni; lavori lunghi in background.

## Contenuto del repository

| File | Cosa |
|---|---|
| [`SKILL.md`](../SKILL.md) | La skill: scala dei costi, checklist, strumenti per il browser, anti-pattern, diagramma decisionale, regola di manutenzione |
| [`CHANGELOG.md`](../CHANGELOG.md) | Ogni modifica alla skill, con motivo e risparmio stimato |
| [`examples/flows.md`](../examples/flows.md) | Flussi concreti: foglio di calcolo, Drive, board di coordinamento, video, batch, invii |
| [`checklists/`](../checklists/) | Prima del browser, nuovo script, invio Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only di token/costo per attività (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Modello della metrica (intestazione CSV + esempi) |
| [`tests/`](../tests/) | Test unitari del logger |
| [`assets/banner.png`](../assets/banner.png) | Banner del README |

## Misuralo

Registra token/costo per attività e il percorso usato. Se `browse` o `computer-use` dominano il riepilogo, manca uno script.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Contribuire

- Hai trovato un percorso più economico (nuovo script, connettore, API, plugin, flag della CLI)? Apri una PR che modifica `SKILL.md` **e** aggiungi una riga a `CHANGELOG.md` (data, cosa, perché, risparmio stimato). È una regola permanente per tutti i bot.
- Mantieni `SKILL.md` breve (< ~250 righe), imperativo e in inglese.
- **Repo pubblico:** niente token, chiavi, email, numeri di telefono, nomi di clienti, ID di file, hostname o URL interni. Usa placeholder come `<DRIVE_FILE_ID>`.
- Esegui il selftest e i test unitari prima di aprire la PR.

## Licenza

MIT. Vedi [LICENSE](../LICENSE).
