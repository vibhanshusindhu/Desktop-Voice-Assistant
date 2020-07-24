import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5') # 'sapi5' is a speech recognition API designed by Microsoft.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #Voice id helps us to select different voices.


# A function that converts our text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# A function to greet the user according to the time of computer.
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Varnam. Please tell me how may I help you")       

# A function that takes microphone input from the user and returns string output.
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


execution=True


if __name__ == "__main__":

    greetMe()

    while execution:
    
        query = takeCommand().lower() #converting the query into lowercase.

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")

            try:
                results = wikipedia.summary(query, sentences=2) # this function will return 2 sentecnes from the wikipedia artcile
                speak("According to Wikipedia")
                print(results)
                speak(results) # the results are being spoken by the assistant
            except Exception as e:
                speak("No Results Found!")
                print("No Results Found")

        elif "How are you" in query:
	          speak("I am good,Sir.Thank you.")

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")   

        elif 'open codeforces' in query:
            speak("Opening codeforces...")
            webbrowser.open("codeforces.com")

        elif 'play songs' in query:
            music_dir = 'D:\\Me\\songs\\classic'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open geeks for geeks' in query:
            speak("Opening geeksforgeeks...")
            webbrowser.open("geeksforgeeks.org")

        elif 'open interview bit' in query:
            speak("Opening interview bit...")
            webbrowser.open("interviewbit.com")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%x")
            speak(f"Sir, the date is {date}")

        elif 'open VScode' in query:
            codePath = "C:\\Users\\vibhanshu\\AppData\\Local\\Programs\\Microsoft VSCode\\Code.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            speak("Goodbye,Sir!")
            execution=False   
        
        else:
			      speak("Sorry I didn't catch that.")