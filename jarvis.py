import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak('Good morning vivek..!!')

    elif hour>=12 and hour<18:
       speak('Good Afternoon vivek...!!')

    else:
        speak('Good evening Vivek....!!')

    speak(" Hi, I'm ultron. Speed 1 terahertz, memory 1 zigabyte. . How may i help you")  

def takeCommand():
   # It takes microphone input from the user and returns string output 

   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listning...")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" user said: {query}\n ")

   except Exception as e:
       print(e)
       print("say that again please....")
       return"None"

   return query
   
if __name__ =="__main__":
    wish()
    while True:

      query = takeCommand().lower()

      if 'wikipedia' in query:
        speak('searching wikipedia...')
        query= query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
      
      elif 'open youtube' in query:
         webbrowser.open("youtube.com")


      elif 'play music' in query:
         music_dir='D:\\Wondershare UniConverter 13\\Downloaded'
         # music_dir=random.randint(0,2)
         songs=os.listdir(music_dir)
         print (songs)
         os.startfile(os.path.join(music_dir,songs[1]))
