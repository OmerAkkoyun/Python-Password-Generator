
from PyQt5.QtWidgets import QMainWindow,QMessageBox#Uyarý vereceðimiz için gerekli modul messegebox
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import random,os
import string
import urllib.request

class Ui_Form(QWidget):
    def setupUi(self, Form):
        try:

            newpath = r'C:\Password_Generator'
            if not os.path.exists(newpath):  # bu kodlar  klasör oluþturma kodudur.
                os.makedirs(newpath)

            urllib.request.urlretrieve(
                "https://www.shareicon.net/download/2017/01/23/874882_password.ico",
                "C:\Password_Generator\key.ico")
        except:
            pass

        Form.setWindowIcon(QtGui.QIcon(os.path.expanduser("C:\Password_Generator\key.ico")))
        Form.setObjectName("Form")
        Form.resize(502, 339)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 198, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 101))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 58, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 78, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 198, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 101))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 58, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 78, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 101))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 58, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 78, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 58, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 58, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.olustur_buton = QtWidgets.QPushButton(Form)
        self.olustur_buton.setGeometry(QtCore.QRect(150, 170, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.olustur_buton.setFont(font)
        self.olustur_buton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.olustur_buton.setObjectName("olustur_buton")
        self.uzunluk_label = QtWidgets.QLabel(Form)
        self.uzunluk_label.setGeometry(QtCore.QRect(90, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.uzunluk_label.setFont(font)
        self.uzunluk_label.setObjectName("uzunluk_label")
        self.seviye_label = QtWidgets.QLabel(Form)
        self.seviye_label.setGeometry(QtCore.QRect(330, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.seviye_label.setFont(font)
        self.seviye_label.setObjectName("seviye_label")
        self.uzunluk_spinBox = QtWidgets.QSpinBox(Form)
        self.uzunluk_spinBox.setGeometry(QtCore.QRect(180, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.uzunluk_spinBox.setFont(font)
        self.uzunluk_spinBox.setMinimum(4)
        self.uzunluk_spinBox.setMaximum(40)
        self.uzunluk_spinBox.setObjectName("uzunluk_spinBox")
        self.seviye_spinBox = QtWidgets.QSpinBox(Form)
        self.seviye_spinBox.setGeometry(QtCore.QRect(270, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.seviye_spinBox.setFont(font)
        self.seviye_spinBox.setMinimum(1)
        self.seviye_spinBox.setMaximum(10)
        self.seviye_spinBox.setObjectName("seviye_spinBox")
        self.baslik_label = QtWidgets.QLabel(Form)
        self.baslik_label.setGeometry(QtCore.QRect(100, 10, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.baslik_label.setFont(font)
        self.baslik_label.setObjectName("baslik_label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 230, 461, 41))
        self.textEdit.setObjectName("textEdit")
        self.kaydet_buton = QtWidgets.QPushButton(Form)
        self.kaydet_buton.setGeometry(QtCore.QRect(210, 300, 81, 31))
        self.kaydet_buton.setObjectName("kaydet_buton")
        self.kaydet_buton.setEnabled(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Password Generator - Free"))
        self.olustur_buton.setText(_translate("Form", "Oluþtur"))
        self.uzunluk_label.setText(_translate("Form", "Uzunluk"))
        self.seviye_label.setText(_translate("Form", "Seviye"))
        self.baslik_label.setText(_translate("Form", "Þifre Oluþturucu"))
        self.kaydet_buton.setText(_translate("Form", "Kaydet"))

        #********************************** baðlantýlar ***********************************************
        self.olustur_buton.clicked.connect(self.olustur_F)
        self.kaydet_buton.clicked.connect(self.kaydet_F)


    def olustur_F(self):
        self.kaydet_buton.setEnabled(True)
        self.textEdit.setEnabled(True)
        seviye=str(self.seviye_spinBox.text())
        uzunluk=str(self.uzunluk_spinBox.text())

        def generate_password(length, level, output=[]):
            chars = string.ascii_letters
            if level <3:
                chars = "{}{}".format(chars, string.digits)
            if level > 3:
                chars = "{}{}".format(chars, string.punctuation)

            for i in range(length):
                output.append(random.choice(chars))

            return "".join(output)

        print(("-" * 30) + "\n Password Generator\n" + ("-" * 30))

        password_length = int(uzunluk)
        password_level = int(seviye)

        self.password = generate_password(password_length, password_level)
        self.textEdit.setText(self.password)


    def kaydet_F(self):
        QMessageBox.about(self, "Bilgi", "Masaüstüne Kaydedildi!")  # mesaj
        yeni = open(os.path.expanduser(os.path.expanduser("~/Desktop/Sifreniz.txt")), "a", encoding="utf-8")  # Yaz
        yeni.write(self.password)
        yeni.write("\n")
        yeni.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

