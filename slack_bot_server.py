import ssl
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['PYTHONHTTPSVERIFY'] = '0'

from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Resto do seu código continua igual...


# Carregar bases de dadosa
def carregar_dados():
    """Carrega as bases de medicamentos e taxonomia"""
    try:
        with open('medicamentos_slack.json', 'r', encoding='utf-8') as f:
            medicamentos = json.load(f)
        
        with open('taxonomia_slack.json', 'r', encoding='utf-8') as f:
            taxonomia = json.load(f)
            
        return medicamentos, taxonomia
    except FileNotFoundError:
        return [], {}

# Função de busca de medicamentos
def buscar_medicamento(nome):
    """Busca medicamento na base simplificada"""
    medicamentos, taxonomia = carregar_dados()
    
    nome_lower = nome.lower().strip()
    
    for med in medicamentos:
        if nome_lower in med['nome'].lower():
            return {
                'encontrado': True,
                'nome': med['nome'],
                'categoria': med['categoria'],
                'confiabilidade': med['confiabilidade'],
                'emoji': '🟢' if med['confiabilidade'] == 'alta' else '🟡'
            }
    
    return {
        'encontrado': False,
        'sugestao': 'Use a plataforma completa para análise detalhada'
    }

# Rota principal do Slack - Comando /categorizar
@app.route('/slack/categorizar', methods=['POST'])
def slack_categorizar():
    """Processa comando /categorizar do Slack"""
    
    # Obter dados do Slack
    slack_data = request.form
    produto = slack_data.get('text', '').strip()
    
    if not produto:
        return jsonify({
            "response_type": "ephemeral",
            "text": "ℹ️  Uso: /categorizar [nome do medicamento]\nExemplo: /categorizar dipirona"
        })
    
    # Buscar medicamento
    resultado = buscar_medicamento(produto)
    
    if resultado['encontrado']:
        resposta = f"🏥 **{resultado['nome'].title()}**\n" +                   f"📂 {resultado['categoria']} ({resultado['emoji']} {resultado['confiabilidade']})\n" +                   f"⚡ _Consulta rápida - Para análise completa use a plataforma principal_"
    else:
        resposta = f"❓ **{produto.title()}** não encontrado na base rápida\n" +                   f"💡 {resultado['sugestao']}\n" +                   f"🔗 Use: https://plataforma-drauzio.com"
    
    return jsonify({
        "response_type": "in_channel",
        "text": resposta
    })

# Rota para comando /ajuda
@app.route('/slack/ajuda', methods=['POST'])
def slack_ajuda():
    """Mostra ajuda dos comandos"""
    
    ajuda_text = """
🤖 **Drauzio Bot - Comandos Disponíveis**

⚡ **Consultas Rápidas:**
• `/categorizar [medicamento]` - Categorização básica
• `/ean [código]` - Busca por EAN (em breve)
• `/ajuda` - Esta mensagem

🏥 **Plataforma Completa:**
• Análise clínica detalhada
• Processamento de lotes
• Relatórios profissionais
• Precisão de 98.6%

💡 **Dica:** Use o bot para consultas rápidas e a plataforma para análises completas!
    """
    
    return jsonify({
        "response_type": "ephemeral", 
        "text": ajuda_text.strip()
    })

# Rota de status/health check
@app.route('/status')
def status():
    """Verifica se o serviço está funcionando"""
    medicamentos, taxonomia = carregar_dados()
    
    return jsonify({
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "medicamentos_carregados": len(medicamentos),
        "categorias_disponiveis": len(taxonomia)
    })

if __name__ == '__main__':
    print("🚀 Iniciando Servidor Drauzio Slack Bot...")
    print("📍 Endpoints disponíveis:")
    print("   POST /slack/categorizar")
    print("   POST /slack/ajuda") 
    print("   GET  /status")
    print("\n🔗 Configure no Slack:")
    print("   URL: https://seu-servidor.com/slack/categorizar")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
