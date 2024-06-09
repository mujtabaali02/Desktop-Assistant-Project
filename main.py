import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio

# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


#speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()


# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query




#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing")

    else:
        speak("Good evening sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")




if __name__ == "__main__":

    wish_me()

    while True:

        print("\n Tracker 1  - UP \n Tracker 2 - RJHR \n Tracker 3 -Upper North \n Tracker 4 - NLNCR \n Tracker 5 -GJMP")  
        query = takeCommand().lower()
        # print("\nTracker 1  - UP \n Tracker 2 - RJHR \n Tracker 3 -Upper North \n Tracker 4 - NLNCR \n Tracker 5 -GJMP")

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        
        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        
        elif "google" in query:
            speak("Opening google")
            webbrowser.open("google.com")


        elif "github" in query:
            speak("Opening github")
            webbrowser.open("github.com")

        elif "tracker 1" in query:
            speak("Opening undelvalidationtracker for uttar pradesh Region")
            webbrowser.open("https://docs.google.com/spreadsheets/d/1Spd8DtzpmOLpDyE0OK-iKw2Wx1sylpCIHW3IvH0f1eg/edit#gid=998157805")
            # webbrowser.open("amazon.com")
        
        elif "tracker 2" in query:
            speak("Opening undel validation tracker for Rajasthan and Haryana Region")
            webbrowser.open("https://docs.google.com/spreadsheets/d/1NWrZ5THXhWLsxEDyIXLxiYjU6L5Y0CaSPFLC1jVNXkg/edit#gid=1216455963")
        
        elif "tracker 3" in query:
            speak("Opening undel validation tracker for Upper North Region")
            webbrowser.open("https://docs.google.com/spreadsheets/d/14rO-QCRlicdLgk4N2yvh9dWCvcgEY42fdFLiYxXICD0/edit#gid=0")
        
        elif "tracker 4" in query:
            speak("Opening undel validation tracker for Delhi NCR...")
            webbrowser.open("https://docs.google.com/spreadsheets/d/1XApzET25dDu-Q7DVn6s2iu4kGJAhydYq2uVW8_ijL4A/edit#gid=0")
        
        elif "tracker 5" in query:
            speak("Opening undelvalidationtracker for Gujarat and Madhya Pradesh Region")
            webbrowser.open("https://docs.google.com/spreadsheets/d/1UApdetLHxF5d2qKwyK_v118KvgD5Rc9lYHxCi0OZ_so/edit#gid=0") 

         #This query for say the times
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")


        elif 'goodbye' in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()