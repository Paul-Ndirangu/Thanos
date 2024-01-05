import speech_recognition as sr

r = sr.Recognizer()

# Works with aduio files
harvard = sr.AudioFile('audio/sample1.wav')

with harvard as source:
    audio = r.record(source)

type(audio)
r.recognize_google(audio)    
    