from PyQt5 import QtCore, QtWidgets
import sys
import fun_mainwindow
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
    sys.exit(app.exec_())




