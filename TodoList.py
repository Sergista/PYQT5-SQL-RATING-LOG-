import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtWidgets import QLabel, QPushButton, QListWidget, QLineEdit, QTextEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class ToDoList(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список задач")
        self.resize(500, 600)

        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()

        self.task_list_label = QLabel("Список задач:", self)
        self.task_name_label = QLabel('Название задачи:', self)
        self.task_description_label = QLabel('Описание задачи:', self)
        self.tasks_label = QLabel('Категория:', self)
        self.description_list_label = QLabel('Список категорий:', self)

        self.tasks_list = QListWidget()
        self.categories_list = QListWidget()

        self.button_all_tasks = QPushButton("Все задачи", self)
        self.button_active_tasks = QPushButton('Активные задачи', self)
        self.button_completed_tasks = QPushButton('Выполненные задачи', self)
        self.button_add_task = QPushButton('Добавить задачу', self)
        self.button_edit_task = QPushButton('Изменить задачу', self)
        self.button_delete_task = QPushButton('Удалить задачу', self)
        self.button_add_category = QPushButton('Добавить категорию', self)
        self.button_edit_category = QPushButton('Изменить категорию', self)
        self.button_delete_category = QPushButton('Удалить категорию', self)

        self.task_name_line = QLineEdit()
        self.categories_name_line = QLineEdit()

        self.task_description_text = QTextEdit()

        self.initUI()

    def initUI(self):
        self.create_db()
        self.set_structure()
        self.clicked_widget()
        self.show()

    def set_structure(self):
        self.vbox.addWidget(self.task_list_label)
        self.vbox.addWidget(self.tasks_list)

        self.hbox1.addWidget(self.button_all_tasks)
        self.hbox1.addWidget(self.button_active_tasks)
        self.hbox1.addWidget(self.button_completed_tasks)
        self.vbox.addLayout(self.hbox1)

        self.hbox2.addWidget(self.task_name_label)
        self.hbox2.addWidget(self.task_name_line)

        self.vbox.addLayout(self.hbox2)
        self.hbox3.addWidget(self.task_description_label)
        self.hbox3.addWidget(self.task_description_text)

        self.vbox.addLayout(self.hbox3)

        self.hbox4.addWidget(self.tasks_label)
        self.hbox4.addWidget(self.categories_name_line)
        self.vbox.addLayout(self.hbox4)

        self.vbox.addWidget(self.description_list_label)
        self.vbox.addWidget(self.categories_list)

        self.hbox5.addWidget(self.button_add_task)
        self.hbox5.addWidget(self.button_edit_task)
        self.hbox5.addWidget(self.button_delete_task)
        self.vbox.addLayout(self.hbox5)

        self.hbox6.addWidget(self.button_add_category)
        self.hbox6.addWidget(self.button_edit_category)
        self.hbox6.addWidget(self.button_delete_category)
        self.vbox.addLayout(self.hbox6)
        self.setLayout(self.vbox)

    def create_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('ToDoList.sqlite')

        if not self.db.open():
            exit(f"Не удалось открыть базу данных: {self.db.lastError().text()}")
        self.query = QSqlQuery()
        self.query.exec("""
        CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(60) NOT NULL)
        """)
        self.query.exec("""
                CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(120) NOT NULL, 
                description VARCHAR(255) NOT NULL, 
                active BOOL NOT NULL DEFAULT TRUE,
                category_id INTEGER, 
                FOREIGN KEY (category_id) REFERENCES categories (id))
                """)

    def clicked_widget(self):
        pass
        # self.tasks_list.itemClicked.connect(self.task_dtl)
        # self.categories_list.itemClicked.connect(self.categories_dtl)
        # self.button_all_tasks.clicked.connect()
        # self.button_active_tasks.clicked.connect()
        # self.button_completed_tasks.clicked.connect()
        #
        # self.button_add_task.clicked.connect(self.add_task)
        # self.button_edit_task.clicked.connect(self.edit_task)
        # self.button_delete_task.clicked.connect(self.delete_task)
        # self.button_add_category.clicked.connect(self.add_category)
        # self.button_edit_category.clicked.connect(self.edit_category)
        # self.button_delete_category.clicked.connect(self.delete_category)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todolist = ToDoList()
    sys.exit(app.exec_())
