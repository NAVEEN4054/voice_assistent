import speech_recognition as sr
import pyttsx3
import wikipedia 
import webbrowser
import datetime
import pywhatkit
import pyaudio

recognizer=sr.Recognizer()
machine=pyttsx3.init("sapi5")
voices = machine.getProperty("voices")

machine.setProperty('voice', voices[1].id) 

def speak(input):
    machine.say(input)
    machine.runAndWait()

def greet():
   hour=datetime.datetime.now().hour
   if 0<=hour<12:
      speak("Good Morning")
   elif 12<=hour<18:
      speak("Good Afternoon")
   else:
      speak("Good night")
   
def main():
 greet()
 print(" I am Quantum, How can i help you today")
 speak(" I am Quantum, How can i help you today")
 while True:
   
  try: 
   global command
   with sr.Microphone() as source:
        print("listening...")
        speech=recognizer.listen(source)
        command=recognizer.recognize_google(speech,language='en-in')
        command=command.lower()
        print("you said :",command)
  
   if "hello" in command:
      response="Hello mate!Nice to meet you."
      print(response)
      speak(response)
   elif "who are you" in command:
      response="My name is Quantum, I am virtual voice assistant"
      print("My name is Quantum, I am virtual voice assistant") 
      speak(response)  
   elif "How are you" in command:
      input=print("I am fine, How about you?")
      speak(input)
   elif "wikipedia" in command:
      speak("searching wikipedia...")
      command=command.replace("wikipedia",'')
      result=wikipedia.summary(command,2)
      speak(result)
      print(result)
   elif 'open youtube' in command:
      speak("opening youtube")
      webbrowser.open("youtube.com")
   elif 'open google' in command:
      speak("opening google")
      webbrowser.open("google.com")
   elif 'open chatgpt' in command:
      speak("opening chatgpt")
      webbrowser.open("https://chatgpt.com/")
   elif 'open github' in command:
      speak('opening github')
      webbrowser.open('https://github.com/NAVEEN4054/voice_assistent')   
   elif 'open stackoverflow' in command:
      speak("opening stackoverflow")
      webbrowser.open("stackoverflow.com")
   elif 'open spotify' in command:
      speak("opening spotify")
      webbrowser.open("spotify.com")   
   elif 'open whatsapp' in command:
      speak("opening whatsapp")
      webbrowser.open("https://web.whatsapp.com/")
   elif 'play' in command:
      speak("playing music")
      song=command.replace("play",'')
      pywhatkit.playonyt(song)
   elif 'local disk d' in command:
      speak("opening local disk D")
      webbrowser.open("D://")
   elif 'local disk c' in command:
      speak("opening local disk C")
      webbrowser.open("C://")
   elif 'local disk e' in command:
      speak("opening local disk E")
      webbrowser.open("E://")
   elif 'date' in command:

      date=datetime.datetime.now().strftime("%d \n %m \n %y")
      speak('Todays Date is'+date)  
   elif 'time' in command:
      time=datetime.datetime.now().strftime('%I:%M%p')  
      speak('present time is'+time) 
   else: 
      print("your question is not in my database")
      speak("your question is not in my database")
  except Exception as e:
   print("I didn't understand that.")  
   exit(0) 
main()


                               
