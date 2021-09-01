from PyQt5.QtCore import QThread, pyqtSignal

from backend.assistant import assistant_response
from backend.stt import listen, sleep_now


class MainThread(QThread):
    change_gif_signal = pyqtSignal(int)

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        while True:
            self.change_gif_signal.emit(1)
            command = listen()
            # command = input("ask >>")
            if command != '' or command is None:
                self.change_gif_signal.emit(2)
                sleep_cmd = assistant_response(command)
                if "stop listening" in command:
                    self.change_gif_signal.emit(3)
                    sleep_now(sleep_cmd)



# run_assistant()

