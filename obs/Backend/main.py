from obs import OBSClient
from fastapi import FastAPI, Request # type: ignore
from pydantic import BaseModel # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

app = FastAPI() # type: ignore
obs_client = OBSClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EffectRequest(BaseModel):
    name: str
    type: str

@app.post("/effect")
def effectBruh(request: EffectRequest):
    if(request.type == "image"):
        obs_client.EffectImageWithSound(scene_source="Effect" + request.name)
    elif(request.type == "video"):
        obs_client.EffectVideo(scene_source="Effect" + request.name)

    return {"status": "Success"}
