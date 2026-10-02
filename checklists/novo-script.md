# Checklist: transformar tarefa repetida em script

- [ ] A tarefa já apareceu 2+ vezes (ou vai se repetir num lote).
- [ ] Existe script parecido para **estender**? (`rg -l` antes de criar outro)
- [ ] Entrada por CSV/JSON ou argumentos; nada de digitação em UI.
- [ ] `--help` com exemplo de uso em 1–3 linhas.
- [ ] `--dry-run` em tudo que escreve.
- [ ] Idempotente: rodar 2× não duplica (confere antes de agir).
- [ ] Backup + escrita em temporário + troca atômica para arquivos vivos.
- [ ] Respeita travas de cota e locks; nunca gasta crédito pago sem OK do dono.
- [ ] Saída curta: resumo + só as falhas.
- [ ] `--selftest` ou teste em `tests/`, rodado e passando.
- [ ] Sem segredos no código (lê de env var; nunca imprime).
- [ ] Documentado no runbook (comando + quando usar) e, se ficou mais barato, PR nesta skill + `CHANGELOG.md`.
