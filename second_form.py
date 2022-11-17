# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(1170, 720)
        Test.setMinimumSize(QtCore.QSize(1170, 720))
        Test.setMaximumSize(QtCore.QSize(1170, 720))
        self.background = QtWidgets.QLabel(Test)
        self.background.setGeometry(QtCore.QRect(-6, -5, 1181, 731))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("Snapit-App-Background.png"))
        self.background.setObjectName("background")
        self.name = QtWidgets.QLabel(Test)
        self.name.setGeometry(QtCore.QRect(10, 20, 271, 41))
        self.name.setObjectName("name")
        self.l_gen = QtWidgets.QLabel(Test)
        self.l_gen.setGeometry(QtCore.QRect(90, 250, 301, 81))
        self.l_gen.setObjectName("l_gen")
        self.create = QtWidgets.QPushButton(Test)
        self.create.setGeometry(QtCore.QRect(120, 370, 231, 101))
        self.create.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.create.setObjectName("create")
        self.exit = QtWidgets.QPushButton(Test)
        self.exit.setGeometry(QtCore.QRect(10, 120, 231, 51))
        self.exit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.exit.setObjectName("exit")
        self.rating_2 = QtWidgets.QLabel(Test)
        self.rating_2.setGeometry(QtCore.QRect(760, 190, 281, 61))
        self.rating_2.setObjectName("rating_2")
        self.error_text = QtWidgets.QLabel(Test)
        self.error_text.setGeometry(QtCore.QRect(60, 590, 381, 61))
        self.error_text.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.error_text.setText("")
        self.error_text.setObjectName("error_text")
        self.comp = QtWidgets.QLabel(Test)
        self.comp.setGeometry(QtCore.QRect(940, 10, 211, 151))
        self.comp.setText("")
        self.comp.setPixmap(QtGui.QPixmap("pc1.png"))
        self.comp.setObjectName("comp")
        self.groupBox_3 = QtWidgets.QGroupBox(Test)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 260, 611, 291))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_topic = QtWidgets.QLabel(self.groupBox)
        self.label_topic.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic.setObjectName("label_topic")
        self.verticalLayout.addWidget(self.label_topic)
        self.num_synt = QtWidgets.QSpinBox(self.groupBox)
        self.num_synt.setObjectName("num_synt")
        self.verticalLayout.addWidget(self.num_synt)
        self.label_topic_2 = QtWidgets.QLabel(self.groupBox)
        self.label_topic_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic_2.setObjectName("label_topic_2")
        self.verticalLayout.addWidget(self.label_topic_2)
        self.num_oop = QtWidgets.QSpinBox(self.groupBox)
        self.num_oop.setObjectName("num_oop")
        self.verticalLayout.addWidget(self.num_oop)
        self.label_topic_3 = QtWidgets.QLabel(self.groupBox)
        self.label_topic_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic_3.setObjectName("label_topic_3")
        self.verticalLayout.addWidget(self.label_topic_3)
        self.nummod = QtWidgets.QSpinBox(self.groupBox)
        self.nummod.setObjectName("nummod")
        self.verticalLayout.addWidget(self.nummod)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_topic_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_topic_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic_4.setObjectName("label_topic_4")
        self.verticalLayout_2.addWidget(self.label_topic_4)
        self.num_func = QtWidgets.QSpinBox(self.groupBox_2)
        self.num_func.setObjectName("num_func")
        self.verticalLayout_2.addWidget(self.num_func)
        self.label_topic_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_topic_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic_5.setObjectName("label_topic_5")
        self.verticalLayout_2.addWidget(self.label_topic_5)
        self.num_files = QtWidgets.QSpinBox(self.groupBox_2)
        self.num_files.setObjectName("num_files")
        self.verticalLayout_2.addWidget(self.num_files)
        self.label_topic_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_topic_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_topic_6.setObjectName("label_topic_6")
        self.verticalLayout_2.addWidget(self.label_topic_6)
        self.num_list = QtWidgets.QSpinBox(self.groupBox_2)
        self.num_list.setObjectName("num_list")
        self.verticalLayout_2.addWidget(self.num_list)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.create_2 = QtWidgets.QPushButton(Test)
        self.create_2.setGeometry(QtCore.QRect(710, 570, 231, 101))
        self.create_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.create_2.setObjectName("create_2")

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "Информатика"))
        self.name.setText(_translate("Test", "<html><head/><body><p><span style=\" font-size:14pt;\">Ваше имя:</span></p></body></html>"))
        self.l_gen.setText(_translate("Test", "<html><head/><body><p><span style=\" font-size:14pt;\">Сгенерировать вариант</span></p><p><span style=\" font-size:14pt;\"></span></p></body></html>"))
        self.create.setText(_translate("Test", "Создать вариант!"))
        self.exit.setText(_translate("Test", "Выйти"))
        self.rating_2.setText(_translate("Test", "<html><head/><body><p><span style=\" font-size:14pt;\">Создать вариант вручную</span></p></body></html>"))
        self.label_topic.setText(_translate("Test", "Работа с кодом"))
        self.label_topic_2.setText(_translate("Test", "ООП"))
        self.label_topic_3.setText(_translate("Test", "Модули"))
        self.label_topic_4.setText(_translate("Test", "Функции"))
        self.label_topic_5.setText(_translate("Test", "Работа с файлами"))
        self.label_topic_6.setText(_translate("Test", "Наборы элементов"))
        self.create_2.setText(_translate("Test", "Создать вариант!"))
