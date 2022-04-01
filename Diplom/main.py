from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import shutil

from PyQt5.QtWidgets import QDialog

import nodes
import dialogeditnodeswindow
import mainwindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    file = QtCore.QFile("./stylesheet.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())


    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = mainwindow.Event_MainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setEnabled(0)
    MainWindow.show()

    DialogWindow = dialogeditnodeswindow.Event_DialogEditNodesWindow()
    dui = dialogeditnodeswindow.Ui_DialogEditNodesWindow()
    dui.setupUi(DialogWindow)
    DialogWindow.setFocus()
    DialogWindow.exec_()


    sys.exit(app.exec_())
