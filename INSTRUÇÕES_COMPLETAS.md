
# 🤖 SISTEMA HÍBRIDO DRAUZIO + SLACK

## 📋 ARQUIVOS INCLUÍDOS:
- slack_bot_server.py (servidor principal)
- medicamentos_slack.json (base de medicamentos)
- taxonomia_slack.json (categorias)
- requirements.txt (dependências)
- Procfile (configuração Heroku)
- .env.exemplo (variáveis de ambiente)

## 🚀 DEPLOY RÁPIDO:

### 1. Preparar ambiente local:
```bash
mkdir drauzio-slack-bot
cd drauzio-slack-bot
# Copiar todos os arquivos para esta pasta
```

### 2. Deploy no Heroku:
```bash
git init
heroku login
heroku create seu-app-nome
git add .
git commit -m "Deploy inicial"
git push heroku main
```

### 3. Configurar Slack App:
- Criar app em api.slack.com
- Slash Command URL: https://seu-app.herokuapp.com/slack/categorizar
- Scopes: chat:write, commands
- Instalar no workspace

### 4. Configurar variáveis:
```bash
heroku config:set SLACK_BOT_TOKEN=xoxb-...
heroku config:set SLACK_SIGNING_SECRET=...
```

## 💡 COMO USAR:

### No Slack:
- `/categorizar dipirona` → Consulta rápida
- `/ajuda` → Ver comandos disponíveis

### Nesta plataforma:
- Upload de planilhas → Análise completa
- Relatórios detalhados → Excel/CSV
- Análise clínica → Indicações, contraindicações

## 🔧 MANUTENÇÃO:
- Base rápida: medicamentos_slack.json (atualize conforme necessário)
- Logs: `heroku logs --tail`
- Status: https://seu-app.herokuapp.com/status
