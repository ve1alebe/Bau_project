import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
import uuid
import hashlib


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def help_autor(idd, login, password):
    sqlite_connection = sqlite3.connect('secret_files.db')
    cursor = sqlite_connection.cursor()
    sqlite_insert_with_param = """INSERT INTO users
                              (id, username, password)
                              VALUES (?, ?, ?);"""
    data_tuple = (idd, login, password)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # greet = FirstMainForm()
    # greet.show()
    sys.exit(app.exec())


