import os
from dotenv import load_dotenv

load_dotenv()

OBS_WS_HOST = os.getenv("OBS_WS_HOST") # Der Host auf dem der Websocket läuft

OBS_WS_PORT = int(os.getenv("OBS_WS_PORT", 4455)) # Port des WebSocket

OBS_WS_PASSWORD = os.getenv("OBS_WS_PASSWORD") # Passwort für die Authentifizierung

if not OBS_WS_PASSWORD:
    raise ValueError("Passwort fehlt bzw. nicht angegeben")
