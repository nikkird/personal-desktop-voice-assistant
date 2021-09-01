import re
import time
from backend.tts import Speak
import speech_recognition as sr


class STT:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            query = ""
            try:
                start_time = time.perf_counter()
                # time.clock()
                print("Listening...")
                audio = self.r.listen(source, 4, 10)
                self.r.energy_threshold = 350
                self.r.phrase_threshold = 0.2
                self.r.pause_threshold = 0.2
            except Exception as e:
                print(e)
        try:
            end_time = time.perf_counter()
            print("Listening - start time: " + str(start_time) + "\tend time: " + str(end_time))
            start_time = time.perf_counter()
            print("Recognizing...")
            query = self.r.recognize_google(audio, language='en')
            print(query)
            end_time = time.perf_counter()
            print("Recognizing - start time: " + str(start_time) + "\tend time: " + str(end_time))

        except Exception as e:
            # print(e)
            res = "Please say that again"
            # count = +1
            # print(count)
            print(res)
            Speak(res)
        return query


def sleep_command():
    print("got here")
    Speak("for how much time do you want me to stop taking commands")
    st = listen()
    st = str(st).lower()
    return st


def sleep_now(st):
    if "minute" in st or "minutes" in st:
        search_word = "minute"
        res = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), st)
        search_word = "minutes"
        res1 = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), st)
        if res:
            print(res.group(1))
        st = 60.0 * float(res.group(1))
        print("sleeping" + str(st))
        if res1:
            print(res1.group(1))
            st = 60.0 * float(res.group(1))
            print("sleeping" + str(st))
        time.sleep(st)

    elif "second" in st or "seconds" in st:
        search_word = "seconds"
        res = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), st)
        search_word = "second"
        res1 = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), st)
        if res:
            print(res.group(1))

        print("sleeping" + str(st))
        st = 1.0 * float(res.group(1))
        if res1:
            print(res1.group(1))
            st = 1.0 * float(res1.group(1))
        print("sleeping" + str(st))
        time.sleep(st)

    else:
        # st = st.replace("few seconds", "")
        time.sleep(10)

    print("done sleeping")


def listen():
    lis = STT()
    query = lis.listen()
    return query.lower()


def wake_listener():
    try:
        wake_word = listen()
        print("Recognizing...")
        if "kara" in wake_word.lower() or "cara" in wake_word.lower():
            query = listen()
            return query.lower()
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
