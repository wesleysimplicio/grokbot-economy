<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>Uma skill permanente que faz todo Grok Bot trabalhar por caminhos prontos e determinísticos e parar de queimar tokens.</strong><br />
  <em>Os comandos ficam em inglês para poder copiar exatamente.</em>
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
  <img src="../assets/banner.png" alt="Escada de custo abstrata: passos baratos por script à esquerda, computer use caro à direita" width="860" />
</p>

---

## Resumo

`grokbot-economy` é uma skill para o Grok Bot, um assistente de desktop com LLM que tem shell, leitura de arquivos, conectores MCP, plugins, um navegador no box, o `browse` CLI e subagentes de computer use guiados por screenshots. Ela manda o bot **planejar, revisar e tratar exceções com o LLM, e executar com código**: trabalho repetido vira script, lotes passam por CSV/JSON, o navegador é o último recurso, crédito pago exige OK do dono e mensagens entre bots são curtas.

A skill em si (`SKILL.md`) e o resto do repositório estão em inglês. Só este README é traduzido, para 15 idiomas.

## Instalação

1. **Mais fácil:** num chat do Grok Bot, peça para salvar como skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manual:** copie todo o `SKILL.md` (com o frontmatter) para o editor de skills do bot, ou cole no chat e peça para salvar como skill.
3. **Agentes que leem pastas de skills** (estilo Cursor/Claude):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Depois, chame com `/grokbot-economy` ou cite em rotinas. A descrição faz os bots carregarem a skill no início de qualquer tarefa, antes de abrir o navegador, antes de repetir uma tarefa e ao mandar mensagem para outros bots.

## Princípios

| # | Caminho | Use para |
|---|---|---|
| 1 | Script/CLI | tudo que já tem script |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | receitas prontas de terceiros |
| 4 | API | serviços sem conector |
| 5 | `browse` CLI (text/DOM) | sites sem API, lidos como texto |
| 6 | Computer use (screenshots) | só login (um humano conclui o 2FA), exceções, UIs sem API nem DOM automatizável; captcha/bloqueio anti-bot → pare e passe para um humano, ou use a API oficial |

- **O LLM planeja; o código executa.** Tarefa vista 2 vezes vira script com `--dry-run`, idempotência e teste.
- **Checklist antes do navegador:** script? conector? plugin? API? o `browse` resolve por texto?
- **Lotes por CSV/JSON + script**, nunca campo a campo numa UI; relate só as falhas.
- **Leitura barata:** `rg` + leitura com offset/limit, sem despejar arquivos inteiros, sem reler, sem loops de sleep/polling.
- **Guardas de dinheiro:** nunca gaste crédito pago (TTS além da cota, créditos de clipping, anúncios) sem OK explícito do dono; respeite os arquivos de trava de cota.
- **Edição segura de arquivos:** dry-run, teste em cópia, backup + troca atômica, locks, diffs pequenos.
- **Instagram/WhatsApp:** API oficial primeiro; senão envios conservadores, em ritmo humano e aprovados por humano; sem ferramentas de evasão anti-bot; pare no primeiro aviso.
- **Mensagens entre bots:** curtas, apontando caminhos de arquivo, itens agrupados, sem mensagens só de ok.
- **Modelo do tamanho certo:** esforço baixo para trabalho mecânico, alto só para julgamento; trabalhos longos em background.

## Conteúdo do repositório

| Arquivo | O quê |
|---|---|
| [`SKILL.md`](../SKILL.md) | A skill: escada de custo, checklists, ferramentas de navegador, anti-padrões, fluxograma de decisão, regra de manutenção |
| [`CHANGELOG.md`](../CHANGELOG.md) | Toda mudança na skill, com motivo e economia estimada |
| [`examples/flows.md`](../examples/flows.md) | Fluxos concretos: planilha, Drive, board de coordenação, vídeos, lotes, envios |
| [`checklists/`](../checklists/) | Antes do navegador, script novo, envio por Instagram/WhatsApp |
| [`scripts/token_log.py`](../scripts/token_log.py) | Logger append-only de tokens/custo por tarefa (stdlib, `--selftest`) |
| [`templates/token-log.csv`](../templates/token-log.csv) | Modelo da métrica (cabeçalho CSV + exemplos) |
| [`tests/`](../tests/) | Testes unitários do logger |
| [`assets/banner.png`](../assets/banner.png) | Banner do README |

## Meça

Registre tokens/custo por tarefa e o caminho usado. Se `browse` ou `computer-use` dominam o resumo, falta um script.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Como contribuir

- Achou um caminho mais barato (script novo, conector, API, plugin, flag de CLI)? Abra um PR mudando o `SKILL.md` **e** adicione uma linha no `CHANGELOG.md` (data, o quê, por quê, economia estimada). É regra permanente para todos os bots.
- Mantenha o `SKILL.md` curto (< ~250 linhas), imperativo e em inglês.
- **Repo público:** nada de tokens, chaves, e-mails, telefones, nomes de clientes, IDs de arquivo, hostnames ou URLs internas. Use placeholders como `<DRIVE_FILE_ID>`.
- Rode o selftest e os testes unitários antes de abrir o PR.

## Licença

MIT. Veja [LICENSE](../LICENSE).
