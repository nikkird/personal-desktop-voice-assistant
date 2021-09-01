import sys

import PyQt5.uic.pyuic
from PyQt5.QtCore import Qt, QPoint, QSize, QEvent
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget


class FramelessDragableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            print(PyQt5.uic.pyuic.Version)
            self.setFixedSize(200, 200)
            self.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            self.center()

            self.lbl = QLabel(self)
            self.movie = QMovie("elements/kara_ava_m.gif")
            self.movie.setScaledSize(QSize(100, 100))
            self.lbl.setMovie(self.movie)
            self.lbl.sizeHint()
            self.installEventFilter(self)
            self.movie.start()
            self.lbl.setGeometry(0, 0, 100, 100)

            self.oldPos = self.pos()
            self.show()
        except Exception as e:
            print(e)

    def sizeHint(self):
        return QSize(200, 200)

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
            print("Mouse is over the label")
            self.stop = True
            return True
        elif event.type() == QEvent.Leave:
            print("Mouse is not over the label")
            self.stop = False
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FramelessDragableWidget()
    sys.exit(app.exec_())