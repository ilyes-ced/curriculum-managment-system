# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogigvggp.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sqlite3,json
import os


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 430)
        Dialog.setStyleSheet(open(os.path.join(os.path.curdir, 'styles/style2.css')).read())
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(210, 250, 165, 41))
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(25, 250, 165, 41))
        self.buttonBox = QDialogButtonBox(self.widget_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 190, 0, 0))
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setMaximumSize(QSize(0, 0))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 401, 51))
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 15, 121, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.btn_close = QPushButton(self.widget_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(360, 15, 20, 20))
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(25, 70, 351, 41))
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 91, 16))
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 50, 40))
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(25, 110, 351, 41))
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 10, 91, 21))
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 50, 40))
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(25, 150, 351, 41))
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 10, 91, 20))
        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 50, 40))
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(25, 190, 351, 41))
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 10, 74, 21))
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 50, 40))
        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 359, 401, 71))
        self.pushButton = QPushButton(self.widget_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 20, 227, 30))
        self.pushButton_2 = QPushButton(self.widget_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(25, 20, 101, 30))
        self.comboBox_3 = QComboBox(self.widget_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(25, 300, 351, 41))
        self.buttonBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox.raise_()
        self.widget_3.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.widget_6.raise_()
        self.widget_7.raise_()
        self.widget_8.raise_()
        self.comboBox_3.raise_()
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)



        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(self.ff)
        self.btn_close.clicked.connect(self.ff)

        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore

        QMetaObject.connectSlotsByName(Dialog)

        self.comboBox.activated.connect(self.changed_teacher)
        self.comboBox_2.activated.connect(self.changed)
        self.comboBox_3.activated.connect(self.changed)




        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))




        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "confirm"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_5.setText(_translate("Dialog", "select teacher"))
        self.label_6.setText(_translate("Dialog", "Season"))
        self.label_7.setText(_translate("Dialog", "Class"))
        self.label_8.setText(_translate("Dialog", "Day"))
        self.label_9.setText(_translate("Dialog", "Time"))
  

        


    def ff(self):
        self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).click()

    def changed_teacher(self):
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute("select * from teachers where name=?",(self.comboBox.currentText(),))
        teachers = cur.fetchone()
        self.comboBox_2.setCurrentText(teachers[2])
        self.teacher = self.comboBox.currentText()
        self.subject = self.comboBox_2.currentText()
        self.classe = self.comboBox_3.currentText()

        
    def changed(self):
        self.teacher = self.comboBox.currentText()
        self.subject = self.comboBox_2.currentText()
        self.classe = self.comboBox_3.currentText()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
