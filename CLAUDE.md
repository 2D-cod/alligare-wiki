# Regras para qualquer agente de IA que ler este vault

Este vault (`AlligareWiki`) é a memória compartilhada de Adleniel (Alligare). Pode ser aberto por
Hermes, Claude Code, Gemini CLI, Abacus AI (Desktop/CLI) ou qualquer outro agente com acesso a
arquivos. Todos devem seguir as mesmas regras, para a base não virar bagunça.

## Antes de fazer qualquer coisa (toda sessão)
1. Leia `SCHEMA.md` (convenções, taxonomia de tags).
2. Leia `index.md` (catálogo de todas as páginas, uma linha cada).
3. Leia as últimas ~30 linhas de `log.md` (o que mudou recentemente).
Só depois disso, leia, crie ou edite páginas.

## Estrutura
- `raw/` = fontes imutáveis (nunca editar).
- `entities/`, `concepts/`, `comparisons/`, `queries/`, `ops/` = páginas da wiki (markdown,
  frontmatter YAML, mínimo 2 `[[wikilinks]]` por página, tags só da taxonomia do SCHEMA.md).
- Toda página nova entra em `index.md`. Toda ação (ingest, update, query, lint) entra em `log.md`.

## Regras que NINGUÉM pode quebrar
- **Nunca** gravar senhas, tokens, chaves de API ou credenciais de clientes neste vault.
- Números financeiros (receita, margem, caixa, dívidas) que não vêm do dossiê (`/opt/data/MEMORY.md`,
  fora deste vault) entram marcados `[A VALIDAR]`, nunca como fato.
- Não enviar nada deste vault para serviços de terceiros sem necessidade clara (ele tem dados de
  clientes e do negócio da Alligare).
- Idioma: português do Brasil, com acentos.
- Se duas fontes contradizem, registre as duas com data, não sobrescreva em silêncio.

## Escrevendo
- Siga o formato do `SCHEMA.md` (frontmatter completo: title, created, updated, type, tags, sources,
  confidence).
- Rode `python3 _meta/lint.py` depois de editar, se o seu ambiente tiver Python disponível. Ele
  aponta links quebrados, páginas órfãs, tags fora da taxonomia, etc.
- Um ingest que tocaria 10+ páginas existentes: confirme com o usuário antes.

## Convivência entre vários agentes
Este vault sincroniza por Git com `github.com/2D-cod/alligare-wiki`. Se outro agente (ou o próprio
Adleniel no Obsidian) está editando ao mesmo tempo, pode dar conflito de merge. Prefira: puxar
(`git pull`) antes de editar, e enviar (`git commit` + `push`) logo depois de uma edição, em vez de
deixar mudanças acumulando sem enviar.

Referência completa do padrão: skill `llm-wiki` (Hermes) / gist de Andrej Karpathy sobre LLM wikis.
