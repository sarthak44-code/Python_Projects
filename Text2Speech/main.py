from gtts import gTTS
import os

file = open("text.txt")
Data = file.read()
language = 'en'

Audio = gTTS(text = Data, lang=language, slow=False)

Audio.save("aud.wav")
os.system("aud.wav")



