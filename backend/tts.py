import pyttsx3


class STT:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)


class Speak(STT):
    def __init__(self, phrase):
        super().__init__()
        self.speak_(phrase)

    def speak_(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()


class SlowSpeak(STT):
    def __init__(self, phrase):
        super().__init__()
        self.phrase = phrase

    def speak_(self, phrase):
        newVoiceRate = 100
        self.engine.setProperty('rate', newVoiceRate)
        self.engine.say(phrase)
        self.engine.runAndWait()
