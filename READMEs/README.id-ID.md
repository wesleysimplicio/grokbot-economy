<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Skill permanen yang membuat setiap Grok Bot bekerja lewat jalur siap pakai yang deterministik dan berhenti membakar token.</strong><br />
  <em>Perintah tetap dalam bahasa Inggris agar bisa disalin persis.</em>
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
  <img src="../assets/banner.png" alt="Tangga biaya abstrak: langkah skrip murah di kiri, computer use mahal di kanan" width="860" />
</p>

---

## Ringkasnya

`grokbot-economy` adalah skill untuk Grok Bot, asisten desktop berbasis LLM dengan shell, pembacaan file, konektor MCP, plugin, browser di box, CLI `browse`, dan subagen computer use berbasis screenshot. Skill ini menyuruh bot **merencanakan, meninjau, dan menangani pengecualian dengan LLM, lalu mengeksekusi dengan kode**: pekerjaan berulang menjadi skrip, batch diproses lewat CSV/JSON, browser adalah pilihan terakhir, kredit berbayar butuh persetujuan pemilik, dan pesan antarbot tetap singkat.

Skill itu sendiri (`SKILL.md`) dan bagian lain repositori ditulis dalam bahasa Inggris. Hanya README ini yang diterjemahkan: 14 terjemahan ditambah versi asli bahasa Inggris.

## Instalasi

1. **Paling mudah:** di chat Grok Bot, minta bot menyimpannya sebagai skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manual:** salin seluruh `SKILL.md` (termasuk frontmatter) ke editor skill bot, atau tempel di chat lalu minta disimpan sebagai skill.
3. **Agen yang membaca folder skill** (gaya Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Lalu panggil dengan `/grokbot-economy` atau sebut dalam rutinitas. Deskripsinya membuat bot memuatnya di awal setiap tugas, sebelum membuka browser, sebelum mengulang tugas, dan saat mengirim pesan ke bot lain.

## Prinsip

| # | Jalur | Gunakan untuk |
|---|---|---|
| 1 | Script/CLI | apa pun yang sudah punya skrip |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | resep siap pakai dari pihak ketiga |
| 4 | API | layanan tanpa konektor |
| 5 | `browse` CLI (text/DOM) | situs tanpa API, dibaca sebagai teks |
| 6 | Computer use (screenshots) | hanya login (manusia menyelesaikan 2FA), pengecualian, UI tanpa API atau DOM yang bisa diskrip; captcha/blokir anti-bot → berhenti dan serahkan ke manusia, atau gunakan API resmi |

- **LLM merencanakan; kode mengeksekusi.** Tugas yang muncul dua kali menjadi skrip dengan `--dry-run`, idempoten, dan tes.
- **Checklist sebelum browser:** skrip? konektor? plugin? API? bisakah `browse` melakukannya lewat teks?
- **Batch lewat CSV/JSON + skrip**, jangan pernah per kolom di UI; laporkan hanya yang gagal.
- **Membaca dengan hemat:** `rg` + baca dengan offset/limit, tanpa dump file utuh, tanpa membaca ulang, tanpa loop sleep/polling.
- **Pengaman biaya:** jangan pernah memakai kredit berbayar (TTS melebihi kuota, kredit clipping, iklan) tanpa persetujuan eksplisit pemilik; patuhi file kunci kuota.
- **Edit file dengan aman:** dry-run, uji pada salinan, backup + tukar atomik, lock, diff kecil.
- **Instagram/WhatsApp:** API resmi dulu; jika tidak ada, pengiriman konservatif dengan ritme manusia dan disetujui manusia; tanpa alat penghindar anti-bot; berhenti pada peringatan pertama.
- **Pesan antarbot:** singkat, menunjuk path file, item digabung, tanpa pesan yang hanya berisi «ok».
- **Model sesuai ukuran:** usaha rendah untuk pekerjaan mekanis, tinggi hanya untuk penilaian; pekerjaan panjang di latar belakang.

## Isi repositori

| File | Isi |
|---|---|
| [`SKILL.md`](../SKILL.md) | Skill: tangga biaya, checklist, opsi alat browser, anti-pola, diagram keputusan, aturan pemeliharaan |
| [`CHANGELOG.md`](../CHANGELOG.md) | Setiap perubahan skill, dengan alasan dan perkiraan penghematan |
| [`examples/flows.md`](../examples/flows.md) | Alur konkret: spreadsheet, Drive, papan koordinasi, video, batch, pengiriman |
| [`checklists/`](../checklists/) | Sebelum browser, skrip baru, pengiriman Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only token/biaya per tugas (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Templat metrik (header CSV + contoh) |
| [`tests/`](../tests/) | Tes unit untuk logger |
| [`assets/banner.png`](../assets/banner.png) | Banner README |

## Ukur

Catat token/biaya per tugas dan jalur yang dipakai. Jika `browse` atau `computer-use` mendominasi ringkasan, ada skrip yang belum dibuat.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Berkontribusi

- Menemukan jalur yang lebih murah (skrip baru, konektor, API, plugin, flag CLI)? Buka PR yang mengubah `SKILL.md` **dan** tambahkan satu baris ke `CHANGELOG.md` (tanggal, apa, mengapa, perkiraan penghematan). Ini aturan permanen untuk semua bot.
- Jaga `SKILL.md` tetap singkat (< ~250 baris), imperatif, dan dalam bahasa Inggris.
- **Repo publik:** tanpa token, kunci, email, nomor telepon, nama klien, ID file, hostname, atau URL internal. Gunakan placeholder seperti `<DRIVE_FILE_ID>`.
- Jalankan selftest dan tes unit sebelum membuka PR.

## Lisensi

MIT. Lihat [LICENSE](../LICENSE).
