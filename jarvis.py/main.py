import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import gaana



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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print('processing')
        query=r.recognize_google(audio,language='en-in')
        print(f"You: {query}\n")

    except Exception as e:
        print('say that again please...')
        speak('say that again please...')
        return "None"
    return query

# def playsong(song_name):
#     """
#     play music from web browser
#     """
#     print('what song do you want to play sir')
#     speak('what song do you want to play sir')
#     play=takecommand()
#     if audio in play:
#         song_name=song_name.replace('','%20')
#         url='https://gaana.com/search/{}'.format(song_name)
#         source_code=requests.get(url)
#         plain_text=source_code.text
#         soup= Beautifulsoup(plain_text, 'html.parser')
#     elif 'video' in query:
#         url='http://www.youtube.com/results?search_query='
#         temp=song_name.replace(' ','+')
#         url=url+temp
#         source_code=requests.get(url)
#         plain_text=source_code.text
#         soup= Beautifulsoup(plain_text, 'html.parser')

#         url_list=[]
#         for line in soup.findall('a',{'dir':"ltr"}):
#             href=link.get('href')
#             if '/watch?'in href:
#                 url_list.append(href)
#         webbrowser.open(yt_url+url_list[0])

#     else:
#         er="please say again"

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

         #logic for tasks performed by jarvis
        if 'wikipedia' in query:
            speak('ok searching wikipedia..')
            query=query.replace("wikipedia",'')
            result = wikipedia.summary(query, sentences=3)
            speak("acording to wikipedia...")
            print(result)
            speak(result)

        elif 'youtube' in query:
            speak("ok opening youtube..")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("ok opening google..")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strftime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            speak("playing music")
            webbrowser.open("https://www.youtube.com/watch?v=Ps4aVpIESkc&list")

        elif 'go to sleep' in query:
            speak('ok goodbye sir')
            exit()

        elif 'shutdown' in query:
            os.system('shutdown -s')

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()

        elif 'play song' in query:
            gaana.playsong()

        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)