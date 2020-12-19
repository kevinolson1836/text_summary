import speech_recognition as sr
r = sr.Recognizer()

hellow=sr.AudioFile("audio_only (1).wav")
with hellow as source:
    audio = r.record(source)
try:
    s = r.recognize(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
