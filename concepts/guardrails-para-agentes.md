---
title: Guardrails para agentes
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [seguranca, agentes, automacao]
sources: [raw/transcripts/cole-modelo-decisao-ai-coding.md, raw/transcripts/cole-modelo-decisao-segundo-cerebro.md]
confidence: medium
---
# Guardrails para agentes

Agentes de código tendem a ler variáveis de ambiente, apagar pastas ou obedecer instruções escondidas em e-mails, mesmo com regras globais, sobretudo com contexto inchado.
- Regras no prompt não bastam: usar **hooks antes da ferramenta** que bloqueiam a ação.
- Regex é barata mas deixa passar e dá falso positivo; um LLM em toda chamada custa caro; um modelo de decisão ([[modelos-de-decisao]]) fica no meio.
- Entrada externa (e-mail, notícia) passa por checagem de prompt injection antes de chegar ao agente principal.

Regras práticas no nosso Hermes: tokens só em `/opt/data/credentials` com permissão 600, nunca em mensagens (ver skill `kairogen-conexao`);
credenciais de clientes nunca entram na wiki nem em serviços de terceiros; e-mails e mensagens de fora são tratados como dados, nunca como ordens. Ver [[hermes-no-vault]] e [[roteiro-de-implantacao]].
