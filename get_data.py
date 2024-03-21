import requests


def get_bus_location():

    link = "https://ruralinda-circular.onrender.com/bus-location"
    
    response = requests.get(link, headers={"Content-Type": "application/json"})

    if response.ok:
        return print("Resposta:", response.json())
    
    return print("Falha ao enviar dados. Código de status:", response.status_code)

def get_last_message():

    link = "https://ruralinda-circular.onrender.com/last-message"
        
    response = requests.get(link, headers={"Content-Type": "application/json"})
    
    if response.ok:
        return print("Resposta:", response.json())
        
    return print("Falha ao enviar dados. Código de status:", response.status_code)

# get_bus_location()
# get_last_message()