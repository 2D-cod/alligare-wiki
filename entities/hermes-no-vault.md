---
title: Hermes e as conexões do vault
created: 2026-11-23
updated: 2026-11-23
type: entity
tags: [hermes, ferramenta, second-brain]
sources: [raw/articles/dossie-alligare-2026-11.md]
confidence: high
---
# Hermes: conexões e estado

Hermes Agent no desktop do Adleniel, perfil `default`. Conexões em 2026-11-23:
- **Asana** (conector, workspace alligare.co): funcionando; 96 projetos em aberto no primeiro levantamento.
- **KAIROGEN MCP** (device flow): funcionando; token em `/opt/data/credentials/kairogen/`, renovação automática via [[cadencia-semanal]] e skill `kairogen-conexao`.
- **Telegram**: bot e usuário permitido estão no `.env`; `hermes send -l` lista o DM (`telegram:Aj`). Envio de teste ainda não feito e canal "home" não definido.
- **Strava**: OAuth próprio, escopo só `read`.
- Skills: `obsidian`, `llm-wiki`, `pdf`, `alligare-dossie`, `alligare-wiki`, entre outras.
Memória curta (2.200 caracteres) aponta para `/opt/data/MEMORY.md` e para esta wiki. Ver [[segundo-cerebro-4cs]].
