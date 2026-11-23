---
title: Cadência: o que roda sozinho
created: 2026-11-23
updated: 2026-11-23
type: summary
tags: [cadencia, automacao, processo]
sources: [raw/articles/cole-4cs-segundo-cerebro.md]
confidence: high
---
# Cadência (o quarto C)

Tarefas agendadas no Hermes (ver `cronjob list`). Regra: **nada de relatório longo sem decisão no fim**.

| Quando | O que | Tipo |
|---|---|---|
| A cada 6 h | Renova o token do KAIROGEN; só avisa se falhar | script, sem LLM |
| Segunda 8h | Panorama da semana: Asana (projetos vermelhos/amarelos, atrasos), propostas sem resposta, 3 prioridades | agente |
| Sexta 17h | Fecho da semana: decisões e lições da semana vão para a wiki; propõe ajustes ao plano | agente |
| Sexta 16h | Lint da wiki; só avisa se achar problema | script, sem LLM |

Entrega: no chat do desktop (padrão). O Telegram parece pronto, falta o envio de teste para trocar a entrega ([[hermes-no-vault]]). Quem decide ajustar horários é o Adleniel.
Relacionado: [[segundo-cerebro-4cs]], [[roteiro-de-implantacao]].
