# Checklist: antes de abrir o navegador

Responda em ordem. O primeiro "sim" encerra a checklist: use esse caminho.

- [ ] **Script/CLI pronto?** `ls /workspace/controle/scripts` · `rg -l '<tarefa>' /workspace/controle` · `<cli> --help`
- [ ] **Conector MCP?** Liste as tools do servidor (Drive, Gmail, GitHub, Calendar...) e use a que resolve.
- [ ] **Plugin/skill?** `browse skills find <domínio>` ou skills instaladas.
- [ ] **API direta?** `gh api`, REST do serviço, `UploadFile` / `DownloadFile`.
- [ ] **browse CLI por texto?** `browse open <url> --session <tarefa>` → `browse snapshot` / `browse get text body`.
- [ ] **Só sobrou computer use?** Escreva o objetivo fechado ("faça login e pare"), limite de prints e o ponto de devolução ao script.

Depois: registre o caminho usado com `scripts/token_log.py add ...`.
Se você fez isso à mão pela 2ª vez → regra "vira script" (SKILL.md §3).
