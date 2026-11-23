---
title: Controle de acesso do agente ao vault
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [seguranca, obsidian, hermes, agentes]
sources: [raw/transcripts/wanderloots-hermes-obsidian-acesso.md, raw/transcripts/obsidian-herder-agentes-no-vault.md]
confidence: medium
---
# Controle de acesso do agente ao vault

Ideia do vídeo (Wanderloots): o agente não precisa ver o vault inteiro. Separar notas humanas e notas de IA **dentro do mesmo vault**.
Três camadas, da mais fraca à mais forte:
1. **Skill (camada "branda"):** regras escritas no `SKILL.md` ("nunca ler a pasta private"). O autor chama de boa prática, não de segurança: o agente pode esquecer a regra quando o contexto é compactado.
2. **Montagens do Docker:** o agente roda num container e só enxerga o que foi montado, em modo `rw` (padrão), `ro` (só leitura) ou **máscara** (uma pasta vazia montada por cima da pasta privada, que some para o agente).
3. **Sistema operacional do host:** o mais seguro e o mais complexo (não detalhado no vídeo).
Também: um **perfil** do Hermes por nível de confiança (por exemplo, perfil com modelo de nuvem sem acesso ao vault; perfil com modelo local com acesso total). Cada perfil tem a sua configuração de volumes.
Controle de versão com Git funciona como botão de desfazer: commit-base antes de deixar o agente escrever; ver [[versionamento-do-vault]].
No vídeo o vault fica dentro da pasta de trabalho montada no container, e o caminho do vault é passado ao container por variável de ambiente (`OBSIDIAN_VAULT_PATH`, com o caminho como o container o enxerga).

Aplicação aqui: ver [[hermes-no-vault]] e [[roteiro-de-implantacao]].
