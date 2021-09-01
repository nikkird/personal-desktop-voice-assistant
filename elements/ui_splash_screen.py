from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PyQt5.QtGui import (QFont, QPalette, QBrush, QColor)
from PyQt5.QtWidgets import *


class UiSplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
                                            "border-radius: 150px;\n"
                                            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749"
                                            "rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                            "}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
                                      "	border-radius: 150px;\n"
                                      "	background-color: rgba(77, 77, 127, 120);\n"
                                      "}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
                                     "	border-radius: 135px;\n"
                                     "	background-color: rgb(77, 77, 127);\n"
                                     "}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 193, 191))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        """self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
                                      "color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle)"""
        # -------------
        """palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)"""


        self.logo = QPushButton(self.widget)
        self.logo.setGeometry(QRect(20, 20, 20, 20))
        # self.logo.setPalette(palette)
        self.logo.setToolTipDuration(-1)
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("background-image: url(elements/kara_logo-removebg-preview.png);")
        # self.logo.setStyleSheet("background-image: url(:/newPrefix/kara_logo-removebg-preview.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")

        self.gridLayout.addWidget(self.logo)

        # --------------

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(30)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
                                           "color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage)

        self.labelLoadingInfo = QLabel(self.widget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.labelLoadingInfo.setFont(font2)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
                                            "	border-radius: 10px;	\n"
                                            "	background-color: rgb(93, 93, 154);\n"
                                            "	color: #FFFFFF;\n"
                                            "	margin-left: 40px;\n"
                                            "	margin-right: 40px;\n"
                                            "}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo)

        self.labelCredits = QLabel(self.widget)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
                                        "color: rgb(155, 155, 255);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    #
    #

    # setupUi
    def retranslateUi(self, SplashScreen):

        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))

        """self.labelTitle.setText(QCoreApplication.translate("SplashScreen",
                                                           u"<html><head/><body><p>"
                                                           u"<span style=\" font-weight:600; "
                                                           u"color:#9b9bff;\">YOUR</span> APPLICATION NAME</p>"
                                                           u"</body></html>",
                                                           None))"""
        """self.labelPercentage.setText(QCoreApplication.translate("SplashScreen",
                                                                u"<p><span style=\" font-size:30pt;\">0</span>"
                                                                u"<span style=\" font-size:30pt; "
                                                                u"vertical-align:super;\">%</span></p>",
                                                                None))"""
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"by: NSP", None))
    # retranslateUi
