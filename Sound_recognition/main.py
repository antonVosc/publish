import speech_recognition as sr

recogniser = sr.Recognizer()
sound = sr.AudioFile('test_rec.wav')

with sound as source:
    audio = recogniser.record(source)

text = recogniser.recognize_google(audio)
print(text)