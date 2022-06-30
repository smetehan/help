import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import smtplib
r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım")
        except sr.UnknownValueError:
            speak("sistem çalışmadı")
        return voice
def mailgönder(voice):
    if "e-posta gönder" in voice:
        mesaj = record("mesaj nedir")
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        speak("kullanıcı adını ve şifreni gir")
        a = str(input("kullanıcı adınız :"))
        b = str(input("şifreniz"))
        mail.login(a,b)
        c = input("gönderilecek adres :")
        mail.sendmail(a,c,mesaj)
        speak("gönderiliyorr")

def response(voice):
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    if "arama yap" in voice:
        search = record("ne aramak istiyorsun")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search+"için bulduklarım")


    if "ne haber" in voice:
        speak("iyiyim senden naber")
    if "tamamdır" in voice:
        speak("görüşürüz")
        exit()
    if "saat kaç" in voice:
        print(datetime.now().strftime("%H:%M:&S"))
def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("nasıl yardımcı olabilirim")
time.sleep(1)
while 1:
   voice = record()
   print(voice)
   response(voice)
   mailgönder(voice)