import sys

from dotenv import load_dotenv

from PySide6.QtWidgets import QApplication, QMainWindow
from cadastroapostas.view.tela_apostas import Ui_MainWindow

load_dotenv()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
