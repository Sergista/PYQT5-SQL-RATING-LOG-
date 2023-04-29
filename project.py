import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import Qt


class Clicker(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("Кликер")
        self.resize(300, 400)
        self.lcd = QLCDNumber((self))
        self.btn1 = QPushButton("Нажми меня", self)
        self.btn2 = QPushButton("Нажми меня", self)
        self.vbox = QVBoxLayout()
        self.set_structure()
        self.btn1.clicked.connect(self.press_button)
        self.btn2.clicked.connect(self.press_button)
        self.show()

    def set_structure(self):
        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.setLayout(self.vbox)

    def press_button(self):
        sender = self.sender()
        print(sender.text())
        if sender.text() == "Нажми меня":
            self.counter += 1
            self.btn2.setText("Сбросить")
        elif sender.text() == "Сбросить":
            self.counter = 0
            self.btn2.setText("Нажми меня")
        self.lcd.display(self.counter)

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_1:
            self.counter += 1
        elif event.key() == 45:
            self.counter = 0
        self.lcd.display(self.counter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clicker()
    sys.exit(app.exec_())
