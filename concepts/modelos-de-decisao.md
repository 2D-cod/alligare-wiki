---
title: Modelos de decisão (System 1)
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [agentes, custos, seguranca, automacao]
sources: [raw/transcripts/cole-modelo-decisao-ai-coding.md, raw/transcripts/cole-modelo-decisao-segundo-cerebro.md, raw/articles/openrouter-decisions-api.md]
confidence: medium
---
# Modelos de decisão ("System 1")

Modelo **TypeSafe Jev** (nome confirmado na documentação do OpenRouter, 2026-11-23). Outros modelos de decisão no mesmo endpoint: Cloudflare Clef, Inception Mercury Decide, Liquid D1, OpenAI, Perplexity, Parallel. Endpoint: `POST /api/alpha/decisions`. Conceito: não gera texto; recebe um estado e várias perguntas de múltipla escolha e responde todas em paralelo com probabilidades.
Alegação do autor: 20 a 200x mais rápido e 40 a 1000x mais barato que um LLM para decidir. Acessado pelo endpoint "decisions" do OpenRouter. [dados do autor, não verificados]

Usos que ele aplica:
- **Guardrail de segurança** em hook pre-tool-use: bloqueia ler `.env`, apagar pastas, exfiltrar dados, sair do foco. Ver [[guardrails-para-agentes]].
- **Filtro de entrada:** detectar prompt injection em e-mails e decidir se vale responder; filtrar notícias; detectar duplicatas.
- **Classificação de fluxo:** tipo de tarefa (bug ou feature) e nível de modelo necessário.
- **Testes** de jogo e de navegador.

Limites: não substitui o LLM quando a decisão exige muito contexto (ele manda o caso incerto para um LLM menor). Padrão: **sanduíche**, LLM antes e depois, decisão no meio.
Relevância Alligare: triagem de e-mails de leads e fornecedores, classificação de pedidos de orçamento. Só vale testar com volume; hoje é ideia, não plano ([[roteiro-de-implantacao]]).
