from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
from sys import exit, argv
import pyperclip
from PySide2 import QtWidgets, QtCore
from main_window import Ui_MainWindow

app = QtWidgets.QApplication(argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


class Generator:
    def __init__(self):
        self.blank = ""

    def random_pass(self):
        letter = ascii_lowercase + ascii_uppercase + digits
        self.blank = "".join(choice(letter) for _ in range(int(ui.spinBox.text())))

    def domainlike(self):
        q = "".join(choice(digits) for _ in range(6))
        w = "".join(choice(ascii_lowercase))
        e = "".join(choice(ascii_uppercase))
        self.blank = f"{q}{w}{e}"

    def getpassword(self):
        if ui.assbreaker.isChecked():
            self.random_pass()
        if ui.domainlike.isChecked():
            self.domainlike()
        if ui.clipboard.isChecked():
            pyperclip.copy(self.blank)

        ui.information_label.setText("Пароль: " + self.blank)
        ui.information_label.setStyleSheet("""font-size: 20px;""")
        ui.information_label.setAlignment(QtCore.Qt.AlignCenter)


pwd = Generator()
ui.get_password_button.clicked.connect(pwd.getpassword)
exit(app.exec_())
