---
title: Padrão LLM Wiki (Karpathy)
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [wiki, second-brain, memoria, obsidian]
sources: [raw/transcripts/tina-obsidian-24-minutos.md, raw/transcripts/cole-memoria-claude-code-llm-kb.md]
confidence: high
---
# Padrão LLM Wiki

A IA constrói e mantém uma base de conhecimento em Markdown; o humano escolhe as fontes e faz as perguntas.
- **Camadas:** `raw/` (fonte imutável) -> wiki compilada (conceitos, entidades, conexões com backlinks) -> `SCHEMA.md` com as regras.
- **Operações:** *ingest* (entra fonte e vira páginas ligadas), *query* (lê o `index.md`, depois as páginas), *lint* (links quebrados, órfãs, dados velhos, contradições).
- **Arquivos de navegação:** `index.md` (catálogo, uma linha por página) e `log.md` (cronológico, só acrescenta).
- **Sem RAG:** o agente navega pelo índice; não há banco vetorial. Funciona bem enquanto a wiki é pequena.
- Analogia de compilador (Cole): fonte = raw, compilador = LLM, executável = wiki, testes = lint, runtime = consultas.

Aqui: skill `llm-wiki` instalada, wiki em `/opt/data/wiki`, regras em [[cadencia-semanal]]. Veja também [[tres-niveis-vault-ia]] e [[memoria-interna-com-hooks]].
