import pyttsx3

from datetime import datetime
from decouple import config

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if(hour >= 0) and (hour < 12):
        speak(f"Good morning {USER}")
    elif(hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif(hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? { USER}")

if __name__ == '__main__':
    greet_me()