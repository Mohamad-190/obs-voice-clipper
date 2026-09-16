import obsws_python as obs
from src.config import OBS_WS_HOST, OBS_WS_PORT, OBS_WS_PASSWORD

class OBSClient:
    def __init__(self):
        self.client = obs.ReqClient(
            host = OBS_WS_HOST,
            port = OBS_WS_PORT,
            password = OBS_WS_PASSWORD,
            timeout = 3
        )


    def save_replay_buffer(self):
        self.client.save_replay_buffer()


    def get_last_replay_path(self) -> str:
        response = self.client.get_last_replay_path()
        return response.save_replay_path