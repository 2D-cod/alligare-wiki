---
source_url: https://openrouter.ai/docs/guides/features/decisions
ingested: 2026-11-23
sha256: b76be481465cd6649d1ae9b190a4af38edce96ad036542154db701d01337fa5c
note: resumo de snippets de busca
---
Resumo de resultados de busca (não a página completa) sobre a Decisions API do OpenRouter, 2026-11-23.

Endpoint POST /api/alpha/decisions (também servido como POST /api/v1/systemone para o SDK da TypeSafe). Consulta modelos System One com um estado e perguntas tipadas (choice, noul, score, box), com probabilidades. Modelos citados: typesafe/jev-1.14 (e ~typesafe/jev-latest; texto e imagem), Cloudflare Clef, Inception Mercury Decide, Liquid D1 (liquid/d1), openai/gpt-6-luna-decisions, perplexity/pplx-decider-v1.2, parallel/decisions-fast (com consulta à web). Preços listados por 1M tokens de entrada (artigo da Parallel, 06/11/2026): Jev US$0,042; Liquid D1 US$0,02; OpenAI luna US$0,10; Perplexity US$0,02. Lista viva: GET https://openrouter.ai/api/v1/models?output_modalities=decisions. Usa a chave do OpenRouter.
