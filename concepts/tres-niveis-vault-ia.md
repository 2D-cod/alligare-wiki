---
title: Três níveis de IA com Obsidian
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [obsidian, second-brain, wiki]
sources: [raw/transcripts/tina-obsidian-24-minutos.md]
confidence: high
---
# Três níveis de IA com Obsidian (Tina Huang)

Obsidian é uma pasta de arquivos `.md`: legível, local e aceita qualquer software. Isso o torna ideal para IA.

1. **Segundo cérebro:** você escreve, a IA lê e interpreta o vault (Claude, Codex, Hermes com modelo local se quiser privacidade total).
2. **Banco de dados de IA:** vários agentes e widgets *gravam* logs e documentos no vault; você consulta. Várias máquinas (PC, VPS) escrevem no mesmo vault via sincronização.
3. **LLM Wiki:** a IA escreve, organiza, consulta e faz manutenção; você só alimenta fontes e pergunta. Ver [[padrao-llm-wiki]].

Sincronização: Obsidian Sync (pago, criptografado ponta a ponta), Git ou Syncthing. Nosso estado: nível 3 montado em `/opt/data/wiki`; sincronizar com o PC é pendência ([[roteiro-de-implantacao]]).
Alternativas a serviços de terceiros: [[opcoes-de-memoria-compartilhada]]. Plugins citados: Smart Connections, Copilot. Entrada rápida de conteúdo: bot de Telegram (o nosso tem bot no `.env`; falta testar).
