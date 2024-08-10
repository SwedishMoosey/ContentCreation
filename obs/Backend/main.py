import time, os
from fastapi import FastAPI # type: ignore
from obswebsocket import obsws, requests # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI() # type: ignore
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

@app.get("/test")
def test():
    ws.connect()
    PopupWithSound(scene_source="Center Monitor Scene", image_source="testImage", audio_source="testAudio", duration=1)
    ws.disconnect()
    return {"status": "Hello there"}








# Connection parameters
HOST = os.getenv('OBS_HOST')
PORT = 4455
PASSWORD = "OFR1KitYP19bPpRG"

# Connect to OBS
ws = obsws(HOST, PORT, PASSWORD)

# Function to show a popup
def PopupWithSound(scene_source, image_source, audio_source=False, duration=5):
    image_item_id = ws.call(requests.GetSceneItemId(sceneName = scene_source, sourceName = image_source)).getSceneItemId()

    ws.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = True))
    if(audio_source):
        ws.call(requests.TriggerMediaInputAction(inputName = audio_source, mediaAction="OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART"))
    
    time.sleep(duration)
    
    ws.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = False))
