from functools import singledispatch

import dialogeditnodeswindow
from PyQt5 import QtCore, QtGui, QtWidgets
import nodes
import sys, os
import pickle


class Event_DialogEditNodesWindow(QtWidgets.QDialog):


    def InitUI(self):
        self.ui = dialogeditnodeswindow.Ui_DialogEditNodesWindow()
        self.ui.setupUi(self)
        self.i = 3
        self.ui.ENAddParam.clicked.connect(self.__AddEmptyParam)
        self.ui.ENSave.clicked.connect(self.__SaveFile)
        self.ui.ENLoad.clicked.connect(self.__LoadFile)
        self.ui.ENLoadCMD.clicked.connect(self.__LoadCMD)
        self.ui.ENSaveChanged.clicked.connect(self.__SaveChanged)
        self.ui.ENeNameNode.textChanged.connect(self.__ChangedEvent)
        self.ui.ENePathRun.textChanged.connect(self.__ChangedEvent)
        self.list = []
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

    def ShowUI(self, node: nodes.Node):
        self.node = node
        self.ui.ENeNameNode.setText(node.name)
        self.ui.ENePathRun.setText(node.run)
        self.__ParsNodeToForm(node)
        self.ui.ENSaveChanged.setEnabled(0)
        self.exec_()
        print()

    def __SaveFile(self):
        if not os.path.exists("nodes"): os.makedirs("nodes")
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,"Сохранить файл","./nodes","All Files(*.pkl)")
        if ok:
            oFile=open(filename, 'wb')
            pickle.dump(self.__ParsFormToNode(), oFile)
            oFile.close()

    def __LoadFile(self):
        if not os.path.exists("nodes"): os.makedirs("nodes")
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "./nodes", "All Files(*.pkl)")
        if ok:
            iFile=open(filename, 'rb')
            node = pickle.load(iFile)
            iFile.close()
            self.__ParsNodeToForm(node)

    def __LoadCMD(self):
        dialogLoadCMD = QtWidgets.QInputDialog()
        #dialogLoadCMD.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        text, ok = dialogLoadCMD.getText(self, 'Добавление через команду cmd', 'Введите команду для запуска из командной строки')
        if ok:
            self.__ParsNodeToForm(nodes.pars(text))


    def closeEvent(self,event):
        print("closeDialog")
        print(self.list)

        if self.ui.ENSaveChanged.isEnabled():
            reply = QtWidgets.QMessageBox.question(
                self,
                "Закрыть не сохраняя?",
                "Изменения не сохранены. Вы уверены, что хотите закрыть окно редактирования без сохранения?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if reply != QtWidgets.QMessageBox.Yes:
                event.ignore()
                return

        self.__DelAllParam()
        event.accept()

    def __DelAllParam(self):
        print("DellAllParam")
        for elem in self.list:
            elem[0].deleteLater()
            elem[1].deleteLater()
            elem[2].deleteLater()
            elem[3].deleteLater()
        self.list.clear()

    def __DelParam(self, edit1, edit2, check, btn):
        print("del")
        edit1.deleteLater()
        edit2.deleteLater()
        check.deleteLater()
        btn.deleteLater()
        self.list.remove([edit1,edit2,check,btn])

    def __ClearEmptyParam(self):
        for x in reversed(range(0, len(self.list))):
            if (self.list[x][0].text().strip()==""):
                self.list[x][0].deleteLater()
                self.list[x][1].deleteLater()
                self.list[x][2].deleteLater()
                self.list[x][3].deleteLater()
                self.list.remove(self.list[x])




    def __ParsNodeToForm(self,node):
        self.__DelAllParam()
        self.ui.ENeNameNode.setText(node.name)
        self.ui.ENePathRun.setText(node.run)
        for key in node.dict:
            self.__AddParam(key,node.dict.get(key)[0],node.dict.get(key)[1])

    def __ParsFormToNode(self):
        dict = {}
        for elem in self.list:
            print(elem[0].text)
            dict[elem[0].text()] = [elem[1].text(), elem[2].isChecked()]
        node = nodes.Node(self.ui.ENeNameNode.text(), self.ui.ENePathRun.text(), dict)
        return node


    def __AddEmptyParam(self):
        self.__AddParam("","",0)

    def __ChangedEvent(self):
        self.ui.ENSaveChanged.setEnabled(1)

    def __SaveChanged(self):
        self.ui.ENSaveChanged.clearFocus()
        self.ui.ENSaveChanged.setEnabled(0)
        self.__ClearEmptyParam()
        self.node.replace(self.__ParsFormToNode())


    def __AddParam(self,editText1, editText2, boolCheck: bool):
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setPointSize(12)

        lineEdit_1 = QtWidgets.QLineEdit(self.ui.ENscrollAreaParamContents)
        lineEdit_1.setMinimumSize(QtCore.QSize(0, 35))
        lineEdit_1.setMaximumSize(QtCore.QSize(16777215, 35))
        lineEdit_1.setFont(font)
        self.ui.ENgridParam.addWidget(lineEdit_1, self.i, 0, 1, 1)

        lineEdit_2 = QtWidgets.QLineEdit(self.ui.ENscrollAreaParamContents)
        lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        lineEdit_2.setFont(font)
        self.ui.ENgridParam.addWidget(lineEdit_2, self.i, 1, 1, 1)

        horizontalLayout = QtWidgets.QHBoxLayout()
        checkBox = QtWidgets.QCheckBox(self.ui.ENscrollAreaParamContents)
        checkBox.setMaximumSize(QtCore.QSize(60, 16777203))
        checkBox.setText("")
        horizontalLayout.addWidget(checkBox)
        self.ui.ENgridParam.addLayout(horizontalLayout, self.i, 2, 1, 1)

        pushButton = QtWidgets.QPushButton(self.ui.ENscrollAreaParamContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
        pushButton.setSizePolicy(sizePolicy)
        pushButton.setMinimumSize(QtCore.QSize(35, 35))
        pushButton.setMaximumSize(QtCore.QSize(35, 35))
        pushButton.setText(_translate("EditNodeWindow", "-"))
        self.ui.ENgridParam.addWidget(pushButton, self.i, 3, 1, 1)

        pushButton.clicked.connect(lambda: self.__DelParam(lineEdit_1,lineEdit_2, checkBox, pushButton))
        lineEdit_1.textChanged.connect(self.__ChangedEvent)
        lineEdit_2.textChanged.connect(self.__ChangedEvent)
        checkBox.stateChanged.connect(self.__ChangedEvent)

        self.list.append([lineEdit_1,lineEdit_2,checkBox,pushButton])

        lineEdit_1.setText(editText1)
        lineEdit_2.setText(editText2)
        checkBox.setChecked(boolCheck)

        self.i+=1




