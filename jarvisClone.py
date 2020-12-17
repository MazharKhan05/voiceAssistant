import speech_recognition as sr
from time import ctime
import webbrowser
from gtts import gTTS
import os
import playsound


r = sr.Recognizer()

def speech(text):
    data = gTTS(text= text, lang='en')
    fName = "audio.mp3"
    data.save(fName)
    playsound.playsound(fName)
    os.remove('./audio.mp3') 


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
            speech(ask)
        audio = r.listen(source)
        audio_data= ""
        try:
            audio_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speech('Sorry, I did not get that')
        except sr.RequestError:
            speech('Sorry, my speech service is down')
        return audio_data

def respond(content):
    if  'what is your name' in content:
        print(content)
        print('My name is Jarvis...')
        speech('My name is Jarvis...')
    if 'what time is it' in content:
        print(content)
        print(ctime())
        speech(ctime())
    if  'search' in content: 
        keyword = record_audio('what do you want to search for?')
        print(keyword)
        url = "https://www.google.com/search?q=" + keyword
        
        webbrowser.get().open(url)
        print('Here is what I found for ' + keyword)
        speech('Here is what I found for ' + keyword)
    if  'find location' in content: 
        keyword = record_audio('what do you want to locate?')
        print(keyword)
        url = "https://www.google.nl/maps/place/" + keyword + "/&amp"
        webbrowser.get().open(url)
        print('Here is the location of ' + keyword)
        speech('Here is the location of ' + keyword)
    if 'what can you do' in content:
        print(content)
        print("You can ask me for:\n Time-> by saying, `what time is it?`,\n Google anyting-> by saying, `search`,\n Locate anything-> by saying, `find Location`,\n Exit-> by saying, `bye`. ")
        speech("You can ask me for:\n Time-> by saying, `what time is it?`,\n Google anyting-> by saying, `search`,\n Locate anything-> by saying, `find Location`,\n Exit-> by saying, `bye`. ")
    if 'exit' in content:
        print('Bye, Always there to help you anytime')
        speech('Bye, Always there to help you anytime')
        exit()

   
speech('How can I help you?')

while 1:
    content = record_audio()
    respond(content)
