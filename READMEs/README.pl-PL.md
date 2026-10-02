<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Stała skill, dzięki której każdy Grok Bot pracuje gotowymi, deterministycznymi ścieżkami i przestaje palić tokeny.</strong><br />
  <em>Polecenia zostają po angielsku, aby można je było skopiować dokładnie.</em>
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
  <img src="../assets/banner.png" alt="Abstrakcyjna drabina kosztów: tanie kroki skryptowe po lewej, drogie computer use po prawej" width="860" />
</p>

---

## W skrócie

`grokbot-economy` to skill dla Grok Bota, desktopowego asystenta LLM z powłoką, odczytem plików, konektorami MCP, pluginami, przeglądarką w boxie, CLI `browse` i subagentami computer use sterowanymi zrzutami ekranu. Każe botowi **planować, sprawdzać i obsługiwać wyjątki przez LLM, a wykonywać kodem**: powtarzalna praca staje się skryptem, partie idą przez CSV/JSON, przeglądarka to ostateczność, płatne kredyty wymagają zgody właściciela, a wiadomości między botami są krótkie.

Sama skill (`SKILL.md`) i reszta repozytorium są po angielsku. Tylko ten README jest przetłumaczony, na 15 języków.

## Instalacja

1. **Najprościej:** na czacie z Grok Botem poproś, by zapisał ją jako skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Ręcznie:** skopiuj cały `SKILL.md` (razem z frontmatter) do edytora skilli bota albo wklej go na czacie i poproś o zapisanie jako skill.
3. **Agenci czytający foldery skilli** (styl Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Następnie wywołuj ją przez `/grokbot-economy` albo wspominaj w rutynach. Jej opis sprawia, że boty ładują ją na początku każdego zadania, przed otwarciem przeglądarki, przed powtórzeniem zadania i przy pisaniu do innych botów.

## Zasady

| # | Ścieżka | Do czego |
|---|---|---|
| 1 | Script/CLI | wszystko, co ma już skrypt |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | gotowe przepisy firm trzecich |
| 4 | API | usługi bez konektora |
| 5 | `browse` CLI (text/DOM) | strony bez API, czytane jako tekst |
| 6 | Computer use (screenshots) | tylko logowanie, 2FA, captcha, wyjątki, strony blokujące automatyzację |

- **LLM planuje; kod wykonuje.** Zadanie widziane dwa razy staje się skryptem z `--dry-run`, idempotencją i testem.
- **Checklista przed przeglądarką:** skrypt? konektor? plugin? API? czy `browse` zrobi to przez tekst?
- **Partie przez CSV/JSON + skrypt**, nigdy pole po polu w UI; raportuj tylko błędy.
- **Tanie czytanie:** `rg` + odczyt z offset/limit, bez zrzucania całych plików, bez ponownego czytania, bez pętli sleep/polling.
- **Bezpieczniki finansowe:** nigdy nie wydawaj płatnych kredytów (TTS ponad limit, kredyty na klipy, reklamy) bez wyraźnej zgody właściciela; respektuj pliki blokady limitu.
- **Bezpieczna edycja plików:** dry-run, testy na kopiach, backup + atomowa podmiana, blokady, małe diffy.
- **Instagram/WhatsApp:** najpierw oficjalne API; w przeciwnym razie ostrożne wysyłki w ludzkim tempie, każda zatwierdzona przez człowieka; żadnych narzędzi do obchodzenia zabezpieczeń anty-bot; stop przy pierwszym ostrzeżeniu.
- **Wiadomości między botami:** krótkie, ze ścieżkami do plików, zgrupowane, bez wiadomości typu samo „ok”.
- **Model dobrany do zadania:** niski wysiłek dla pracy mechanicznej, wysoki tylko dla decyzji; długie zadania w tle.

## Zawartość repozytorium

| Plik | Co |
|---|---|
| [`SKILL.md`](../SKILL.md) | Skill: drabina kosztów, checklisty, narzędzia przeglądarki, antywzorce, schemat decyzyjny, zasada utrzymania |
| [`CHANGELOG.md`](../CHANGELOG.md) | Każda zmiana w skill, z powodem i szacowaną oszczędnością |
| [`examples/flows.md`](../examples/flows.md) | Konkretne przepływy: arkusz, Drive, tablica koordynacji, wideo, partie, wysyłki |
| [`checklists/`](../checklists/) | Przed przeglądarką, nowy skrypt, wysyłka przez Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only tokenów/kosztu na zadanie (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Szablon metryki (nagłówek CSV + przykłady) |
| [`tests/`](../tests/) | Testy jednostkowe loggera |
| [`assets/banner.png`](../assets/banner.png) | Baner README |

## Mierz

Zapisuj tokeny/koszt na zadanie i użytą ścieżkę. Jeśli w podsumowaniu dominują `browse` lub `computer-use`, brakuje skryptu.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Współtworzenie

- Znalazłeś tańszą ścieżkę (nowy skrypt, konektor, API, plugin, flaga CLI)? Otwórz PR zmieniający `SKILL.md` **i** dodaj linię do `CHANGELOG.md` (data, co, dlaczego, szacowana oszczędność). To stała zasada dla wszystkich botów.
- Utrzymuj `SKILL.md` krótki (< ~250 linii), w trybie rozkazującym i po angielsku.
- **Publiczne repo:** żadnych tokenów, kluczy, e-maili, numerów telefonów, nazw klientów, ID plików, hostname'ów ani wewnętrznych URL-i. Używaj placeholderów jak `<DRIVE_FILE_ID>`.
- Przed otwarciem PR uruchom selftest i testy jednostkowe.

## Licencja

MIT. Zobacz [LICENSE](../LICENSE).
