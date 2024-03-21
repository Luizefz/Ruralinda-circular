import requests
import json
from webhook import BusMessage
from uuid import uuid4
from datetime import datetime

link = "http://localhost:8000/"

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

bus_location = {
    "id": str(uuid4()),
    "username": "Anderson",
    "message_type": "location",
    "message_content": "Aquii!",
    "location": (-8.2446217252051, -34.98216853741),  #Latitude / Longetude
    "datetime": formatted_datetime
}

# Convertendo o dicionário para JSON
json_data = json.dumps(bus_location)

# Enviando uma solicitação POST com os dados JSON para a rota "/new"
response = requests.post(link+'add-bus-location/', data=json_data, headers={"Content-Type": "application/json"})

# Verifica se a solicitação foi bem-sucedida e imprime a resposta
if response.ok:
    print("Resposta:", response.json().get("message"))
else:
    print("Falha ao enviar dados. Código de status:", response.status_code)
