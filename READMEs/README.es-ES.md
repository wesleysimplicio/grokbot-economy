<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Una skill permanente que hace que cada Grok Bot trabaje por caminos listos y deterministas y deje de quemar tokens.</strong><br />
  <em>Los comandos se quedan en inglés para poder copiarlos exactamente.</em>
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
  <img src="../assets/banner.png" alt="Escalera de coste abstracta: pasos baratos por script a la izquierda, computer use caro a la derecha" width="860" />
</p>

---

## En resumen

`grokbot-economy` es una skill para Grok Bot, un asistente de escritorio con LLM que tiene shell, lectura de archivos, conectores MCP, plugins, un navegador en el box, el CLI `browse` y subagentes de computer use guiados por capturas de pantalla. Le indica al bot **planificar, revisar y gestionar excepciones con el LLM, y ejecutar con código**: el trabajo repetido se convierte en script, los lotes pasan por CSV/JSON, el navegador es el último recurso, los créditos de pago necesitan el OK del dueño y los mensajes entre bots son breves.

La skill en sí (`SKILL.md`) está escrita en portugués de Brasil, el idioma de trabajo del equipo. Este README está disponible en 15 idiomas.

## Instalación

1. **Lo más fácil:** en un chat de Grok Bot, pide que la guarde como skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manual:** copia todo `SKILL.md` (con el frontmatter) en el editor de skills del bot, o pégalo en el chat y pide que lo guarde como skill.
3. **Agentes que leen carpetas de skills** (estilo Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Después, invócala con `/grokbot-economy` o menciónala en rutinas. Su descripción hace que los bots la carguen al empezar cualquier tarea, antes de abrir el navegador, antes de repetir una tarea y al escribir a otros bots.

## Principios

| # | Camino | Úsalo para |
|---|---|---|
| 1 | Script/CLI | todo lo que ya tiene script |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | recetas listas de terceros |
| 4 | API | servicios sin conector |
| 5 | `browse` CLI (text/DOM) | sitios sin API, leídos como texto |
| 6 | Computer use (screenshots) | solo inicio de sesión, 2FA, captcha, excepciones, sitios que bloquean la automatización |

- **El LLM planifica; el código ejecuta.** Una tarea vista dos veces se convierte en script con `--dry-run`, idempotencia y test.
- **Checklist antes del navegador:** ¿script? ¿conector? ¿plugin? ¿API? ¿lo resuelve `browse` por texto?
- **Lotes con CSV/JSON + script**, nunca campo a campo en una UI; informa solo de los fallos.
- **Lectura barata:** `rg` + lecturas con offset/limit, sin volcar archivos enteros, sin releer, sin bucles de sleep/polling.
- **Límites de gasto:** nunca gastes créditos de pago (TTS por encima de la cuota, créditos de clipping, anuncios) sin el OK explícito del dueño; respeta los archivos de bloqueo de cuota.
- **Edición segura de archivos:** dry-run, pruebas en copias, backup + cambio atómico, locks, diffs pequeños.
- **Instagram/WhatsApp:** primero la API oficial; si no, envíos conservadores, a ritmo humano y aprobados por una persona; sin herramientas de evasión anti-bot; para en el primer aviso.
- **Mensajes entre bots:** breves, apuntando a rutas de archivo, agrupando ítems, sin mensajes de solo «ok».
- **Modelo del tamaño justo:** esfuerzo bajo para trabajo mecánico, alto solo para decisiones de criterio; trabajos largos en segundo plano.

## Contenido del repositorio

| Archivo | Qué es |
|---|---|
| [`SKILL.md`](../SKILL.md) | La skill (PT-BR): escalera de coste, checklists, herramientas de navegador, antipatrones, diagrama de decisión, regla de mantenimiento |
| [`CHANGELOG.md`](../CHANGELOG.md) | Cada cambio en la skill, con el motivo y el ahorro estimado |
| [`examples/fluxos.md`](../examples/fluxos.md) | Flujos concretos: hoja de cálculo, Drive, tablero de coordinación, vídeos, lotes, envíos |
| [`checklists/`](../checklists/) | Antes del navegador, script nuevo, envío por Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only de tokens/coste por tarea (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Plantilla de la métrica (cabecera CSV + ejemplos) |
| [`tests/`](../tests/) | Tests unitarios del logger |
| [`assets/banner.png`](../assets/banner.png) | Banner del README |

## Mídelo

Registra tokens/coste por tarea y el camino usado. Si `browse` o `computer-use` dominan el resumen, falta un script.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Contribuir

- ¿Encontraste un camino más barato (script nuevo, conector, API, plugin, flag de CLI)? Abre un PR que cambie `SKILL.md` **y** añade una línea a `CHANGELOG.md` (fecha, qué, por qué, ahorro estimado). Es una regla permanente para todos los bots.
- Mantén `SKILL.md` corto (< ~250 líneas), imperativo y en PT-BR.
- **Repo público:** nada de tokens, claves, correos, teléfonos, nombres de clientes, IDs de archivos, hostnames ni URLs internas. Usa placeholders como `<DRIVE_FILE_ID>`.
- Ejecuta el selftest y los tests unitarios antes de abrir el PR.

## Licencia

MIT. Consulta [LICENSE](../LICENSE).
