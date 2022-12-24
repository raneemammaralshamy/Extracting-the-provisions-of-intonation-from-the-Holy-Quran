import final as E
import pyquran as q
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 821)
        self.le = QtWidgets.QLineEdit()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1131, 791))
        self.label.setStyleSheet("background-image: url(image.jpg) norepeat;\n")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 190, 241, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 290, 241, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(170, 470, 821, 299))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setStyleSheet("background-color:grey;")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 55, 16))
        self.label_2.setTabletTracking(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 300, 55, 16))
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setTabletTracking(False)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "run"))
        self.label_2.setText(_translate("MainWindow", "السورة"))
        self.label_3.setText(_translate("MainWindow", "الآية"))

        self.pushButton.clicked.connect(self.btn_clk)

    def btn_clk(self):
        E.result.clear()
        E.t = q.quran.get_verse(int(self.textEdit.toPlainText()), int(self.textEdit.toPlainText()), True)
        print(E.t)

        engine = E.Quran()
        engine.reset()
        engine.run()
        mystr = ""
        for res in E.result:
            mystr += res
            mystr += '\n'

            self.textEdit_3.setPlainText(res);




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
