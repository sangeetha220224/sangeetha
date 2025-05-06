import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def respond(command):
    if 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif 'stop' in command or 'exit' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I can tell the time or open Google. Try saying one of those.")
    return True

# Start assistant
speak("Hello! I am your voice assistant.")
while True:
    command = listen()
    if command:
        if not respond(command):
            break
