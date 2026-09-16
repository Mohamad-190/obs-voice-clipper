from src.obs_client import OBSClient

obs_client = OBSClient()
print("Verbindung zu OBS erfolgreich.")

obs_client.save_replay_buffer()
print("Replay Buffer gespeichert.")