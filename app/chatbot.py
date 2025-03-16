# este seria el codigo del chatbot
import requests
import json
from config.config import API_URL, AGENT_ID

def get_agent_response(user_input):
    headers = {'Content-Type': 'application/json'}
    data = {'query': user_input}
    try:
        response = requests.post(API_URL.format(agent_id=AGENT_ID), headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result.get('response', 'No response from agent')
    except Exception as e:
        return f"Error al conectar con el agente: {e}"
