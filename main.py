import sys
import sqlite3
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIntValidator
import uuid
import hashlib
from main_form import Ui_Autorization
from second_form import Ui_Test


# id1 - ситаксис
# id2 - наборы элементов
# id3 - модули
# id4 - функции
# id5 - ооп
# id6 - работа с файлами
#


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def help_autor(login, password):
    sqlite_connection = sqlite3.connect('secret_files.db')
    cursor = sqlite_connection.cursor()
    sqlite_insert_with_param = """INSERT INTO users
                              (username, password)
                              VALUES (?, ?);"""
    data_tuple = (login, password)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    cursor.close()


def choose_random_id():
    rand_id = random.randint(0, 60)
    return rand_id


class FirstMainForm(QMainWindow, Ui_Autorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aut.clicked.connect(self.enter)  # функция входа
        self.reg.clicked.connect(self.regis)  # функция регистрации

    def regis(self):
        if self.reg_log.text() and self.reg_pas.text() and self.reg_rep_pas.text():
            if len(self.reg_pas.text()) >= 7:
                if self.reg_pas.text() == self.reg_rep_pas.text():
                    try:
                        login = self.reg_log.text()
                        password = self.reg_pas.text()
                        password = hash_password(password)
                        help_autor(login, password)
                        self.show_error.setText('Успешная регистрация!')
                    except Exception as e:
                        # print(e)
                        if str(e) == 'UNIQUE constraint failed: users.username':
                            self.show_error.setText('Пользователь с таким именем уже существует.')
                else:
                    self.show_error.setText('Пароли не совпадают.')
            else:
                self.show_error.setText('Минимальная длина пароля - 7 символов.')

        else:
            self.show_error.setText('Некорректные данные.')

    def enter(self):
        con = sqlite3.connect('secret_files.db')
        cur = con.cursor()
        check_username = self.aut_log.text()
        if self.aut_log.text() and self.aut_pass.text():
            try:
                username1 = cur.execute(f"SELECT username from users")
                for i in username1:
                    if i[0] == check_username:
                        susername = i[0]
                        password1 = cur.execute(f"""SELECT password from users WHERE username LIKE '{i[0]}';""")
                        for j in password1:
                            password = j[0]
            except Exception as e:
                print(e)  # я хочу спать
            try:
                if check_username == susername and check_password(password, self.aut_pass.text()):
                    greet.close()
                    work.show()
                # print(1)
                else:
                    self.show_error.setText('Неверный логин или пароль')
            except Exception as e:
                if str(e) == "local variable 'susername' referenced before assignment":
                    self.show_error.setText('Некорректные данные.')
        else:
            self.show_error.setText('Некорректные данные.')


class SecondMainForm(QWidget, Ui_Test):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit.clicked.connect(self.returnn)  # функция на главную

    def returnn(self):
        work.close()
        greet.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    greet = FirstMainForm()
    work = SecondMainForm()
    greet.show()
    sys.exit(app.exec())
