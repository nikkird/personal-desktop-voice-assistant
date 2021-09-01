import os
import re
import subprocess
import time

import winshell

from backend.stt import listen
from backend.tts import Speak, SlowSpeak
from res.credentials.credentials import cred


def empty_bin():
    Speak("do you really want to empty recycle bin")
    choice = listen()
    if choice == cred['kara_pass']:
        Speak("recycling bin wait")
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        # Speak("Recycle Bin Recycled")
    else:
        Speak("wrong password please try again")


def shutdown():
    Speak("Hold on a Sec   shutting down the system.")
    time.sleep(2)
    subprocess.call('shutdown/p/f')


def restart_():
    Speak("Restarting system")
    subprocess.call(["shutdown", "/r"])


def hibernate():
    Speak("Hibernating")
    subprocess.call("shutdown/h")


def open_file(command):
    if "word" in command:
        Speak("Opening Microsoft Word")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk')
    elif "powerpoint" in command:
        Speak("Opening Microsoft powerpoint")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk')
    elif "pdf" in command or "adobe" in command:
        Speak("Opening Adobe")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader XI.lnk')

    elif "figma" in command.lower() or "figma" in command:
        Speak("Opening Figma app")
        os.startfile("C:\\Users\\win\\AppData\\Local\\Figma\\Figma.exe")
        time.sleep(7.0)

    elif "atom" in command.lower():
        Speak("Opening atom editor")
        os.startfile("C:\\Users\\win\\Desktop\\atom.exe")
        time.sleep(7.0)

    elif "visual studio" in command.lower() or "v s code" in command.lower():
        Speak("Opening Microsoft visual studio editor")
        os.startfile("C:\\Program Files(x86)\\Microsoft Visual Studio 10.0\\Common7\\IDE\\devenv.exe")
        time.sleep(7.0)


    elif "calculator" in command.lower() or "cal c" in command:
        Speak("Opening calculator")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    elif "notepad" in command.lower():
        Speak("Opening notepad")
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    else:
        Speak("Application not available")


def close_file(command):
    if "word" in command:
        print("got here...calc close")
        os.system("taskkill /F /IM figma.exe")
        Speak("word closed")

    elif "powerpoint" in command:
        print("got here...calc close")
        os.system("taskkill /F /IM figma.exe")
        Speak("powerpoint closed")

    elif "pdf" in command or "adobe" in command:
        print("got here...calc close")
        os.system("taskkill /F /IM figma.exe")
        Speak("adobe closed")

    elif "visual studio" in command.lower() or "v s code" in command:
        # print("got here...figma close")
        os.system("taskkill /F /IM devenv.exe")
        Speak("figma closed")

    elif "figma" in command.lower() or "figma" in command:
        # print("got here...figma close")
        os.system("taskkill /F /IM figma.exe")
        Speak("figma closed")

    elif "atom" in command.lower():
        # print("got here...figma close")
        os.system("taskkill /F /IM atom.exe")
        Speak("atom closed")

    elif "calculator" in command.lower() or "cal c" in command:
        print("got here...calc close")
        os.system("taskkill /F /IM calculator.exe")
        Speak("calculator closed")

    elif "notepad" in command.lower():
        print("got here...notepad close")
        os.system("taskkill /F /IM notepad.exe")
        Speak("notepad closed")

    elif "google" in command.lower() or "chrome" in command.lower():
        print("got here...chrome close")
        os.system("taskkill /im chrome.exe /f")
        Speak("google chrome closed")

    else:
        Speak("Application not available")


def launch_app(command):
    reg_ex = re.search('launch (.*)', command)
    if reg_ex:
        Speak("opening")
        open_file(command)

    # Speak('I have launched the desired application')


def close_app(command):
    reg_ex = re.search('close (.*)', command)
    if reg_ex:
        Speak("closing")
        close_file(command)

    # Speak('I have launched the desired application')


def get_pronunciation():
    Speak("Please List out the spelling")
    list_of_char = listen()
    # SlowSpeak("Please List out the spelling, it is pronounced as 2")
    word = str(list_of_char).replace(" ", "")
    if word == "":
        list_of_char = listen()
        word = str(list_of_char).replace(" ", "")

    while True:
        Speak("it is pronounced as\n" + word)
        SlowSpeak(word)
        Speak("do you want me to repeat")
        res = listen()
        if "again" in res.lower() or "yes" in res.lower():
            continue
        else:
            break