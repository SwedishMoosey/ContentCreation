import time, os
from fastapi import FastAPI # type: ignore
from obswebsocket import obsws, requests # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from dotenv import load_dotenv # type: ignore

app = FastAPI() # type: ignore
load_dotenv()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/effect/bruh")
def effectBruh():
    ws.connect()
    EffectImageWithSound(scene_source="EffectBruh")
    ws.disconnect()
    return {"status": "Success"}

@app.get("/effect/crying")
def effectBruh():
    ws.connect()
    EffectVideo(scene_source="EffectCrying")
    ws.disconnect()
    return {"status": "Success"}

@app.get("/effect/rage")
def effectBruh():
    ws.connect()
    EffectVideo(scene_source="EffectRage")
    ws.disconnect()
    return {"status": "Success"}

# Connection parameters
HOST = os.getenv("OBS_IP")
PORT = os.getenv("OBS_PORT")
PASSWORD = os.getenv("OBS_PASSWORD")

# Connect to OBS
ws = obsws(HOST, PORT, PASSWORD)

def EffectImageWithSound(scene_source, image_source="Image", audio_source="Sound", duration=1):
    image_item_id = ws.call(requests.GetSceneItemId(sceneName = scene_source, sourceName = scene_source + image_source)).getSceneItemId()
    print(image_item_id)

    ws.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = True))
    ws.call(requests.TriggerMediaInputAction(inputName = scene_source + audio_source, mediaAction="OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART"))
    
    time.sleep(duration)
    
    ws.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = False))

def EffectVideo(scene_source, video_source="Video"):
    ws.call(requests.TriggerMediaInputAction(sceneName = scene_source, inputName = scene_source + video_source, mediaAction="OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART"))
