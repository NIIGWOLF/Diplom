# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogrunbuild.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogRunBuild(object):
    def setupUi(self, DialogRunBuild):
        DialogRunBuild.setObjectName("DialogRunBuild")
        DialogRunBuild.resize(481, 168)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogRunBuild)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lFolder = QtWidgets.QLabel(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lFolder.setFont(font)
        self.lFolder.setObjectName("lFolder")
        self.gridLayout.addWidget(self.lFolder, 0, 0, 1, 1)
        self.lNode = QtWidgets.QLabel(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lNode.setFont(font)
        self.lNode.setObjectName("lNode")
        self.gridLayout.addWidget(self.lNode, 1, 0, 1, 1)
        self.pbFolder = QtWidgets.QProgressBar(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbFolder.setFont(font)
        self.pbFolder.setProperty("value", 24)
        self.pbFolder.setObjectName("pbFolder")
        self.gridLayout.addWidget(self.pbFolder, 0, 1, 1, 1)
        self.pbNode = QtWidgets.QProgressBar(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbNode.setFont(font)
        self.pbNode.setProperty("value", 24)
        self.pbNode.setObjectName("pbNode")
        self.gridLayout.addWidget(self.pbNode, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.lState = QtWidgets.QLabel(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lState.setFont(font)
        self.lState.setObjectName("lState")
        self.gridLayout_2.addWidget(self.lState, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(DialogRunBuild)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(DialogRunBuild)
        QtCore.QMetaObject.connectSlotsByName(DialogRunBuild)

    def retranslateUi(self, DialogRunBuild):
        _translate = QtCore.QCoreApplication.translate
        DialogRunBuild.setWindowTitle(_translate("DialogRunBuild", "Построение mash-объекта"))
        self.lFolder.setText(_translate("DialogRunBuild", "Процес обработки папок:"))
        self.lNode.setText(_translate("DialogRunBuild", "Прогрес выполнения нодов:"))
        self.pbFolder.setFormat(_translate("DialogRunBuild", "%v/%m"))
        self.pbNode.setFormat(_translate("DialogRunBuild", "%v/%m"))
        self.lState.setText(_translate("DialogRunBuild", "Статус:"))
        self.pushButton.setText(_translate("DialogRunBuild", "Остановить"))