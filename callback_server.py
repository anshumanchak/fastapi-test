from fastapi import FastAPI, Response, Request, HTTPException
from pydantic import BaseModel
# import xml.etree.ElementTree as ET

app = FastAPI()

# class AtomFeed(BaseModel):
#     data: str

@app.post("/callback")
async def handle_callback(request: Request):
    try:
        print("Received XML Data:")
        body_bytes = await request.body()
        print(body_bytes)
        # body_json = await request.json()
        # print(body_json)
        # body_str = body_bytes.decode("utf-8")
        # print(body_str)
        return {"message": "XML data received and processed successfully"}
    
    except Exception as e:
        print(str(e))
        return {"error": str(e)}

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