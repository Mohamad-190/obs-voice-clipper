from src.wake_word_listener import WakeWordListener

listener = WakeWordListener()
print("Höre zu... Sag 'Hey Jarvis'")

listener.listen()
print("Wake-Word erkannt!")