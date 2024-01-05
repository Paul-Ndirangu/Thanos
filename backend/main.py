from fastapi import FastAPI
import speech_recognition as sr 
import pyttsx3 as t

app = FastAPI()
r = sr.Recognizer()



@app.get("/")
def root():
    return {"Root."}


# Function to convert text to speech.
def speech_to_text(speech):
    # Initialize the engine
    engine = t.init()
    engine.say(speech)
    engine.runAndWait()


# Use the microphone as a source for speech input.
with sr. Microphone() as source2:
    # wait for a second to let the recognizer
    # adjust the energy threshold based on the
    # surrounding noise level
    
    r.adjust_for_ambient_noise(source2, duration=0.2)
    
    # Listens for the user's input
    audio2 = r.listen(source2)