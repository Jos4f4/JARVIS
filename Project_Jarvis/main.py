from ipaddress import ip_address

import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp

from datetime import datetime
from decouple import config
from random import choice
from conv import random_text
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you {USER}")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening ")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey("ctrl+alt+k", start_listening)
keyboard.add_hotkey("ctrl+alt+p", pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour()
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry I couldm't understand. Can you please repeat that?")
        queri = 'None'
    return queri


if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")

            elif 'open command prompt' in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "Open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.window.camera:', shell=True)

            elif "Open notepad" in query:
                speak("Opening notepad for you sir")
                notepad_path = "C:\\Users\\carlo\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                os.startfile(notepad_path)

            elif "open discord" in query:
                speak("Opening discord for you sir")
                discord_path = "C:\\Users\\carlo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\discord.exe"
                os.startfile(discord_path)

            elif "open gta" in query:
                speak("Opening Gta for you sir")
                gta_path = "D:\\Tanishg\\GTA\\Launcher.exe"
                os.startfile(gta_path)

            elif "open armoury crate" in query:
                speak("Opening Gta for you sir")
                crate_path = "C:\\Program Files\\ASUS\\ARMOURY CRATE Service\\DenoiseAIPlugin\\ArmouryCrate.DenoiseAI.exe"
                os.startfile(crate_path)

            elif "ip adrress" in query:
                ip_address = find_my_ip()
                speak(
                    f"your ip address is {ip_address}"
                )
                print(f"your Ip address is {ip_address}")

            elif "open youtube" in query:
                speak("What do you want to play on youtube, sir?")
                video = take_command().lower()
                youtube(video)

            elif "open google" in query:
                speak(f"What do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia, {results}")
                speak("I am printing in on terminal")
                print(results)

            elif "send an email" in query:
                speak("On what email address do you want to send sir? Please enter in the terminal")
                receiver_add = input("Email address")
                speak("What should be the subject sir?")
                subject = take_command().capitalize()
                speak("What is the message?")
                message = take_command().capitalize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir")
                    print("I have sent the email sir")
                else:
                    speak("something went wrong Please check the error log")