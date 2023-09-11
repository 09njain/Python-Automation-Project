import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import smtplib
import pyaudio


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Let me Know How can i help you? What are you Looking for")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to You....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing your voice.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said:{query}\n")
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail','gmailpassword')
    server.sendmail('your gmail',to,content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower() #Converting user query into lower case
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        elif 'email to your friend' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "friend gmail address"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
    




    




