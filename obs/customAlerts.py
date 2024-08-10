import time
from obswebsocket import obsws, requests # type: ignore

# Connection parameters
HOST = "192.168.0.79"
PORT = 4455
PASSWORD = "OFR1KitYP19bPpRG"

# Connect to OBS
ws = obsws(HOST, PORT, PASSWORD)
ws.connect()

# Function to show a popup
def show_popup(image_source="testImage", audio_source="testAudio", duration=5):
    # Show the image
    ws.call(requests.SetSceneItemProperties(item=image_source, visible=True))
    # Start the audio
    ws.call(requests.PlayPauseMedia(media_name=audio_source, play=True))
    
    # Wait for the duration
    time.sleep(duration)
    
    # Hide the image
    ws.call(requests.SetSceneItemProperties(item=image_source, visible=False))
    # Stop the audio (optional, since it should stop on its own)
    ws.call(requests.PlayPauseMedia(sourceName=audio_source, play=False))

# Example usage
show_popup(duration=5)

# Disconnect when done
ws.disconnect()
