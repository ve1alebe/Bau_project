import sys
import sqlite3
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
import uuid
import hashlib

from PyQt5 import QtWidgets

from main_form1 import Ui_Autorization
from second_form import Ui_Test
from third1 import Ui_Checker
from fourth1 import Ui_End
from er import Ui_Dialog


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


class FirstMainForm(QMainWindow, Ui_Autorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aut.clicked.connect(self.enter)  # функция входа
        self.reg.clicked.connect(self.regis)  # функция регистрации
        self.aut_check.toggled.connect(self.showpassword_aut)
        self.reg_check.toggled.connect(self.showpassword_reg)
        self.reg_pas_check.toggled.connect(self.showpassword_reg_rep)

    def showpassword_aut(self):
        self.aut_pass.setEchoMode(
            QtWidgets.QLineEdit.Normal if self.aut_check.isChecked() else QtWidgets.QLineEdit.Password)

    def showpassword_reg(self):
        self.reg_pas.setEchoMode(
            QtWidgets.QLineEdit.Normal if self.reg_check.isChecked() else QtWidgets.QLineEdit.Password)

    def showpassword_reg_rep(self):
        self.reg_rep_pas.setEchoMode(
            QtWidgets.QLineEdit.Normal if self.reg_pas_check.isChecked() else QtWidgets.QLineEdit.Password)

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
                            self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                else:
                    self.show_error.setText('Пароли не совпадают.')
                    self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
            else:
                self.show_error.setText('Минимальная длина пароля - 7 символов.')
                self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")

        else:
            self.show_error.setText('Некорректные данные.')
            self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")

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
                    greet.hide()
                    work.name.setText(f'Имя: {check_username}')
                    work.name.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
                    work.show()
                # print(1)
                else:
                    self.show_error.setText('Неверный логин или пароль')
                    self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
            except Exception as e:
                if str(e) == "local variable 'susername' referenced before assignment":
                    self.show_error.setText('Некорректные данные.')
                    self.show_error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        else:
            self.show_error.setText('Некорректные данные.')
            self.show_error.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")


class SecondMainForm(QWidget, Ui_Test):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.returnn)  # функция на главную
        self.create_2.clicked.connect(self.create2)  # функция создания по темам
        self.create.clicked.connect(self.creatte)  # функция создания рандомного теста
        self.check = True

    def returnn(self):
        work.close()
        greet.show()

    def create2(self):
        if self.num_synt.text() == '0' and self.num_func.text() == '0' and self.num_oop.text() == '0' \
                and self.num_files.text() == '0' and self.nummod.text() == '0' and self.num_list.text() == '0':
            self.error_text.setText('Вы не выбрали вопросы.')
        elif int(self.num_synt.text()) >= 8 or int(self.num_list.text()) >= 10 or int(self.nummod.text()) >= 11 or int(
                self.num_func.text()) >= 18 or int(self.num_oop.text()) >= 8 or int(self.num_files.text()) >= 12:
            self.error_text.setText('Слишком много вопросов')
        else:
            work.close()
            self.check = True
            test.show()

    def creatte(self):
        work.close()
        self.check = False
        test.show()


class ThirdMainForm(QWidget, Ui_Checker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.next_que.clicked.connect(self.next)  # функция дальше
        self.next_que_2.clicked.connect(self.skip)  # функция пропуск вопроса
        self.next_que_3.clicked.connect(self.begin)  # функция начала
        self.ans0.hide()
        self.ans0.hide()
        self.ans1.hide()
        self.ans2.hide()
        self.ans3.hide()
        self.next_que.hide()
        self.next_que_2.hide()
        self.question_text.hide()
        self.que = []
        self.answ = []
        self.count = 0
        self.aim = 0

    def begin(self):
        self.answ = []
        self.que = []
        self.aim = 0
        con = sqlite3.connect('secret_files.db')
        cur = con.cursor()
        result = cur.execute(f"""SELECT syn_mistakes, oop_mistakes, files_mistakes, modules_mistakes, func_mistakes,
                                    lists_mistakes FROM users WHERE username LIKE '{greet.aut_log.text()}'""")
        for i in result:
            self.syn = i[0]
            self.oop = i[1]
            self.files = i[2]
            self.mod = i[3]
            self.func = i[4]
            self.lists = i[5]
        rate = cur.execute(f"""SELECT rate FROM users WHERE username LIKE '{greet.aut_log.text()}'""")
        for i in rate:
            rating = i[0]
        if work.check:
            try:
                last_len = 0
                con = sqlite3.connect('secret_files.db')
                cur = con.cursor()
                list_id = []
                if work.num_func.text() != '0':
                    all_id_list = []
                    num_que = int(work.num_func.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 4""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                    last_len = len(list_id)
                if work.num_synt.text() != '0':
                    all_id_list = []
                    num_que = int(work.num_synt.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 1""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != last_len + num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                    last_len = len(list_id)
                if work.num_list.text() != '0':
                    all_id_list = []
                    num_que = int(work.num_list.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 2""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != last_len + num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                    last_len = len(list_id)
                if work.nummod.text() != '0':
                    all_id_list = []
                    num_que = int(work.nummod.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 3""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != last_len + num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                    last_len = len(list_id)
                if work.num_oop.text() != '0':
                    all_id_list = []
                    num_que = int(work.num_oop.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 5""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != last_len + num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                    last_len = len(list_id)
                if work.num_files.text() != '0':
                    all_id_list = []
                    num_que = int(work.num_files.text())
                    all_id = cur.execute(f"""SELECT question_id from tasks WHERE topic_id = 6""")
                    for j in all_id:
                        all_id_list.append(j[0])
                    while len(list_id) != last_len + num_que:
                        prob_id = random.choice(all_id_list)
                        if prob_id not in list_id:
                            list_id.append(prob_id)
                        else:
                            continue
                self.que = list_id
                random.shuffle(self.que)
            except Exception as e:
                #print(e)
                er.show()
        elif not work.check:
            try:
                self.sp = []
                self.sp.append(self.syn)
                self.sp.append(self.lists)
                self.sp.append(self.mod)
                self.sp.append(self.func)
                self.sp.append(self.oop)
                self.sp.append(self.files)
                # print(self.sp)
                # print(max(self.sp))
                # self.sp.remove(max(self.sp))
                # print(self.sp)
                # most_mist = max(self.sp)
                # most_id = self.sp.index(most_mist) + 1
                list_id = []
                last_len = 0
                for i in range(6):
                    all_id_list = []
                    # print(self.sp)
                    most_mist = self.sp.index(max(self.sp)) + 1
                    # print(most_mist, max(self.sp))
                    con = sqlite3.connect('secret_files.db')
                    cur = con.cursor()
                    result = f"""SELECT question_id from tasks WHERE topic_id = '{most_mist}'"""
                    # print(result)
                    first_mist = cur.execute(result)
                    for j in first_mist:
                        all_id_list.append(j[0])
                    # print(self.sp[most_mist - 1])
                    if self.sp[most_mist - 1] >= 50:
                        # print(3)
                        while len(list_id) != last_len + 3:
                            prob_id = random.choice(all_id_list)
                            if prob_id not in list_id:
                                list_id.append(prob_id)
                            else:
                                continue
                        last_len = len(list_id)
                    elif 25 <= self.sp[most_mist - 1] < 50:
                        while len(list_id) != last_len + 2:
                            prob_id = random.choice(all_id_list)
                            if prob_id not in list_id:
                                list_id.append(prob_id)
                            else:
                                continue
                        last_len = len(list_id)
                    elif 10 <= self.sp[most_mist - 1] < 25:
                        # print(1)
                        while len(list_id) != last_len + 1:
                            prob_id = random.choice(all_id_list)
                            if prob_id not in list_id:
                                list_id.append(prob_id)
                            else:
                                continue
                        last_len = len(list_id)
                    elif 10 > self.sp[most_mist - 1]:
                        #  print(1)
                        while len(list_id) != last_len + 1:
                            prob_id = random.choice(all_id_list)
                            if prob_id not in list_id:
                                list_id.append(prob_id)
                            else:
                                continue
                        last_len = len(list_id)
                    self.sp[most_mist - 1] = -99

                #  print(list_id)
                self.que = list_id
                # print(self.que)
                random.shuffle(self.que)

            except Exception as e:
               # print(e)
               er.show()

        con = sqlite3.connect('secret_files.db')
        cur = con.cursor()
        question = cur.execute(f"""SELECT question from tasks WHERE question_id = '{self.que[self.count]}'""")
        for i in question:
            tek_question = i[0]
        answers = cur.execute(f"""SELECT answers from tasks WHERE question_id = '{self.que[self.count]}'""")
        for i in answers:
            tek_answers = i[0]
            tek_answers = tek_answers.split('-')
        correct_answer = cur.execute(
            f"""SELECT correct_answer from tasks WHERE question_id = '{self.que[self.count]}'""")
        for i in correct_answer:
            self.tek_correct = i[0]
        self.ans0.show()
        self.ans0.setText(tek_answers[0])
        self.ans1.show()
        self.ans1.setText(tek_answers[1])
        self.ans2.show()
        self.ans2.setText(tek_answers[2])
        self.ans3.show()
        self.ans3.setText(tek_answers[3])
        self.next_que.show()
        self.next_que_2.show()
        self.question_text.show()
        self.question_text.setText(f'{tek_question}')
        self.next_que_3.hide()

    def next(self):
        try:
            if self.ans0.isChecked() or self.ans1.isChecked() or self.ans2.isChecked() or self.ans3.isChecked():
                if self.ans0.isChecked():
                    if int(self.tek_correct) == 0:
                        self.aim += 1
                        self.answ.append(f'№{self.count + 1} - верно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        low_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in low_mist1:
                            low_mist = i[0]
                        if low_mist == 1:
                            self.syn -= 1
                            if self.syn <= 0:
                                self.syn = 0
                        elif low_mist == 2:
                            self.lists -= 1
                            if self.lists <= 0:
                                self.lists = 0
                        elif low_mist == 3:
                            self.mod -= 1
                            if self.mod <= 0:
                                self.mod = 0
                        elif low_mist == 4:
                            self.func -= 1
                            if self.func <= 0:
                                self.func = 0
                        elif low_mist == 5:
                            self.oop -= 1
                            if self.oop <= 0:
                                self.oop = 0
                        elif low_mist == 6:
                            self.files -= 1
                            if self.files <= 0:
                                self.files = 0
                    else:
                        self.answ.append(f'№{self.count + 1} - неверно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        add_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in add_mist1:
                            add_mist = i[0]
                        if add_mist == 1:
                            self.syn += 3
                        elif add_mist == 2:
                            self.lists += 3
                        elif add_mist == 3:
                            self.mod += 3
                        elif add_mist == 4:
                            self.func += 3
                        elif add_mist == 5:
                            self.oop += 3
                        elif add_mist == 6:
                            self.files += 3
                elif self.ans1.isChecked():
                    if int(self.tek_correct) == 1:
                        self.aim += 1
                        self.answ.append(f'№{self.count + 1} - верно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        low_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in low_mist1:
                            low_mist = i[0]
                        if low_mist == 1:
                            self.syn -= 1
                            if self.syn <= 0:
                                self.syn = 0
                        elif low_mist == 2:
                            self.lists -= 1
                            if self.lists <= 0:
                                self.lists = 0
                        elif low_mist == 3:
                            self.mod -= 1
                            if self.mod <= 0:
                                self.mod = 0
                        elif low_mist == 4:
                            self.func -= 1
                            if self.func <= 0:
                                self.func = 0
                        elif low_mist == 5:
                            self.oop -= 1
                            if self.oop <= 0:
                                self.oop = 0
                        elif low_mist == 6:
                            self.files -= 1
                            if self.files <= 0:
                                self.files = 0
                    else:
                        self.answ.append(f'№{self.count + 1} - неверно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        add_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in add_mist1:
                            add_mist = i[0]
                        if add_mist == 1:
                            self.syn += 3
                        elif add_mist == 2:
                            self.lists += 3
                        elif add_mist == 3:
                            self.mod += 3
                        elif add_mist == 4:
                            self.func += 3
                        elif add_mist == 5:
                            self.oop += 3
                        elif add_mist == 6:
                            self.files += 3
                elif self.ans2.isChecked():
                    if int(self.tek_correct) == 2:
                        self.aim += 1
                        self.answ.append(f'№{self.count + 1} - верно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        low_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in low_mist1:
                            low_mist = i[0]
                        if low_mist == 1:
                            self.syn -= 1
                            if self.syn <= 0:
                                self.syn = 0
                        elif low_mist == 2:
                            self.lists -= 1
                            if self.lists <= 0:
                                self.lists = 0
                        elif low_mist == 3:
                            self.mod -= 1
                            if self.mod <= 0:
                                self.mod = 0
                        elif low_mist == 4:
                            self.func -= 1
                            if self.func <= 0:
                                self.func = 0
                        elif low_mist == 5:
                            self.oop -= 1
                            if self.oop <= 0:
                                self.oop = 0
                        elif low_mist == 6:
                            self.files -= 1
                            if self.files <= 0:
                                self.files = 0
                    else:
                        self.answ.append(f'№{self.count + 1} - неверно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        add_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in add_mist1:
                            add_mist = i[0]
                        if add_mist == 1:
                            self.syn += 3
                        elif add_mist == 2:
                            self.lists += 3
                        elif add_mist == 3:
                            self.mod += 3
                        elif add_mist == 4:
                            self.func += 3
                        elif add_mist == 5:
                            self.oop += 3
                        elif add_mist == 6:
                            self.files += 3
                elif self.ans3.isChecked():
                    if int(self.tek_correct) == 3:
                        self.aim += 1
                        self.answ.append(f'№{self.count + 1} - верно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        low_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in low_mist1:
                            low_mist = i[0]
                        if low_mist == 1:
                            self.syn -= 1
                            if self.syn <= 0:
                                self.syn = 0
                        elif low_mist == 2:
                            self.lists -= 1
                            if self.lists <= 0:
                                self.lists = 0
                        elif low_mist == 3:
                            self.mod -= 1
                            if self.mod <= 0:
                                self.mod = 0
                        elif low_mist == 4:
                            self.func -= 1
                            if self.func <= 0:
                                self.func = 0
                        elif low_mist == 5:
                            self.oop -= 1
                            if self.oop <= 0:
                                self.oop = 0
                        elif low_mist == 6:
                            self.files -= 1
                            if self.files <= 0:
                                self.files = 0
                    else:
                        self.answ.append(f'№{self.count + 1} - неверно')
                        con = sqlite3.connect('secret_files.db')
                        cur = con.cursor()
                        add_mist1 = cur.execute(
                            f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
                        for i in add_mist1:
                            add_mist = i[0]
                        if add_mist == 1:
                            self.syn += 3
                        elif add_mist == 2:
                            self.lists += 3
                        elif add_mist == 3:
                            self.mod += 3
                        elif add_mist == 4:
                            self.func += 3
                        elif add_mist == 5:
                            self.oop += 3
                        elif add_mist == 6:
                            self.files += 3
                self.count += 1
                con = sqlite3.connect('secret_files.db')
                cur = con.cursor()
                question = cur.execute(f"""SELECT question from tasks WHERE question_id = '{self.que[self.count]}'""")
                for i in question:
                    tek_question = i[0]
                answers = cur.execute(f"""SELECT answers from tasks WHERE question_id = '{self.que[self.count]}'""")
                for i in answers:
                    tek_answers = i[0]
                    tek_answers = tek_answers.split('-')
                correct_answer = cur.execute(
                    f"""SELECT correct_answer from tasks WHERE question_id = '{self.que[self.count]}'""")
                for i in correct_answer:
                    self.tek_correct = i[0]
                self.ans0.show()
                self.ans0.setText(tek_answers[0])
                self.ans1.show()
                self.ans1.setText(tek_answers[1])
                self.ans2.show()
                self.ans2.setText(tek_answers[2])
                self.ans3.show()
                self.ans3.setText(tek_answers[3])
                self.next_que.show()
                self.next_que_2.show()
                self.question_text.show()
                self.question_text.setText(f'{tek_question}')
                self.next_que_3.hide()
            else:
                pass


        except Exception as e:
            try:
                if self.count == len(self.que):
                    con = sqlite3.connect('secret_files.db')
                    cur = con.cursor()
                    '''cur.execute(
                        f"""UPDATE users SET syn_mistakes = {int(self.syn)}, oop_mistakes = {int(self.oop)},
                         files_mistakes = {int(self.files)}, modules_mistakes = {int(self.files))},
                          func_mistakes = {int(self.func)}, lists_mistakes = {int(self.lists)}
                           WHERE username LIKE '{greet.aut_log}'""")'''
                    result = '''UPDATE users SET syn_mistakes = ?,oop_mistakes = ?,files_mistakes = ?,
                    modules_mistakes = ?,func_mistakes = ?, lists_mistakes = ? WHERE username LIKE ?'''
                    record_list = [(int(self.syn)), (int(self.oop)), (int(self.files)), (int(self.mod)),
                                   (int(self.func)),
                                   (int(self.lists)), str((greet.aut_log.text()))]
                    cur.execute(result, record_list)
                    con.commit()
                    con.close()
                    self.ans0.hide()
                    self.ans0.hide()
                    self.ans1.hide()
                    self.ans2.hide()
                    self.ans3.hide()
                    self.next_que.hide()
                    self.next_que_2.hide()
                    self.question_text.hide()
                    self.next_que_3.show()
                    self.que = []
                    self.count = 0
                    test.hide()
                    results.show()
                else:
                   # print(e)
                   er.show()
            except Exception as e1:
              #  print(e1)
              er.show()

    def skip(self):
        self.answ.append(f'№{self.count + 1} - неверно')
        try:
            con = sqlite3.connect('secret_files.db')
            cur = con.cursor()
            add_mist1 = cur.execute(
                f"""SELECT topic_id from tasks WHERE question_id = '{self.que[self.count]}'""")
            for i in add_mist1:
                add_mist = i[0]
            if add_mist == 1:
                self.syn += 3
            elif add_mist == 2:
                self.lists += 3
            elif add_mist == 3:
                self.mod += 3
            elif add_mist == 4:
                self.func += 3
            elif add_mist == 5:
                self.oop += 3
            elif add_mist == 6:
                self.files += 3
        except Exception as ee:
            #print(ee)
            er.show()
        try:
            self.count += 1
            con = sqlite3.connect('secret_files.db')
            cur = con.cursor()
            question = cur.execute(f"""SELECT question from tasks WHERE question_id = '{self.que[self.count]}'""")
            for i in question:
                tek_question = i[0]
            answers = cur.execute(f"""SELECT answers from tasks WHERE question_id = '{self.que[self.count]}'""")
            for i in answers:
                tek_answers = i[0]
                tek_answers = tek_answers.split('-')
            correct_answer = cur.execute(
                f"""SELECT correct_answer from tasks WHERE question_id = '{self.que[self.count]}'""")
            for i in correct_answer:
                self.tek_correct = i[0]
            self.ans0.show()
            self.ans0.setText(tek_answers[0])
            self.ans1.show()
            self.ans1.setText(tek_answers[1])
            self.ans2.show()
            self.ans2.setText(tek_answers[2])
            self.ans3.show()
            self.ans3.setText(tek_answers[3])
            self.next_que.show()
            self.next_que_2.show()
            self.question_text.show()
            self.question_text.setText(f'{tek_question}')
            self.next_que_3.hide()
        except Exception as e:
            try:
                if self.count == len(self.que):
                    con = sqlite3.connect('secret_files.db')
                    cur = con.cursor()
                    '''cur.execute(
                        f"""UPDATE users SET syn_mistakes = {int(self.syn)}, oop_mistakes = {int(self.oop)},
                         files_mistakes = {int(self.files)}, modules_mistakes = {int(self.files))},
                          func_mistakes = {int(self.func)}, lists_mistakes = {int(self.lists)}
                           WHERE username LIKE '{greet.aut_log}'""")'''
                    result = '''UPDATE users SET syn_mistakes = ?,oop_mistakes = ?,files_mistakes = ?,
                    modules_mistakes = ?,func_mistakes = ?, lists_mistakes = ? WHERE username LIKE ?'''
                    record_list = [(int(self.syn)), (int(self.oop)), (int(self.files)), (int(self.mod)),
                                   (int(self.func)),
                                   (int(self.lists)), str((greet.aut_log.text()))]
                    cur.execute(result, record_list)
                    con.commit()
                    con.close()
                    self.ans0.hide()
                    self.ans0.hide()
                    self.ans1.hide()
                    self.ans2.hide()
                    self.ans3.hide()
                    self.next_que.hide()
                    self.next_que_2.hide()
                    self.question_text.hide()
                    self.next_que_3.show()
                    self.que = []
                    self.count = 0
                    test.hide()
                    results.show()
                else:
                    #print(e, 1)
                    er.show()
            except Exception as e1:
                #print(e1, 2)
                er.show()


class FourthMainForm(QWidget, Ui_End):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ret.clicked.connect(self.on_main)
        self.show_results.clicked.connect(self.results)
        self.topic.setText(f'Результаты')
        self.res.hide()
        self.ret.hide()

    def results(self):
        try:
            self.topic.setText(f'Ваш результат: {test.aim}')
            self.show_results.hide()
            self.res.show()
            self.ret.show()
            for i in range(len(test.answ)):
                self.res.insertPlainText(test.answ[i])
                self.res.insertPlainText('\n')
            test.answ = []

        except Exception as e:
           # print(e)
           er.show()

    def on_main(self):
        self.res.hide()
        self.ret.hide()
        self.topic.setText(f'Результаты')
        self.res.setPlainText('')
        self.show_results.show()
        test.aim = 0
        results.close()
        work.show()



class Err(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_main)

    def on_main(self):
        work.close()
        test.close()
        results.close()
        greet.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    greet = FirstMainForm()
    work = SecondMainForm()
    test = ThirdMainForm()
    results = FourthMainForm()
    er = Err()
    greet.show()
    sys.exit(app.exec())
