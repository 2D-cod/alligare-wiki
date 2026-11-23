# Wiki Schema

## Domain
Segundo cérebro de Adleniel: (1) como operar a pilha de IA (Hermes, Obsidian, MCP, skills, cadência) e (2) conhecimento da Alligare
(empresa, precificação, clientes, recorrência, plano de negócios). Idioma: português do Brasil, com acentos. Termos técnicos podem ficar em inglês.

## Conventions
- Nomes de arquivo: minúsculas, hífens, sem espaços e sem acento (`segundo-cerebro-4cs.md`).
- Toda página tem frontmatter YAML (abaixo). `[[wikilinks]]` entre páginas, mínimo 2 links de saída por página.
- Ao editar uma página, atualizar `updated`. Toda página nova entra em `index.md`. Toda ação entra em `log.md`.
- `raw/` é imutável (fontes). Correções vão para as páginas da wiki, nunca para `raw/`.
- Afirmações de vídeos: dizer a fonte em `sources:`. Nomes ouvidos por STT e não confirmados vão marcados "(nome a confirmar)".
- Nunca gravar credenciais, senhas, tokens, nem dados de acesso de clientes. Valores financeiros pessoais só no dossiê.
- Números do negócio que não estão no dossiê levam `[A VALIDAR]`.

## Frontmatter
```yaml
---
title: Título
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [da taxonomia]
sources: [raw/transcripts/arquivo.md]
confidence: high | medium | low
---
```

## Tag Taxonomy
TAXONOMY: second-brain, wiki, memoria, agentes, skills, seguranca, automacao, cadencia, custos, obsidian, hermes, ferramenta, processo, alligare, clientes, precificacao, vendas, recorrencia, plano

## Page Thresholds
- Criar página quando algo aparece em 2+ fontes ou é central em uma. Menção passageira não vira página.
- Dividir páginas com mais de ~200 linhas. Arquivar o que foi superado em `_archive/`.

## Update Policy
Fonte mais nova vence a mais antiga. Se houver contradição real, registrar as duas posições com data e marcar `contradictions:`.
