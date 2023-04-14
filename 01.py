import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("I am Jarvis Komal. please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    # print(e)
        print("Say that again please...") 
        return "None"   
    return query

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()
        #query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
                speak('Searching wikipedia...')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'who creates you' in query:
            speak("Komal create you by using python")

        # elif "advice" in query:
        #         speak(f"Here's an advice for you, mam")
        #         advice = get_random_advice()
        #         speak(advice)
        #         speak("For your convenience, I am printing it on the screen mam.")   
        #         print(advice)

        # elif 'the time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Mam, the time is {strTime}")

        elif 'how are you' in query:
                speak("I am good mam what about you!")

        elif 'open code' in query:
            codePath = "C:\\Users\\komal\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)


        elif 'hello' in query:
            speak("Hello Komal Mam...")

        elif 'logout' in query:
            speak("Thank you mam!")
            exit()                           


