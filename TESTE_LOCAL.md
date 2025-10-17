
# 🧪 TESTE LOCAL DO SISTEMA

## Testar servidor localmente (antes do deploy):

```bash
python slack_bot_server.py
```

## Testar endpoints:

### 1. Status do sistema:
```bash
curl http://localhost:5000/status
```

### 2. Simular comando Slack:
```bash
curl -X POST http://localhost:5000/slack/categorizar \
     -d "text=dipirona" \
     -H "Content-Type: application/x-www-form-urlencoded"
```

### 3. Comando de ajuda:
```bash
curl -X POST http://localhost:5000/slack/ajuda \
     -H "Content-Type: application/x-www-form-urlencoded"
```

## Respostas esperadas:
- Status: JSON com informações do sistema
- Categorizar: Categoria do medicamento ou "não encontrado"
- Ajuda: Lista de comandos disponíveis
