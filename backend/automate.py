import os
import random
import time
import pygame
import requests
import re
import urllib
import webbrowser
from datetime import datetime
from urllib import parse
from urllib.request import urlopen
import pyjokes as pyjokes
import wolframalpha as wolframalpha
from wikipedia import wikipedia
from pygame import mixer
from backend.stt import listen
from backend.tts import Speak

import pywhatkit


from res.credentials.credentials import cred


def youtube_query(domain):
    print("hey")
    query_string = urllib.parse.urlencode({"search_query": domain})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                html_content.read().decode())
    # returns all links in search result
    return search_results


def open_youtube(command):

    if "play" in command.lower():
        reg_ex = re.search("youtube (.+)", command)
        command = str(command).lower().replace("play on youtube", "")
        command = command.replace(" ", "+")
        print(command)
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={command}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print(video_ids)
        webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[1])
        time.sleep(5)

    elif "on youtube" in command.lower() or "in youtube" in command.lower():
        reg_ex = re.search("youtube (.+)", command)
        print(reg_ex)
        # driver = webdriver.Chrome(executable_path='chromedriver')
        Speak("Opening in youtube")
        indx = command.lower().split().index('youtube')
        query = command.split()[indx + 1:]
        # driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(query))
        time.sleep(5.00)
        return
    elif "open youtube and search" in command.lower() or "search" in command.lower():
        reg_ex = re.search("search (.+)", command)
        print(reg_ex)
        # driver = webdriver.Chrome(executable_path='chromedriver')
        Speak("Opening in youtube")
        indx = command.lower().split().index('search')
        query = command.split()[indx + 1:]
        # driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(query))
        # webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
    else:
        webbrowser.open("https://www.youtube.com")


def get_maps(query):
    query = query.replace("where is", "")
    location = query
    Speak("You asked to Locate")
    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    Speak(location)


def open_google(command):

    Speak("opening google")
    if 'open google' == command.lower():
        webbrowser.open("https://www.google.com")
    else:
        # driver = webdriver.Chrome(executable_path='chromedriver')
        # indx = command.lower().split().index('google')
        # query = command.split()[1]
        command = command.replace("open google and search", "")
        command = command.replace("search on google", "")
        command = command.replace("google", "")
        command = command.replace("search", "")
        # driver.get("https://www.google.com/search?q =" + '+'.join(query))
        webbrowser.open("https://www.google.com/search?q=" + command + "")


def open_sites(command):
    if 'goodreads' in command.lower() or 'good reads' in command.lower():
        webbrowser.open("https://www.goodreads.com/")
    elif 'wattpad' in command.lower() or 'what pad' in command.lower():
        webbrowser.open("https://www.wattpad.com/")
    elif 'gmail' in command.lower() or 'email' in command.lower():
        webbrowser.open("https://mail.google.com/")

    time.sleep(6)


def call_wiki(query):
    query = query.replace("wikipedia", "")
    query = query.replace("according to", "")
    if "who is" in query or "what is" in query:
        query = query.replace("who is", "")
        query = query.replace("what is", "")
    results = wikipedia.summary(query, sentences=3)
    if results != "":
        results = "According to Wikipedia" + str(results)
        Speak(results)
    else:
        Speak("can you repeat the command please")


def open_stackoverflow():
    webbrowser.open("https://www.stackoverflow.com")


def call_wolframalpha(query):
    query = query.lower()
    client = wolframalpha.Client(cred['wolfram_api_key'])
    if "calculate" in query:
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        Speak("The answer is " + answer)
    elif "what is" in query:
        indx = query.lower().split().index('what is')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("" + answer)
        Speak("" + answer)
    res = client.query(query)
    try:
        print(next(res.results).text)
        Speak(next(res.results).text)
    except StopIteration:
        print("No results")
        Speak("I am not sure")


def write_notes():
    Speak("What should I write, ")
    note = listen()
    Speak("Should I include date and time")
    res = listen()
    Speak("what should I name the file")
    name = listen()

    if name == "anything":
        name = "autonamed"
    else:
        name = name.replace(" ", "")
    file = open(f'output/{name}.txt', 'w')
    if 'yes' in res or 'sure' in res:
        strTime = datetime.now().strftime("%H: %M: %S")
        file.write(strTime + ":- \n" + note)
        Speak("Done")
    else:
        file.write(note)
        Speak("Done")


def get_notes():
    # speak("Showing Notes")
    fname = "demo.txt"
    file = open(f"output/{fname}", "r")
    Speak(file.readlines())
    # speak(file.read())


def get_jokes():
    Speak(pyjokes.get_joke())


def get_news():

    query_params = {
        "source": "the-times-of-india",
        "sortBy": "top",
        "apiKey": cred['news_api_key']
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    Speak(results)


# play_mp3() music with pygame function starts here
mixer.init()


def play_mp3(file_path):
    mixer.init()
    print("yes")
    files = os.listdir(file_path)
    d = random.choice(files)
    mixer.music.load(os.path.join(file_path, d))
    mixer.music.play()
    print("playing...")
    time.sleep(6)
    mixer.music.stop()
    return
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)


def pause_music():
    print("paused", end="\r")
    pygame.mixer.music.pause()


def unpause_music():
    print("unpaused", end="\r")
    pygame.mixer.music.unpause()


# def check_songs(song):

def play_songs(command):
    # path = 'F:\\songs\\new\\Talaash\\'
    Speak('Do you have any preference')
    preference = listen()
    if "yes" in preference.lower():
        Speak("What do you have in mind")
        command1 = listen()
        # play blank space
        song_name = command1.replace("play ", "")
        pywhatkit.playonyt(song_name)
        time.sleep(8.0)
    else:
        play_mp3('F:\\songs_\\')


def song_commands(command):
    if command == "pause":
        pause_music()
        return True

    elif command == "unpause":
        unpause_music()
        return True

    else:
        print("stoping...")
        pygame.mixer.music.stop()
        return False


def get_weather():
    # Google Open weather website
    # to get API of Open weather
    api_key = cred['weather_api_key']
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    Speak("which city")
    print("City name : ")
    city_name = listen()
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}"
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " + str(
            current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
            current_pressure) + "\n humidity (in percentage) = " + str(
            current_humidiy) + "\n description = " + str(weather_description))
        Speak(weather_description + "in" + city_name)
    else:
        Speak(" City Not Found ")