import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QApplication, QMessageBox, QDesktopWidget, QInputDialog
from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.create_data_base()
        self.resize(400, 400)
        self.setWindowTitle("Журнал")
        self.create_button()
        self.show()

    def create_button(self):
        self.add_student = QPushButton("Добавить ученика", self)
        self.add_student.move(5, 5)
        self.add_student.resize(150, 30)
        self.add_student.clicked.connect(self.b_student)
        self.add_mark = QPushButton("Добавить оценку", self)
        self.add_mark.move(5, 40)
        self.add_mark.resize(150, 30)
        self.add_mark.clicked.connect(self.set_mark)
        self.show_table = QPushButton("Показать оценки", self)
        self.show_table.move(5, 75)
        self.show_table.resize(150, 30)

    def create_data_base(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("studentperfomance.sqlite")
        if not self.db.open():
            print(self.db.lastError().text())
            sys.exit(1)
        self.query = QSqlQuery()
        self.query.exec("""
         CREATE TABLE marks(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
         name VARCHAR(40) NOT NULL,
         grades VARCHAR(40))""")

        """Добавляем учеников"""

    def b_student(self):
        name = self.get_text()
        if name:
            self.query.prepare("INSERT INTO marks(name) VALUES (?)")
            self.query.addBindValue(name)
            self.query.exec()

    def get_text(self):
        name, ok = QInputDialog.getText(self, "Добавить ученика", "Введите имя")
        if ok:
            return name

        """""Добавляем оценки"""

    def set_mark(self):
        names = self.get_names()
        name = self.get_choice(names)
        if name:
            mark = self.get_integer()
            new_grades = self.get_grades(mark, name)
            self.update_grade(name, new_grades)

    def update_grade(self, name, new_grade):
        self.query.prepare("""UPDATE marks SET grades = (?) WHERE name = (?)""")
        self.query.addBindValue(new_grade)
        self.query.addBindValue(name)
        self.query.exec()

    def get_grades(self, mark, name):
        self.query.prepare("""SELECT grades FROM marks WHERE name = (?)""")
        self.query.addBindValue(name)
        self.query.exec()
        self.query.first()
        grades = self.query.value(0)
        if grades == "":
            return mark
        else:
            return f"{grades},{mark}"

    def get_integer(self):
        mark, ok = QInputDialog.getInt(self, "выбрать оценку", "Оценка", 5, 1, 5, 1)
        if ok:
            return mark

    def get_choice(self, names):
        name, ok = QInputDialog.getItem(self, "выбрать ученика", "выберите имя", names)
        if ok:
            return name

    def get_names(self):
        self.query.exec("""SELECT name FROM marks""")
        name_list = []
        while self.query.next():
            name_list.append(self.query.value(0))
        return name_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemple = Window()
    sys.exit(app.exec_())
