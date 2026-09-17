import numpy as np
import sounddevice as sd
from openwakeword.model import Model


class WakeWordListener:

    def __init__(self):
        self.model = Model(wakeword_models=["hey_jarvis"],
        inference_framework="onnx"
        )
        self.threshold = 0.5
        self.sample_rate = 16000 
        self.chunk_size = 1280      
    

    def listen(self):
       
       # Mikrofon Stream öffnen, schließt sich automatisch danach
        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size
        ) as stream:
            while True:
                audio_chunk, _ = stream.read(self.chunk_size) # nächstes Audio-Stück lesen
                audio_data = np.frombuffer(audio_chunk, dtype=np.int16) # in Zahlen-Array umwandeln

                predictions = self.model.predict(audio_data) # Modell bewertet das Audio-Stück

                for wakeword, score in predictions.items(): # jedes erkannte Wake-Word prüfen
                    if score > self.threshold:  # Wahrscheinlichkeit hoch genug?
                        return True # Wake-Word erkannt -> Methode beenden