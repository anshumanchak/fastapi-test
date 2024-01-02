from fastapi import FastAPI
from pydantic import BaseModel
import xml.etree.ElementTree as ET

app = FastAPI()

class AtomFeed(BaseModel):
    data: str

@app.post("/callback")
async def receive_notification(feed_data: AtomFeed):
    received_data = feed_data.data
    print("Received Atom Feed Data:")
    print(received_data)
    return {"received_data": received_data}

@app.get("/")
async def print_root():
    return "Hi, you are inside disag"

@app.get("/callback")
async def receive_notification(feed_data: AtomFeed):
    received_data = feed_data.data
    print("Received Atom Feed Data:")
    print(received_data)
    return {"received_data": received_data}
