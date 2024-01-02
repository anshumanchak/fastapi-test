from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
# import xml.etree.ElementTree as ET

app = FastAPI()

# class AtomFeed(BaseModel):
#     data: str

@app.post("/callback")
async def yt_notification(feed_data: str):
    received_data = feed_data
    print("Received Atom Feed Data:")
    print(received_data)
    return {"received_data": received_data}

@app.get("/")
async def print_root():
    return "Hi, you are inside disag"

@app.get("/callback")
async def receive_notification(request: Request):
    hub_topic = request.query_params.get('hub.topic')
    hub_challenge = request.query_params.get('hub.challenge')
    hub_mode = request.query_params.get('hub.mode')
    hub_lease_seconds = request.query_params.get('hub.lease_seconds')
    print("Hub Topic:", hub_topic)
    print("Hub Challenge:", hub_challenge)
    print("Hub Mode:", hub_mode)
    print("Hub Lease Seconds:", hub_lease_seconds)
    return int(hub_challenge)
