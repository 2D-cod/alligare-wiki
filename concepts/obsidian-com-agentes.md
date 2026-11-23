---
title: Agentes dentro do Obsidian
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [obsidian, agentes, ferramenta]
sources: [raw/transcripts/obsidian-herder-agentes-no-vault.md]
confidence: low
---
# Agentes dentro do Obsidian

Plugin de comunidade (nome ouvido: "Herder"/"obsidian herder", a confirmar) que roda agentes de terminal (Claude Code, Codex, Gemini, Hermes e outros) dentro de uma aba do Obsidian, com sessões persistentes, painel de controle e **log de auditoria com desfazer**. Um segundo plugin de "controle do Obsidian" (via MCP) deixa os agentes abrir painéis, criar notas e usar o Canvas.
Ideia central: vários agentes diferentes trabalham no **mesmo vault**, então o vault é a memória compartilhada ([[tres-niveis-vault-ia]]).
Testado pelo autor em Linux; Windows e Mac não confirmados. Riscos: dar "acesso total" a agentes; manter o vault sem credenciais ([[guardrails-para-agentes]]). Não instalado; só vale depois do vault sincronizado com o PC ([[roteiro-de-implantacao]]).
