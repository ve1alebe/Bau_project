# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Autorization(object):
    def setupUi(self, Autorization):
        Autorization.setObjectName("Autorization")
        Autorization.resize(1170, 720)
        Autorization.setMinimumSize(QtCore.QSize(1170, 720))
        Autorization.setMaximumSize(QtCore.QSize(1170, 720))
        self.background = QtWidgets.QLabel(Autorization)
        self.background.setGeometry(QtCore.QRect(-6, -5, 1291, 731))
        self.background.setMinimumSize(QtCore.QSize(0, 0))
        self.background.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("Snapit-App-Background.png"))
        self.background.setObjectName("background")
        self.show_pas2 = QtWidgets.QLabel(Autorization)
        self.show_pas2.setGeometry(QtCore.QRect(670, 260, 71, 31))
        self.show_pas2.setObjectName("show_pas2")
        self.reg_rep_pas = QtWidgets.QLineEdit(Autorization)
        self.reg_rep_pas.setGeometry(QtCore.QRect(770, 320, 251, 31))
        self.reg_rep_pas.setObjectName("reg_rep_pas")
        self.aut = QtWidgets.QPushButton(Autorization)
        self.aut.setGeometry(QtCore.QRect(160, 310, 251, 31))
        self.aut.setObjectName("aut")
        self.show_pas = QtWidgets.QLabel(Autorization)
        self.show_pas.setGeometry(QtCore.QRect(80, 260, 71, 31))
        self.show_pas.setObjectName("show_pas")
        self.reg_pas = QtWidgets.QLineEdit(Autorization)
        self.reg_pas.setGeometry(QtCore.QRect(770, 260, 251, 31))
        self.reg_pas.setObjectName("reg_pas")
        self.pic = QtWidgets.QLabel(Autorization)
        self.pic.setGeometry(QtCore.QRect(430, 480, 261, 201))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("pc1.png"))
        self.pic.setObjectName("pic")
        self.just1 = QtWidgets.QLabel(Autorization)
        self.just1.setGeometry(QtCore.QRect(150, 150, 291, 31))
        self.just1.setObjectName("just1")
        self.show_login = QtWidgets.QLabel(Autorization)
        self.show_login.setGeometry(QtCore.QRect(80, 210, 61, 31))
        self.show_login.setObjectName("show_login")
        self.show_error = QtWidgets.QLabel(Autorization)
        self.show_error.setGeometry(QtCore.QRect(390, 400, 321, 61))
        self.show_error.setObjectName("show_error")
        self.reg_log = QtWidgets.QLineEdit(Autorization)
        self.reg_log.setGeometry(QtCore.QRect(770, 200, 251, 31))
        self.reg_log.setObjectName("reg_log")
        self.reg = QtWidgets.QPushButton(Autorization)
        self.reg.setGeometry(QtCore.QRect(770, 380, 251, 31))
        self.reg.setObjectName("reg")
        self.aut_log = QtWidgets.QLineEdit(Autorization)
        self.aut_log.setGeometry(QtCore.QRect(160, 210, 251, 31))
        self.aut_log.setObjectName("aut_log")
        self.greet_1 = QtWidgets.QLabel(Autorization)
        self.greet_1.setGeometry(QtCore.QRect(200, 40, 791, 61))
        self.greet_1.setObjectName("greet_1")
        self.aut_pass = QtWidgets.QLineEdit(Autorization)
        self.aut_pass.setGeometry(QtCore.QRect(160, 260, 251, 31))
        self.aut_pass.setObjectName("aut_pass")
        self.show_rep_pas = QtWidgets.QLabel(Autorization)
        self.show_rep_pas.setGeometry(QtCore.QRect(580, 320, 181, 31))
        self.show_rep_pas.setObjectName("show_rep_pas")
        self.show_login_2 = QtWidgets.QLabel(Autorization)
        self.show_login_2.setGeometry(QtCore.QRect(670, 200, 61, 31))
        self.show_login_2.setObjectName("show_login_2")
        self.just2 = QtWidgets.QLabel(Autorization)
        self.just2.setGeometry(QtCore.QRect(700, 150, 341, 31))
        self.just2.setObjectName("just2")

        self.retranslateUi(Autorization)
        QtCore.QMetaObject.connectSlotsByName(Autorization)

    def retranslateUi(self, Autorization):
        _translate = QtCore.QCoreApplication.translate
        Autorization.setWindowTitle(_translate("Autorization", "Приветствие"))
        self.show_pas2.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Пароль</span></p></body></html>"))
        self.aut.setText(_translate("Autorization", "Войти"))
        self.show_pas.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Пароль</span></p></body></html>"))
        self.just1.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Войди, если уже есть аккаунт</span></p></body></html>"))
        self.show_login.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Логин</span></p></body></html>"))
        self.show_error.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.reg.setText(_translate("Autorization", "Создать аккаунт"))
        self.greet_1.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:18pt;\">Система проверка знаний школьников по информатике</span></p></body></html>"))
        self.show_rep_pas.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Повторите пароль</span></p></body></html>"))
        self.show_login_2.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Логин</span></p></body></html>"))
        self.just2.setText(_translate("Autorization", "<html><head/><body><p><span style=\" font-size:12pt;\">Зарегистрируйся, если нет аккаунта</span></p></body></html>"))
# import aut_rc
# import pcc_rc
