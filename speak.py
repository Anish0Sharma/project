import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("goodmorning!")
    elif hour>12 and hour<18:
        speak("good afternoon!")
    else :
        speak("good evening")
    speak("i am anuj sir. please tell me how may i help you")


def takeCommond():
    r = sr.Recognizer() 

    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("reconiging...")
        query=r.recognize_google(audio, language='en_in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please..")
        return "None"

    return query



def sendMail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail.com','your_password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommond().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia"," ")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak("result")

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        #elif'play music' in query:
            #music_dir='path of songs'
            #songs=os.listdir(music_dir)
            #print(song)
            #os.start(os.path.join(music_dir,songs[0]))

        elif'the time' in query:
            strTime=datetime.dayetime.now().strftime("%H:%M:%S")
            speak(f"str,the time{strTime}")

        elif'open code' in query:
            codePath="G:\python"

        elif "email to anish" in query:
            try:
                speak("what should i say?")
                content=takeCommond()
                to="anishsharma939@gmail.com"
                sendMail(to,content)
                speak("email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry sir")
