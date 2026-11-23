---
title: Passo a passo: conectar o Obsidian ao Hermes
created: 2026-11-23
updated: 2026-11-23
type: summary
tags: [obsidian, processo, hermes]
sources: [raw/transcripts/wanderloots-hermes-obsidian-acesso.md, raw/transcripts/tina-obsidian-24-minutos.md]
confidence: medium
---
# Passo a passo: conectar o Obsidian ao Hermes

Objetivo: abrir esta wiki no Obsidian do seu PC e manter os dois lados sincronizados. O vault vive no servidor em `/opt/data/wiki`.
Contexto e riscos: [[controle-de-acesso-ao-vault]], [[versionamento-do-vault]], [[roteiro-de-implantacao]].

## Etapa 0 - Decidir (2 minutos)
| | Git (grátis) | Obsidian Sync (pago) |
|---|---|---|
| Celular | Não | Sim |
| Conflito de edição | Possível | Raro |
| Passos | Mais | Menos |
Escolha um. Sem Sync, vá de Git.

## Etapa 1 - Preparar o vault no servidor (o Hermes faz; precisa do seu OK)
1. Tirar `raw/articles/dossie-alligare-2026-11.md` do vault (contém dados pessoais e de clientes).
2. Criar `.gitignore` e rodar `git init` com um commit-base.
3. Conferir que nenhuma credencial entrou (a pasta `/opt/data/credentials` fica fora do vault).
Conferência: `git log` mostra 1 commit; o dossiê não está na pasta.

## Etapa 2 - Instalar o Obsidian no PC
1. Baixe em obsidian.md e instale.
2. Ainda não abra nenhuma pasta; primeiro sincronize (etapa 3).

## Etapa 3A - Caminho Git
1. **Você:** no GitHub, crie um repositório **privado** `alligare-wiki` e ative a verificação em duas etapas na conta.
2. **Hermes:** gera uma chave SSH só para este repositório e mostra a **chave pública**.
3. **Você:** no repositório, Settings > Deploy keys > Add deploy key, cole a chave pública e marque "Allow write access".
4. **Hermes:** liga o remoto e faz o primeiro `push`.
5. **Você, no PC:** instale o Git, rode `git clone` do repositório e, no Obsidian, "Abrir pasta como cofre" e escolha a pasta clonada.
6. No Obsidian: Configurações > Plugins da comunidade > ativar > buscar **Obsidian Git** > instalar e ativar. Configure commit e pull automáticos (a cada 10 min é um bom começo).
7. **Hermes:** agenda commit e push periódicos do lado do servidor.

## Etapa 3B - Caminho Obsidian Sync
1. **Você:** no Obsidian do PC, crie um cofre novo e ative Configurações > Sync (conta e assinatura).
2. **Hermes:** instala o `obsidian-headless` (pacote npm; o servidor tem Node 26).
3. **Você:** faz o login da sua conta Obsidian no terminal quando o Hermes pedir. O Hermes não digita a sua senha.
4. **Hermes:** conecta `/opt/data/wiki` ao cofre remoto e inicia a sincronização contínua em segundo plano.
Nota: os comandos do `obsidian-headless` vêm da skill `llm-wiki`; ainda não foram testados neste servidor.

## Etapa 4 - Testar nos dois sentidos
1. No PC, crie a nota `teste-do-pc.md` com um link no formato wikilink (dois colchetes) apontando para a página `alligare`. Espere o sync. Peça ao Hermes: "leia teste-do-pc".
2. Peça ao Hermes: "crie a nota teste-do-hermes". Confira que ela aparece no Obsidian.
3. Apague as duas notas e faça o commit.
Sucesso = as duas notas aparecem do outro lado em menos de 1 a 2 minutos (Git: depende do intervalo).

## Etapa 5 - Fechar as pontas
- Gravar `WIKI_PATH` e `OBSIDIAN_VAULT_PATH` no `.env` (aprovação pendente; a skill `alligare-wiki` funciona sem isso).
- Criar `humano/` (notas suas, só leitura para o agente) e `privado/`. Hoje valem só como regra escrita; o bloqueio real exige configurar montagens do Docker fora do servidor ([[controle-de-acesso-ao-vault]]).
- Testar o Telegram e trocar as tarefas agendadas para entregar lá ([[cadencia-semanal]]).

## Se algo der errado
- Conflito de Git: não apague nada; peça ao Hermes para mostrar `git status` e resolver com você.
- Nota sumiu: `git log` e `git checkout` do ponto anterior (é para isso que o commit-base existe).
- Sync parado: confira se o processo em segundo plano está ativo e se o login não expirou.
