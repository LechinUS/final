from PyQt5 import QtCore, QtGui, QtWidgets

#автоматическая конвертация из .ui в .py
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(140, 50, 141, 31))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(290, 50, 101, 31))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 90, 381, 231))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#Добавление действия в список
    def add_it(self):
        item = self.additem_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.additem_lineEdit.setText("")

#удаление действия из списка
    def delete_it(self):
        clicked = self.mylist_listWidget.currentRow()
        self.mylist_listWidget.takeItem(clicked)
    
 #очистка списка
    def clear_it(self):
        self.mylist_listWidget.clear()

#отоброжение окна  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список дел"))
        self.additem_pushButton.setText(_translate("MainWindow", "Добавить действие"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Удалить действие"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Очистить список"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())