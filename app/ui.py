# aeste el codigo de las interfaz
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from app.chatbot import get_agent_response

class KaliSupportApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kali Support Chatbot')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

    def send_message(self):
        user_input = self.input_field.text()
        if user_input:
            self.chat_area.append(f"User: {user_input}")
            response = get_agent_response(user_input)
            self.chat_area.append(f"Kali Support: {response}")
            self.input_field.clear()
