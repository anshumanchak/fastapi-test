from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
# import xml.etree.ElementTree as ET

app = FastAPI()

# class AtomFeed(BaseModel):
#     data: str

@app.post("/callback")
async def handle_callback(xml_data: bytes):
    try:
        decoded_xml = xml_data.decode("utf-8")
        print("Received XML Data:")
        print(decoded_xml)
        return {"message": "XML data received and processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing XML data")

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
