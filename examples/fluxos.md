# Exemplos de fluxos econômicos

Comandos reais do nosso fluxo, com placeholders no lugar de dados sensíveis.
Antes de usar, confira `--help`: as flags podem ter mudado. Se mudaram, atualize este arquivo (SKILL.md §18).

## 1. Planilha de controle (`fila.py`)

❌ Caro: abrir a planilha no navegador, rolar, achar a linha, editar célula por célula, tirar prints.

✅ Barato:
```bash
F=/workspace/controle/scripts/fila.py
python3 $F proximo --pais <PAIS> --todos        # próximo item acionável e por que os outros estão fechados
python3 $F lock P0XX --agente "<bot>"
python3 $F ver P0XX                             # só a linha que interessa
python3 $F marcar P0XX --status "<novo status>" --obs "<1 linha>" --agente "<bot>"   # faz backup sozinho
python3 $F unlock P0XX
```
Quando existir `registrar.py`, use-o para gravar planilha + board numa chamada só.

## 2. Drive (`gapi.py` / conector MCP)

❌ Caro: Drive web, arrastar arquivo, conferir pasta com prints.

✅ Barato:
- Conferir se já existe (idempotência): busca do conector Drive com `parentId = '<DRIVE_FOLDER_ID>' and title contains 'P0XX'`.
- Subir arquivo **novo**: `UploadFile` (connection Drive, `destination.folderId = <DRIVE_FOLDER_ID>`) ou `gapi.py` (OAuth) quando existir.
- Baixar: `DownloadFile` com `<DRIVE_FILE_ID>`.
- Nova **versão** do mesmo arquivo (ex.: a planilha mestre): siga o procedimento do runbook; não crie um arquivo duplicado.

## 3. Board de coordenação (Paperclip, `pc.py`)

❌ Caro: abrir a UI, ler o card inteiro, colar log no comentário.

✅ Barato: `pc.py` para ler os **últimos N** comentários e postar **um** comentário curto:
`[<Projeto>/<PAIS>] P0XX: <o que mudou> · próximo: <passo> · prova: <caminho>`. Logs vão para arquivo; o comentário leva o caminho.

## 4. Vídeos (`simplicio-video` + `FINAL-COMANDO.md`)

❌ Caro: um LLM por vídeo, montar comando de render de cabeça, assistir o vídeo várias vezes.

✅ Barato:
```bash
simplicio-video validate <contrato.yaml>
simplicio-video voice    <contrato.yaml>     # cache por hash: fala já gerada não chama a API
simplicio-video render   <contrato.yaml>     # backend local, sem custo
bash /workspace/controle/scripts/qa_v2.sh <pasta-do-prospect>   # QA objetivo + 1 olhada no contact sheet
```
Final sem marca d'água: rode **exatamente** o comando que está em `<pasta-do-prospect>/FINAL-COMANDO.md`.
Se o arquivo tiver aviso de "NÃO ENTREGAR", não renderize nem envie.

## 5. Lote de prospects

```text
lista.csv ──> lote fichas ──> lote voz ──> lote visual + render ──> relatório só de falhas
```
- Um CSV de entrada, um script por etapa, cada etapa idempotente.
- `lote voz` respeita a trava de cota (`tts-bloqueado-ate.txt`) e para no primeiro 429.
- Relatório: `37/40 ok · falhas: P0XX voz 429 (retoma HH:MM), P0YY render: asset faltando`.

## 6. Envios (Gmail, Instagram DM, WhatsApp Web)

Pré-requisito sempre: **OK humano do dono para aquele vídeo** + texto de modelo aprovado.

| Canal | Caminho | Observações |
|---|---|---|
| Gmail | conector MCP/API: rascunho → aprovação → envio | nunca pelo navegador |
| WhatsApp | API oficial (WhatsApp Business Platform / Cloud API) se a conta tiver; senão `browse` na sessão já logada | ritmo humano, teto diário, para no primeiro aviso |
| Instagram DM | API oficial (Instagram Messaging API) se a conta for elegível; senão `browse` na sessão já logada | idem; computer use só para login/challenge, e aí entrega a um humano |

Primeira mensagem (exemplo de modelo): `Your video is ready, here's the preview.` + o mp4 (não link).
Um único lembrete em D+3. Nunca preço em mensagem proativa.

**Risco honesto:** automação de IG/WA pode bloquear a conta do dono. Por isso: um envio por vez, aprovação humana de cada um, sem evasão anti-bot, sem massa, e parar no primeiro aviso.

## 7. Mensagem entre bots

❌ "Oi! Tudo bem? Então, como conversamos antes, o contexto é o seguinte... (40 linhas)"

✅ `[Videos/<PAIS>] P0XX render ok, QA ok · preciso: OK do dono para envio · prévia: <caminho> · prioridade: sim (envio às HH:MM)`
