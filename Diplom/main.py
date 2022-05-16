from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import shutil

from PyQt5.QtWidgets import QDialog

import nodes
import fun_dialogeditnodeswindow
import fun_mainwindow
import mainwindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    file = QtCore.QFile("./stylesheet.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())

    MainWindow = fun_mainwindow.Event_MainWindow()
    MainWindow.InitUI()

    MainWindow.show()
    MainWindow.ClearAndAddFastOptionAllNode()



    #DialogWindow.setFocus()
    #DialogWindow.exec_()


    sys.exit(app.exec_())




