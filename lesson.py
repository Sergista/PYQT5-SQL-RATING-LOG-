import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QApplication, QMessageBox, QDesktopWidget,QInputDialog
from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Журнал")
        self.create_button()
        self.create_data_base()
        self.show()

    def create_button(self):
        self.add_student = QPushButton("Добавить ученика", self)
        self.add_student.move(5, 5)
        self.add_student.resize(150, 30)
        # self.add_student.clicked.connected
        self.add_mark = QPushButton("Добавить оценку", self)
        self.add_mark.move(5, 40)
        self.add_mark.resize(150, 30)
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

    def b_student(self):
        name = self.get_text()
        if name:
            self.query.prepare("INSERT INTO marks(name) VALUES (?)")
            self.query.addBindValue(name)
            self.query.exec()
    def get_text(self):
        name, ok = QInputDialog.getText(self,"Добавить ученика","Введите имя")
        if ok:
            return name





if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemple = Window()
    sys.exit(app.exec_())
