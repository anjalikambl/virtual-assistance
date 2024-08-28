import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
from datetime import date
import datetime
import wikipedia
import pyjokes
import requests

listener=sr.Recognizer()
engine=pyttsx3.init()          #to initialize
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)  #0: male 1: female voice
engine.say('I am alexa')
def talk(text):
    engine.say(text)
    engine.runAndWait()   ## Block while processing all the currently queued command
def take_command():
    with sr.Microphone() as source:
        print("Listening.....")
        voices=listener.listen(source)
        command=listener.recognize_google(voices)
        command=command.lower()
        print(command)
    if 'alexa' in command:
        command=command.replace('alexa','')
        print(command)
    return command


def run_alexa():
    cmd=take_command()
    if 'play' in cmd:
        song=cmd.replace('play','')            #replace because it will replace with the song name
        talk('playing'+song)                   #it will say playing +song
        pw.playonyt(song)                   #it will jump to youtube
    elif 'date' in cmd:
        today=date.today()
        print(today)
        talk(today)
    elif 'time' in cmd:
        time=datetime.datetime.now().strftime('%H:%M')
        #time=datetime.datetime.now().strftime('%I:%M %p')    #string format I-
        print(time)
        talk('Current time is'+time)
    elif 'prime minister' in cmd:
        try:
            #perosn=cmd.replace('who is the prime minister of india','')
            info=wikipedia.summary(cmd)   #string parameter
            print(info)
            talk(info)
        except:
            print('Error')
    elif 'joke' in cmd:
        joking=pyjokes.get_joke(language='en',category='neutral')
        print(joking)
        talk(joking)
    elif 'are you single' in cmd:
        talk('I am in a relationship with wifi')

   


while True:
    run_alexa()                                 #fun call