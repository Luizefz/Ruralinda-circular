import requests
import json
from uuid import uuid4
from datetime import datetime

link = "https://ruralinda-circular.onrender.com/add-bus-message/"

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

bus_message = {
    "id": str(uuid4()),
    "username": "Arthur",
    "message_type": "message",
    "message_content": "Onibus reparado e voltando a circular.",
    "location": (0, 0),  #Latitude / Longetude
    "datetime": formatted_datetime
}

# Convertendo o dicionário para JSON
json_data = json.dumps(bus_message)

# Enviando uma solicitação POST com os dados JSON para a rota "/new"
response = requests.post(link, data=json_data, headers={"Content-Type": "application/json"})

# Verifica se a solicitação foi bem-sucedida e imprime a resposta
if response.ok:
    print("Resposta:", response.json().get("message"))
else:
    print("Falha ao enviar dados. Código de status:", response.status_code)