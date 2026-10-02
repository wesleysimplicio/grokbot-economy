<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Une skill permanente qui fait travailler chaque Grok Bot par des chemins prêts et déterministes et arrête de brûler des tokens.</strong><br />
  <em>Les commandes restent en anglais pour pouvoir être copiées telles quelles.</em>
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
  <img src="../assets/banner.png" alt="Échelle de coûts abstraite : étapes scriptées bon marché à gauche, computer use coûteux à droite" width="860" />
</p>

---

## En bref

`grokbot-economy` est une skill pour Grok Bot, un assistant de bureau à base de LLM doté d'un shell, de la lecture de fichiers, de connecteurs MCP, de plugins, d'un navigateur dans la box, de la CLI `browse` et de sous-agents de computer use pilotés par captures d'écran. Elle demande au bot de **planifier, relire et traiter les exceptions avec le LLM, et d'exécuter avec du code** : le travail répété devient un script, les lots passent par CSV/JSON, le navigateur est le dernier recours, les crédits payants exigent l'accord du propriétaire et les messages entre bots restent courts.

La skill elle-même (`SKILL.md`) est rédigée en portugais du Brésil, la langue de travail de l'équipe. Ce README est disponible en 15 langues.

## Installation

1. **Le plus simple :** dans un chat Grok Bot, demandez-lui de l'enregistrer comme skill :

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manuel :** copiez tout `SKILL.md` (frontmatter compris) dans l'éditeur de skills du bot, ou collez-le dans le chat et demandez de l'enregistrer comme skill.
3. **Agents qui lisent des dossiers de skills** (style Cursor/Claude) :

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Ensuite, invoquez-la avec `/grokbot-economy` ou citez-la dans des routines. Sa description fait que les bots la chargent au début de chaque tâche, avant d'ouvrir le navigateur, avant de répéter une tâche et quand ils écrivent à d'autres bots.

## Principes

| # | Chemin | À utiliser pour |
|---|---|---|
| 1 | Script/CLI | tout ce qui a déjà un script |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | recettes prêtes de tiers |
| 4 | API | services sans connecteur |
| 5 | `browse` CLI (text/DOM) | sites sans API, lus comme du texte |
| 6 | Computer use (screenshots) | uniquement connexion, 2FA, captcha, exceptions, sites qui bloquent l'automatisation |

- **Le LLM planifie ; le code exécute.** Une tâche vue deux fois devient un script avec `--dry-run`, idempotence et test.
- **Checklist avant le navigateur :** script ? connecteur ? plugin ? API ? `browse` peut-il le faire par le texte ?
- **Lots via CSV/JSON + script**, jamais champ par champ dans une UI ; ne signalez que les échecs.
- **Lecture économe :** `rg` + lectures avec offset/limit, pas de dumps complets, pas de relecture, pas de boucles sleep/polling.
- **Garde-fous financiers :** ne dépensez jamais de crédits payants (TTS au-delà du quota, crédits de clipping, publicités) sans l'accord explicite du propriétaire ; respectez les fichiers de verrou de quota.
- **Modifications de fichiers sûres :** dry-run, tests sur des copies, sauvegarde + remplacement atomique, verrous, petits diffs.
- **Instagram/WhatsApp :** l'API officielle d'abord ; sinon des envois prudents, au rythme humain et validés par un humain ; aucun outil de contournement anti-bot ; arrêt au premier avertissement.
- **Messages entre bots :** courts, avec des chemins de fichiers, éléments regroupés, pas de messages de simple accusé de réception.
- **Modèle bien dimensionné :** effort faible pour le travail mécanique, élevé seulement pour le jugement ; tâches longues en arrière-plan.

## Contenu du dépôt

| Fichier | Contenu |
|---|---|
| [`SKILL.md`](../SKILL.md) | La skill (PT-BR) : échelle de coûts, checklists, outils de navigateur, anti-patterns, organigramme de décision, règle de maintenance |
| [`CHANGELOG.md`](../CHANGELOG.md) | Chaque modification de la skill, avec la raison et l'économie estimée |
| [`examples/fluxos.md`](../examples/fluxos.md) | Flux concrets : tableur, Drive, tableau de coordination, vidéos, lots, envois |
| [`checklists/`](../checklists/) | Avant le navigateur, nouveau script, envoi Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only de tokens/coût par tâche (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Modèle de la métrique (en-tête CSV + exemples) |
| [`tests/`](../tests/) | Tests unitaires du logger |
| [`assets/banner.png`](../assets/banner.png) | Bannière du README |

## Mesurez

Enregistrez les tokens/le coût par tâche et le chemin utilisé. Si `browse` ou `computer-use` dominent le résumé, il manque un script.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Contribuer

- Vous avez trouvé un chemin moins cher (nouveau script, connecteur, API, plugin, option de CLI) ? Ouvrez une PR qui modifie `SKILL.md` **et** ajoutez une ligne à `CHANGELOG.md` (date, quoi, pourquoi, économie estimée). C'est une règle permanente pour tous les bots.
- Gardez `SKILL.md` court (< ~250 lignes), impératif et en PT-BR.
- **Dépôt public :** pas de tokens, clés, e-mails, numéros de téléphone, noms de clients, ID de fichiers, hostnames ni URL internes. Utilisez des placeholders comme `<DRIVE_FILE_ID>`.
- Lancez le selftest et les tests unitaires avant d'ouvrir la PR.

## Licence

MIT. Voir [LICENSE](../LICENSE).
