import dialogrunbuild
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread

class Event_DialogRunBuild(QtWidgets.QDialog):


    def InitUI(self):
        self.ui = dialogrunbuild.Ui_DialogRunBuild()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.__OnClickButton)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.state = 0 #0-run/1-process stop/2-stop/3-complite
        self.isEnd = False
        self.th = None


    def ShowUI(self, listFolder:list, listNode:list,th: Thread):
        if not listFolder or not listNode:
            return
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setText("Остановить")
        self.ui.lState.setText("Статус: выполняется")
        self.ui.pbFolder.setValue(self.ui.pbFolder.minimum())
        self.ui.pbFolder.setMaximum(len(listFolder))
        self.ui.pbNode.setValue(self.ui.pbNode.minimum())
        self.ui.pbNode.setMaximum(len(listNode))
        self.state=0
        self.isEnd=False
        self.th=th
        self.exec_()

    def closeEvent(self,event):
        print("closeDialog")

        if self.state!=3:
            reply = QtWidgets.QMessageBox.question(
                self,
                "Exit",
                "Построение mash-объектов не закончено. Вы уверены, что хотите закрыть окно? Это приведет к завершению обработки.",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if reply != QtWidgets.QMessageBox.Yes:
                event.ignore()
            if reply == QtWidgets.QMessageBox.Yes:
                self.isEnd=True
                while (not self.th):
                    pass
        event.accept()

    def ChangedStateStop(self):
        self.ui.lState.setText("Статус: приостановлено")
        self.state = 2
        self.ui.pushButton.setText("Продолжить")
        self.ui.pushButton.setEnabled(True)

    def ChangedStateComplite(self):
        self.ui.pbNode.setValue(self.ui.pbNode.minimum())
        self.ui.lState.setText("Статус: завершено")
        self.state = 3
        self.ui.pushButton.setText("ОК")
        self.ui.pushButton.setEnabled(True)


    def AddProgressBarFolder(self):
        self.ui.pbFolder.setValue(self.ui.pbFolder.value()+1)

    def AddProgressBarNode(self):
        self.ui.pbNode.setValue(self.ui.pbNode.value()+1)

    def ClearProgressBarNode(self):
        self.ui.pbNode.setValue(0)

    def __OnClickButton(self):
        if self.state==0: #run
            self.ui.lState.setText("Статус: в процессе остановки")
            self.state = 1
            self.ui.pushButton.setText("Продолжить")
            self.ui.pushButton.setEnabled(True)
            return
        if self.state==1 or self.state==2: #stop
            self.ui.lState.setText("Статус: выполняется")
            self.state = 0
            self.ui.pushButton.setText("Остановить")
            self.ui.pushButton.setEnabled(True)
            return
        if self.state==3:
            self.hide()
