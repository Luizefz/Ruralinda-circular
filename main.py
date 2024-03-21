from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

last_locations = []
last_messages = []

class BusMessage(BaseModel):
    id: str
    username: str
    message_type: str
    message_content: str
    location: tuple[float, float] #Latitude / Longetude
    datetime: datetime

@app.post("/add-bus-location")
def add_bus_location(body: BusMessage):
    if len(last_locations) >= 5:
        last_locations.pop(0) 
    last_locations.append(body)
    return {"message": "Location added successfully"}

@app.post("/add-bus-message")
def add_bus_message(body: BusMessage):
    if len(last_messages) >= 10:
        last_messages.pop(0)
    last_messages.append(body)
    return {"message": "Message added successfully"}

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/bus-location")
def get_bus_location():
    if len(last_locations) == 0:
        return {"message": "The bus hasn't sent any location yet"}
    return last_locations

@app.get("/last-messages")
def get_last_message():
    if len(last_messages) == 0:
        return {"message": "No messages sent yet"}
    return last_messages


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0")
