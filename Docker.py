import speech_recognition as sr
import webbrowser
import pyttsx3
import getpass
print()
print("This Program launch and stop Docker container for You")
print()
pyttsx3.speak("Hello I am Jarvis")
pyttsx3.speak("I can Launch and Stop Docker Container for you")
pyttsx3.speak("Enter your password")
inpass = getpass.getpass ("Enter your password :")
apass = "nitesh"
if inpass!=apass:
    pyttsx3.speak("Incorrect Password Try Again ")
    exit()
pyttsx3.speak("Access Granted")
pyttsx3.speak("How can i help you") 
#while True:
r =sr.Recognizer()
with sr.Microphone() as source:
    print("I am Listening to You....")
    audio=r.listen(source)
    print("Done...")
    text=r.recognize_google(audio)
    print(text)

if ("run" in text) or ("launch" in text) and ("docker" in text) or ("container" in text):
    webbrowser.open("http://192.168.0.104/drun.html")
    pyttsx3.speak("Opening a Page Run Docker")
elif ("stop" in text) and ("docker" in text) or ("container" in text):
    webbrowser.open("http://192.168.0.104/docstop.html")
    pyttsx3.speak("Opening a Page stop Docker")    
elif ("run" in text) and ("linux" in text) or ("command" in text):
    webbrowser.open("http://192.168.0.104/command.html")
    pyttsx3.speak("Opening a Page Linux Command")
else:
    print("Sorry I cant understand")