import Task1
import pyttsx3
nm=input("Enter Your Name:-")
s =input("Enter A Greeting:-") 
Task1.greeting(s,nm)

e=pyttsx3.init()
# s=input("Enter A String:-")
e.say(s)
e.say(nm)
e.runAndWait()
