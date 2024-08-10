import time, os
from obswebsocket import obsws, requests # type: ignore

class OBSClient:
    def __init__(self):
        self.client = obsws(os.getenv("OBS_IP"), os.getenv("OBS_PORT"), os.getenv("OBS_PASSWORD"))

    def EffectImageWithSound(self, scene_source, image_source="Image", audio_source="Sound", duration=1):
        self.client.connect()
        image_item_id = self.client.call(requests.GetSceneItemId(sceneName = scene_source, sourceName = scene_source + image_source)).getSceneItemId()

        self.client.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = True))
        self.client.call(requests.TriggerMediaInputAction(inputName = scene_source + audio_source, mediaAction="OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART"))
        
        time.sleep(duration)

        self.client.call(requests.SetSceneItemEnabled(sceneName = scene_source, sceneItemId = image_item_id, sceneItemEnabled = False))
        self.client.disconnect()

    def EffectVideo(self, scene_source, video_source="Video"):
        self.client.connect()
        self.client.call(requests.TriggerMediaInputAction(sceneName = scene_source, inputName = scene_source + video_source, mediaAction="OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART"))
        self.client.disconnect()