import speech_recognition as sr
import pyttsx3  # reply to our command
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()  # listen to our command
engine=pyttsx3.init() #this command speaks
voices=engine.getProperty("voices")
voices=engine.setProperty("voice",voices[1].id)  # female voice setup
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...") # know when to speak
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' or 'hey' in command:
                command=command.replace('alexa','You,')
                print(command)
            return command
    except:
        talk("please say something. i am not able to listen to you... sorry i am exiting")
        exit()

def run_alexa():
    command=take_command()
    if 'play' in command:
        song = command
        talk('playing' + song)
        # print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('current time is'+time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    else:
        pass

while True:
    run_alexa()