import os
import requests
import datetime
import pytz


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


today = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))

meses = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}

formatted_name = f"{today.day} de {meses[today.month]} de {today.year}"

url = f"https://api.telegram.org/bot{TOKEN}/setChatTitle"
dados = {"chat_id": CHAT_ID, "title": formatted_name}

response = requests.post(url, data=dados)


if response.status_code == 200:
    print(f"Nome do grupo atualizado para: {formatted_name}")
else:
    print("Erro ao atualizar o nome do grupo:", response.text)
