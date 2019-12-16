from PySide2 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_password_button.setGeometry(QtCore.QRect(280, 50, 100, 100))
        self.get_password_button.setObjectName("get_password_button")
        self.information_label = QtWidgets.QLabel(self.centralwidget)
        self.information_label.setGeometry(QtCore.QRect(10, 10, 380, 30))
        self.information_label.setTextFormat(QtCore.Qt.RichText)
        self.information_label.setObjectName("information_label")
        self.assbreaker = QtWidgets.QRadioButton(self.centralwidget)
        self.assbreaker.setGeometry(QtCore.QRect(20, 50, 230, 25))
        self.assbreaker.setObjectName("checkbox_numbers")
        self.domainlike = QtWidgets.QRadioButton(self.centralwidget)
        self.domainlike.setGeometry(QtCore.QRect(20, 80, 230, 25))
        self.domainlike.setObjectName("checkbox_letter")
        self.clipboard = QtWidgets.QCheckBox(self.centralwidget)
        self.clipboard.setGeometry(QtCore.QRect(20, 150, 230, 20))
        self.clipboard.setObjectName("checkbox_symbols_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 175, 50, 20))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 175, 120, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Генератор паролей", None, -1))
        self.get_password_button.setText(QtWidgets.QApplication.translate("MainWindow", "Get Password", None, -1))
        self.information_label.setText(QtWidgets.QApplication.translate("MainWindow", "", None, -1))
        self.assbreaker.setText(QtWidgets.QApplication.translate("MainWindow", "Рандомный типа 8Yf87eRfO9Iu", None, -1))
        self.domainlike.setText(QtWidgets.QApplication.translate("MainWindow", "Минималочка для домена типа 123456zZ",
                                                                 None, -1))
        self.clipboard.setText(QtWidgets.QApplication.translate("MainWindow", "Скопировать в буфер обмена",
                                                                None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow",
                                                            "<html><head/><body><p>Длина пароля"
                                                            "</p></body></html>", None, -1))

