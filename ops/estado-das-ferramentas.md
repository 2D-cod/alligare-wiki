---
title: Estado das ferramentas (inventário)
created: 2026-11-23
updated: 2026-11-23
type: summary
tags: [ferramenta, hermes, processo]
sources: [raw/articles/dossie-alligare-2026-11.md]
confidence: high
---
# Estado das ferramentas (verificado em 2026-11-23)

| Ferramenta | Estado | Observação |
|---|---|---|
| Hermes (perfil default) | ativo | modelo principal `claude-sonnet-5-5` via provedor Abacus (RouteLLM) |
| Skills `llm-wiki`, `alligare-wiki`, `alligare-dossie`, `obsidian`, `pdf`, `kairogen-conexao` | instaladas | ver [[padrao-llm-wiki]] |
| Asana | conectado | conector, workspace alligare.co |
| KAIROGEN | conectado | MCP nativo (OAuth) no config + token manual em `/opt/data/credentials/kairogen/` |
| Strava | desativado | MCP existe no config com `enabled: false`; escopo só `read` |
| Telegram | provável | bot e usuário no `.env`, DM listado; teste de envio pendente |
| Claude Code CLI | instalado | v2.1.323, npm global |
| **Jev (modelo de decisão)** | **não integrado** | `jev-latest` e `gemini-decision-1` aparecem na lista de modelos do provedor Abacus; não verificado se respondem; sem chave OpenRouter no `.env`; nenhum hook usa. Ver [[modelos-de-decisao]] |
| **OmniRoute** | **não instalado** | sem binário, config ou chave; só skills de CLI no catálogo |
| n8n | não instalado | skills no catálogo |
| Paperclip | não instalado | ver [[meta-harness-empresa-de-agentes]] |
| Obsidian (app) e `ob` headless | não instalados no servidor | o vault `/opt/data/wiki` está pronto para abrir no PC |
| Codex, Gemini CLI, opencode | não instalados | |

Decisões ligadas: [[roteiro-de-implantacao]].
