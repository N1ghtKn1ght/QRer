# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

from Views.UI.Widgets.CardLineEdit import CardLineEdit
from Views.UI.Widgets.LineEdit import LineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(809, 587)
        MainWindow.setWindowTitle(u"QRer")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(37, 37, 37);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 251, 541))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 16))
        self.label.setStyleSheet(u"color: rgb(195, 195, 195);")
        self.Name = LineEdit(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(100, 20, 151, 31))
        self.Name.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"border-color: rgb(255, 0, 4);\n"
"border-color: rgb(50, 50, 50);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 20, 51, 31))
        self.label_2.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Surname = LineEdit(self.frame)
        self.Surname.setObjectName(u"Surname")
        self.Surname.setGeometry(QRect(100, 60, 151, 31))
        self.Surname.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 60, 71, 31))
        self.label_3.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 100, 71, 31))
        self.label_4.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Email = QLineEdit(self.frame)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(100, 100, 151, 31))
        self.Email.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 150, 101, 31))
        self.label_5.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Card = CardLineEdit(self.frame)
        self.Card.setObjectName(u"Card")
        self.Card.setGeometry(QRect(0, 190, 251, 31))
        self.Card.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"border-color: rgb(50, 50, 50);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 230, 121, 31))
        self.label_6.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 230, 91, 31))
        self.label_7.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.CVV = CardLineEdit(self.frame)
        self.CVV.setObjectName(u"CVV")
        self.CVV.setGeometry(QRect(140, 260, 101, 31))
        self.CVV.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"border-color: rgb(50, 50, 50);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Date = QDateTimeEdit(self.frame)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(0, 260, 131, 31))
        self.Date.setStyleSheet(u"color: rgb(150, 150, 150);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Date.setCurrentSection(QDateTimeEdit.MonthSection)
        self.Date.setCalendarPopup(True)
        self.Ready = QPushButton(self.frame)
        self.Ready.setObjectName(u"Ready")
        self.Ready.setGeometry(QRect(30, 320, 191, 51))
        self.Ready.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px; \n"
"border: 2px solid #094065;\n"
"background-color: rgb(91, 91, 91);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(270, 20, 531, 541))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.result = QLabel(self.frame_2)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(65, 0, 400, 400))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 531, 541))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.qrCode = QLabel(self.frame_3)
        self.qrCode.setObjectName(u"qrCode")
        self.qrCode.setGeometry(QRect(0, 0, 530, 400))
        self.save = QPushButton(self.frame_3)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(170, 460, 191, 51))
        self.save.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px; \n"
"border: 2px solid #094065;\n"
"background-color: rgb(91, 91, 91);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label.setText("")
        self.Name.setText("")
        self.Name.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.Surname.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Email.setText("")
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u043e\u0434\u044f \u0434\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u0440\u0442\u044b, \u0412\u044b \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0430\u0435\u0442\u0435, \u0447\u0442\u043e \u0432\u0441\u0435 \u0434\u0435\u043d\u044c\u0433\u0438 \u0441\u043f\u0438\u0448\u0443\u0442\u0441\u044f \u0441 \u0412\u0430\u0448\u0435\u0433\u043e \u0441\u0447\u0435\u0442\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.Card.setText("")
        self.Card.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CVV", None))
        self.CVV.setText("")
        self.CVV.setPlaceholderText("")
        self.Date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/yyyy", None))
        self.Ready.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.result.setText("")
        self.qrCode.setText("")
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        pass
    # retranslateUi

