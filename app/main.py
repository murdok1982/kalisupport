# este seria el punto de entrada 
import sys
from PyQt5.QtWidgets import QApplication
from app.ui import KaliSupportApp

def main():
    app = QApplication(sys.argv)
    ex = KaliSupportApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
