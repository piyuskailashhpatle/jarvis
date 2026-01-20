import pyttsx3
from datetime import datetime
import requests
import json

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("🚀 Jarvis activited sucessfully!")
speak("Hello Karan")
//karan 



while True:
    command = input("Type command: ").lower().strip()

    if command == "exit":
        speak("Goodbye Karan")
        break

    elif "hello" in command:
        speak("Hello Karan, how can I help you?")

    elif "time" in command:
        time = datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    else:

        speak("Sorry, I did not understand")

