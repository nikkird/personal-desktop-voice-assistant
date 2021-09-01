import random
from datetime import datetime
import holidays
from backend.tts import Speak


def call_time():
    strTime = datetime.now().strftime("%H:%M:%S")
    Speak(strTime)


def call_day():
    strTime = datetime.now().strftime("%A")
    print("in today.py:" + strTime)
    Speak(strTime)


def date_today():
    strTime = datetime.now().strftime("%B %d %Y")
    Speak(strTime)


def call_month():
    strTime = datetime.now().strftime("%B")
    Speak(strTime)


is_not_holiday = ["Today is not a holiday", "There is no holiday today", "There is no occasion today"]


def is_holiday():
    # getting India holidays
    india_holidays = holidays.India()
    date = datetime.now().strftime("%d-%m-%Y")
    if date in india_holidays:
        Speak(f"today is {india_holidays.get(date)}")
    else:
        Speak(random.choice(is_not_holiday))


