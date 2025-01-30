import requests

TOKEN = ""
CHAT_ID = ""  # ID do grupo

# Faz a requisição para obter informações do grupo
url = f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={CHAT_ID}"
response = requests.get(url).json()

# Exibe as informações do grupo
if response.get("ok"):
    chat_info = response["result"]
    print(f"📌 ID: {chat_info['id']}")
    print(f"📌 Nome: {chat_info.get('title', 'Sem Nome')}")
    print(f"📌 Username: @{chat_info.get('username', 'Sem username')}")
    print(f"📌 Tipo: {chat_info.get('type', 'Desconhecido')}")
    print(f"📌 Descrição: {chat_info.get('description', 'Sem descrição')}")
    print(f"📌 Link de convite: {chat_info.get('invite_link', 'Sem link')}")
else:
    print(f"Erro: {response.get('description', 'Erro desconhecido')}")
