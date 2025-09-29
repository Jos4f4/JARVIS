#Orientations
#Execution first in terminal
#After, press the buttons ctrl + alt + k for start

import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp

from datetime import datetime
from decouple import config
from conv import random_text
from random import choice

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

listening = False

def start_listening():
    global listening
    listening = True
    print("started listening ")

def pause_listening():
    global listening
    listening = False
    print("stopped listening")

keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language = 'en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir")
            exit()
    except Exception:
        speak("Sorry I couldn't understabd. Can you please repeat that?")
        queri = 'None'

    return queri

if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path = "C:\\ProgramData\\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                os.startfile(notepad_path)

            elif "open discord" in query:
                speak("Opening Discord for you sir")
                discord_path = "C:\\ProgramData\\ASSUS\\Discord\\app-1.0.9028\\discord.exe"
                os.startfile(discord_path)

            elif "open gta" in query:
                speak("Opening Gta for you sir")
                gta_path = "D:\\Tanishq\\GTA\\Launcher.exe"
                os.startfile(gta_path)

            elif "open armoury crate" in query:
                speak("Opening armoury crate for you sir")
                crate_path = "C:\\Program Files\\ASUS\\Armoury CRATE Service\\DenoiseAIPlugin\\ArmouryCrate.DenoiseAI.exe"
                os.startfile(crate_path)
