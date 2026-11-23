---
title: Skills como lições codificadas
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [skills, processo, agentes]
sources: [raw/transcripts/cole-skill-edicao-de-video.md]
confidence: medium
---
# Skills como lições codificadas

Caso: skill de edição de vídeo do Cole. O agente sozinho chega a ~90%; os 10% finais são caros. A skill fecha essa lacuna.
Estrutura que funcionou:
- Tabela no topo que escolhe os passos conforme o tipo de entrega (cada tipo de conteúdo é uma composição de passos reutilizáveis).
- **Scripts determinísticos** como auxiliares (transcrição, cortes, validação que re-transcreve e compara palavra por palavra) devolvendo dados ao agente orquestrador.
- Arquivo de **lições** em linguagem natural: tudo que deu errado entra lá, e a skill melhora a cada uso.
- Regras duras curtas; arquivo de marca (cores) para personalizar.
- Autoiteração: o agente detecta e corrige o próprio erro (corte no meio de frase, transições).
- Pipeline completa opcional com modelos multimodais (ouvir, assistir, gerar imagem, clonar voz) a custo baixo (~US$2,71 por vídeo longo, segundo o autor).

Para a Alligare: copiar o desenho para a skill de proposta (3 linhas) e a de relatório de obra, cada uma com `lessons.md`. Ver [[alligare-skills-planejadas]] e [[precificacao-alligare]].
