from PyQt5.QtCore import Qt, QPoint, QSize, QEvent
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget

from main_thread import MainThread


class FramelessDragableWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 300)
        self.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.center()

        self.lbl = QLabel(self)
        self.movie = QMovie("images/kara_listening.gif")
        self.movie.setScaledSize(QSize(300, 300))
        self.lbl.setMovie(self.movie)
        self.lbl.sizeHint()
        self.installEventFilter(self)
        self.movie.start()
        self.lbl.setGeometry(0, 0, 300, 300)

        self.oldPos = self.pos()
        self.show()
        self.start_execution = MainThread()
        self.start_execution.change_gif_signal.connect(self.update_gif)
        self.start_execution.start()

    def sizeHint(self):
        return QSize(300, 300)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            # print("Mouse is over the label")
            self.stop = True
            return True
        elif event.type() == QEvent.Leave:
            # print("Mouse is not over the label")
            self.stop = False
        return False

    def update_gif(self, value):
        if value == 2:
            self.movie.setScaledSize(QSize(200, 200))
            self.lbl.setGeometry(0, 0, 200, 200)
            self.change_gif("images/robo_cat.gif")
        elif value == 3:
            self.movie.setScaledSize(QSize(300, 300))
            self.lbl.setGeometry(0, 0, 300, 300)
            self.change_gif("images/kara_logo-removebg-preview.png")
        else:
            self.movie.setScaledSize(QSize(300, 300))
            self.lbl.setGeometry(0, 0, 300, 300)
            self.change_gif("images/kara_listening.gif")

    def change_gif(self, gif_file):
        self.movie.stop()
        self.movie.setFileName(gif_file)
        self.movie.start()

    def closeEvent(self, event):
        self.start_execution.quit()
        self.start_execution.wait(1000)
        super().closeEvent(event)


"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FramelessDragableWidget()
    sys.exit(app.exec_())
"""