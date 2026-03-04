import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import applibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="9ee9b78dd33622f18446197e40837699"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
def aiprocces(command):
    client =()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
  ]
)

    return(completion.choices[0].message.content)



def process_command(c):
    #
    # if "open google" in c.lower():
    #     webbrowser.open("https://google.com")
    #     speak("Opening Google")
    # elif "open facebook" in c.lower():
    #     webbrowser.open("https://facebook.com")
    #     speak("Opening Facebook")
    # elif "open linkedin" in c.lower():
    #     webbrowser.open("https://linkedin.com")
    #     speak("Opening LinkedIn")
    # elif "open youtube" in c.lower():
    #     webbrowser.open("https://youtube.com")
    #     speak("Opening YouTube")
    # elif "open news" in c.lower():
    #     webbrowser.open("https://jamuna.tv/?")
    #     speak("OPening news")
    # elif "open result" in c.lower():
    #     webbrowser.open("https://btebresultszone.com/results")
    #     speak("OPening result")
    #This code is for social media
    if c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    #This is for open any app 
    elif c.lower().startswith("open"):
        arif=c.lower().split(" ")[1]
        find=applibrary.app[arif]
        if find:
            webbrowser.open(find)
            speak(f"Opening {arif}")
        else:
            speak("Sorry I don't found this app")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=bd&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiprocces(c)
        speak(output) 


if __name__ == "__main__":
    speak("Hello Jarvis initialized")
    
    while True:
        print("Listening for wake word...")
        
        try:
            with sr.Microphone() as source:
                # Adjust microphone for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Say 'fiha' to activate...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                
            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")
            
            if word.lower() == "fiha":
                speak("Yes..")
                
                with sr.Microphone() as source:
                    print("Jarvis active... Speak your command")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=10)
                    
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                process_command(command)
                
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timed out")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")