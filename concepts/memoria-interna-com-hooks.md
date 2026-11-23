---
title: Memória que evolui com a conversa (hooks)
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [memoria, agentes, automacao]
sources: [raw/transcripts/cole-memoria-claude-code-llm-kb.md]
confidence: medium
---
# Memória interna com hooks

Variante do [[padrao-llm-wiki]] para **dados internos**: em vez de artigos da internet, a fonte são as conversas com o agente.
- Hooks de início de sessão carregam `AGENTS.md` e o `index.md` da base.
- Hooks de fim de sessão e de compactação enviam a conversa a outro LLM que gera resumo (decisões, lições, pendências) e grava no log diário (o "raw").
- Uma vez por dia, um processo extrai conceitos e conexões dos logs para a wiki. Respostas boas são arquivadas, então a base cresce sozinha.
- Resultado citado: pergunta que exigiria vasculhar o código foi respondida em ~10 s pela base.

Adaptação para o Hermes (sem hooks do Claude Code): usar o diário de sessão em [[cadencia-semanal]] (job "fecho da semana": resume decisões e lições e arquiva na wiki) e a regra de registrar decisões em `log.md`. O Hermes já tem memória própria, curta; o volume vive aqui.
