import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('subah ho gyi mamu jaago re')

    elif hour>=12 and hour<18:
        speak('good afternoon sir')

    else:
        speak('good evening sir')

    speak('please tell me how may i help you')

def takecommand():
    """
    it take command from user through microphone
    """
    r =sr.Recognizer
    with sr.Microphone() as source:
        print('listening........')
        r.pausethreshold = 1.5
        audio=r.listen(source)

    try:
        print('processing')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except execption as e:
        print('say that again please...')
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    takecommand()