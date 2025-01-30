import requests

TOKEN = ""

# Obtém os updates do bot (onde ele já interagiu)
url_updates = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
updates = requests.get(url_updates).json()

# Lista para armazenar os grupos válidos
valid_groups = []

# Itera sobre os updates para encontrar grupos
for update in updates.get("result", []):
    chat = update.get("message", {}).get("chat", {})
    chat_id = chat.get("id")
    chat_type = chat.get("type")

    # Verifica se é um grupo ou supergrupo
    if chat_type in ["group", "supergroup"]:
        # Faz um request para verificar se o grupo ainda existe
        url_chat = f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={chat_id}"
        response = requests.get(url_chat).json()
        
        if response.get("ok"):  # Se o grupo ainda existe
            valid_groups.append({"id": chat_id, "title": chat.get("title", "Sem Nome")})

# Exibe os grupos válidos
print("Grupos onde o bot ainda está presente:")
for group in valid_groups:
    print(f"- Title: {group['title']} | (ID: {group['id']})")
