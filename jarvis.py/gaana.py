from bs4 import BeautifulSoup

def playsong(song_name):
    """
    play music from web browser
    """
    print('what song do you want to play sir')
    speak('what song do you want to play sir')
    play=takecommand()
    if audio in play:
        song_name=song_name.replace('','%20')
        url='https://gaana.com/search/{}'.format(song_name)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup= Beautifulsoup(plain_text, 'html.parser')
    elif 'video' in query:
        url='http://www.youtube.com/results?search_query='
        temp=song_name.replace(' ','+')
        url=url+temp
        source_code=requests.get(url)
        plain_text=source_code.text
        soup= Beautifulsoup(plain_text, 'html.parser')

        url_list=[]
        for line in soup.findall('a',{'dir':"ltr"}):
            href=link.get('href')
            if '/watch?'in href:
                url_list.append(href)
        webbrowser.open(yt_url+url_list[0])

    else:
        er="please say again"
