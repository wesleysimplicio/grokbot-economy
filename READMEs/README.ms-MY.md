<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Skill kekal yang membuatkan setiap Grok Bot bekerja melalui laluan sedia ada yang deterministik dan berhenti membazir token.</strong><br />
  <em>Arahan kekal dalam bahasa Inggeris supaya boleh disalin dengan tepat.</em>
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
  <img src="../assets/banner.png" alt="Tangga kos abstrak: langkah skrip murah di kiri, computer use mahal di kanan" width="860" />
</p>

---

## Ringkasnya

`grokbot-economy` ialah skill untuk Grok Bot, pembantu desktop berasaskan LLM dengan shell, bacaan fail, penyambung MCP, plugin, pelayar dalam box, CLI `browse` dan subejen computer use yang dipandu tangkapan skrin. Ia mengarahkan bot untuk **merancang, menyemak dan mengendalikan pengecualian dengan LLM, dan melaksanakan dengan kod**: kerja berulang menjadi skrip, kelompok diproses melalui CSV/JSON, pelayar ialah pilihan terakhir, kredit berbayar memerlukan kelulusan pemilik, dan mesej antara bot kekal ringkas.

Skill itu sendiri (`SKILL.md`) dan selebihnya repositori ditulis dalam bahasa Inggeris. Hanya README ini diterjemahkan, ke dalam 15 bahasa.

## Pemasangan

1. **Paling mudah:** dalam sembang Grok Bot, minta bot menyimpannya sebagai skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manual:** salin keseluruhan `SKILL.md` (termasuk frontmatter) ke editor skill bot, atau tampal dalam sembang dan minta ia disimpan sebagai skill.
3. **Ejen yang membaca folder skill** (gaya Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Kemudian panggil dengan `/grokbot-economy` atau sebut dalam rutin. Penerangannya membuatkan bot memuatkannya pada permulaan setiap tugas, sebelum membuka pelayar, sebelum mengulang tugas dan semasa menghantar mesej kepada bot lain.

## Prinsip

| # | Laluan | Gunakan untuk |
|---|---|---|
| 1 | Script/CLI | apa sahaja yang sudah ada skrip |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | resipi sedia ada daripada pihak ketiga |
| 4 | API | perkhidmatan tanpa penyambung |
| 5 | `browse` CLI (text/DOM) | laman tanpa API, dibaca sebagai teks |
| 6 | Computer use (screenshots) | hanya log masuk, 2FA, captcha, pengecualian, laman yang menyekat automasi |

- **LLM merancang; kod melaksana.** Tugas yang muncul dua kali menjadi skrip dengan `--dry-run`, idempoten dan ujian.
- **Senarai semak sebelum pelayar:** skrip? penyambung? plugin? API? bolehkah `browse` melakukannya melalui teks?
- **Kelompok melalui CSV/JSON + skrip**, jangan sekali-kali medan demi medan dalam UI; laporkan kegagalan sahaja.
- **Bacaan jimat:** `rg` + bacaan dengan offset/limit, tiada lambakan fail penuh, tiada bacaan semula, tiada gelung sleep/polling.
- **Kawalan wang:** jangan sekali-kali guna kredit berbayar (TTS melebihi kuota, kredit klip, iklan) tanpa kelulusan jelas pemilik; patuhi fail kunci kuota.
- **Suntingan fail yang selamat:** dry-run, uji pada salinan, sandaran + tukar atom, kunci, diff kecil.
- **Instagram/WhatsApp:** API rasmi dahulu; jika tiada, penghantaran konservatif pada rentak manusia dan diluluskan manusia; tiada alat mengelak anti-bot; berhenti pada amaran pertama.
- **Mesej antara bot:** ringkas, merujuk laluan fail, item digabungkan, tiada mesej «ok» semata-mata.
- **Model bersaiz tepat:** usaha rendah untuk kerja mekanikal, tinggi hanya untuk pertimbangan; kerja panjang di latar belakang.

## Kandungan repositori

| Fail | Apa |
|---|---|
| [`SKILL.md`](../SKILL.md) | Skill: tangga kos, senarai semak, pilihan alat pelayar, anti-corak, carta alir keputusan, peraturan penyelenggaraan |
| [`CHANGELOG.md`](../CHANGELOG.md) | Setiap perubahan pada skill, dengan sebab dan anggaran penjimatan |
| [`examples/flows.md`](../examples/flows.md) | Aliran konkrit: hamparan, Drive, papan koordinasi, video, kelompok, penghantaran |
| [`checklists/`](../checklists/) | Sebelum pelayar, skrip baharu, penghantaran Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only token/kos setiap tugas (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Templat metrik (pengepala CSV + contoh) |
| [`tests/`](../tests/) | Ujian unit untuk logger |
| [`assets/banner.png`](../assets/banner.png) | Sepanduk README |

## Ukur

Rekod token/kos setiap tugas dan laluan yang digunakan. Jika `browse` atau `computer-use` mendominasi ringkasan, ada skrip yang belum wujud.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Menyumbang

- Jumpa laluan yang lebih murah (skrip baharu, penyambung, API, plugin, bendera CLI)? Buka PR yang mengubah `SKILL.md` **dan** tambah satu baris pada `CHANGELOG.md` (tarikh, apa, mengapa, anggaran penjimatan). Ini peraturan kekal untuk semua bot.
- Pastikan `SKILL.md` ringkas (< ~250 baris), imperatif dan dalam bahasa Inggeris.
- **Repo awam:** tiada token, kunci, e-mel, nombor telefon, nama pelanggan, ID fail, hostname atau URL dalaman. Gunakan pemegang tempat seperti `<DRIVE_FILE_ID>`.
- Jalankan selftest dan ujian unit sebelum membuka PR.

## Lesen

MIT. Lihat [LICENSE](../LICENSE).
