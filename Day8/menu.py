import webbrowser
import speech_recognition as sr

print("Welcome to my tools")
print("Enter your requirements:", end="")

#ch=input()

r=sr.Recognizer()

with sr.Microphone() as source:
    print('start say...')
    audio=r.listen(source)
    print('speech done...')

ch= r.recognize_google(audio)

if("date" in ch) and ("run" in ch) or ("execute" in ch):
   webbrowser.open("http://192.168.0.106/cgi-bin/practice.py?x=date")
elif "calendar" in ch:
   webbrowser.open("http://192.168.0.106/cgi-bin/practice.py?x=cal")
else:
   print("not understand")