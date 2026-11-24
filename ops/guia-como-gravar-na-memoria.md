---
title: Guia rápido: como gravar na memória central (3 níveis)
created: 2026-11-24
updated: 2026-11-24
type: summary
tags: [wiki, processos, segundo-brain, hermes, obsidian]
sources:
confidence: high
---

# Guia rápido: como gravar na memória central

A memória de Adleniel (Alligare) vive neste vault (`AlligareWiki`), sincronizado entre o
servidor (Hermes), o PC e o celular. Qualquer conteúdo que você queira que "todo mundo saiba"
precisa entrar **aqui** — os apps de chat (Claude, Gemini, Abacus) não enviam nada sozinhos.

## O que você fala, em cada situação

### 1. No navegador / celular / "na rua" (qualquer app)
O app de chat do navegador **não grava na pasta sozinho**. Você cola o resultado:

> "Me devolve isso em um parágrafo pra eu colar no Obsidian."

Depois cola na nota, salva → o Obsidian Sync entrega ao servidor → o Hermes lê e usa.

### 2. Claude Desktop no seu PC
O Claude Desktop lê a pasta local `C:\Obsidian\AlligareWiki` e respeita o `CLAUDE.md`. Você pode
pedir direto:

> "Salve um resumo desta conversa numa nota dentro da pasta AlligareWiki."

Ele grava no arquivo e o Sync propaga. (Só funciona com o PC ligado.)

### 3. Claude Code / Gemini CLI no computador
Rode o terminal dentro de `C:\Obsidian\AlligareWiki` + digite `claude` ou `gemini`. Eles leem o
`CLAUDE.md`/`GEMINI.md` e trabalham nos arquivos de verdade.

## O que NÃO funciona (não perca tempo tentando)
- Fazer o Claude/Gemini/Abacus do navegador "gravarem direto na pasta" — só o app de desktop local faz isso.
- Esperar que qualquer app envie automaticamente para a wiki — o elo manual (colar) fecha o ciclo.

## Regra de ouro
Se é importante para a Alligare → vai para o Obsidian (PC ou celular). Sem isso, o Hermes não
"descobre" automaticamente entre conversas. Veja também [[segundo-cerebro-4cs]] e
[[roteiro-de-implantacao]].
