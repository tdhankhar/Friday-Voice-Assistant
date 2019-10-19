import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday..How can i help you sir?")

def takeCommand():
    #takes mike input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except:
        print("Say that again please.....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        
        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open coding ninjas' in query:
            webbrowser.open("codingninjas.in")
        
        elif 'open practice geeksforgeeks' in query:
            webbrowser.open("practice.geeksforgeeks.org")

        elif 'open practice gfg' in query:
            webbrowser.open("practice.geeksforgeeks.org")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            Path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Path)

        elif 'open google chrome' in query:
            Path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Path)
        
        elif 'shut up friday' in query:
            exit()
        
        else:
            speak("Sorry sir! I didn't understand what you just said..")
            speak("Please say that again")
            print("Please say it again!")