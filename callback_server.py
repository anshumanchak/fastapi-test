from fastapi import FastAPI, Response, Request, HTTPException
from pydantic import BaseModel
# import xml.etree.ElementTree as ET

app = FastAPI()

# class AtomFeed(BaseModel):
#     data: str

@app.post("/callback")
async def handle_callback(response: Response):
    print(response)
    # content_type = response.headers['Content-Type']
    # print(content_type)
    print(response.body())
    # if content_type == 'application/xml':
    #     body = await response.body()
    return Response(content=body, media_type="application/xml")
    # else:
    #     raise HTTPException(status_code=400, detail=f'Content type {content_type} not supported')

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
