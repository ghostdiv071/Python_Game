from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel
import codecs


class Rules(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 400)
        self.rules = QLabel(self)
        file = codecs.open("Rules.txt", "r", "utf-8")
        text = file.read()
        file.close()
        self.rules.setText(text)
        self.rules.setObjectName("rules")
        self.rules.move(10, 10)
        self.rules.setFont(QFont("Times", 15))
