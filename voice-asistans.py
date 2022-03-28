import webbrowser
from datetime import datetime
import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import random
import os


r=sr.Recognizer()
def record(ask= False):
    with sr.Microphone() as sourse:
        if ask:
            speak(ask)
        audio = r.listen(sourse)
        voice=''
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım.")
        except sr.RequestError:
            speak("sistem çalışmıyor.")
        return voice

def response(voice):
    if "asistan" in voice:
        speak("efendim ")
    if "nasılsın" in voice:
        speak("iyiyim sen")
    if "İyiyim ben de" in voice:
        speak("Nasıl yardımcı olabilrim.")
    if "saat kaç" in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if "arama yap" in voice:
         search = record("ne aramak istiyorsun")
         url="https://google.com/search?q="+search
         webbrowser.get().open(url)
         speak(search+" için bulduklarım")
    if "tamamdır" in voice:
        speak("Görüşürüz..")
        exit()

def speak(string):
    tts = gTTS(string, lang="tr")
    rand= random.randint(1, 10000)
    file = "audio-" + str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("nasıl yardımcı olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
