# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogeditnodeswindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEditNodesWindow(object):
    def setupUi(self, DialogEditNodesWindow):
        DialogEditNodesWindow.setObjectName("DialogEditNodesWindow")
        DialogEditNodesWindow.resize(800, 400)
        DialogEditNodesWindow.setMinimumSize(QtCore.QSize(800, 400))
        self.gridLayout = QtWidgets.QGridLayout(DialogEditNodesWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.ENmaingrid = QtWidgets.QGridLayout()
        self.ENmaingrid.setSpacing(7)
        self.ENmaingrid.setObjectName("ENmaingrid")
        self.ENverticalmain = QtWidgets.QVBoxLayout()
        self.ENverticalmain.setObjectName("ENverticalmain")
        self.ENTitle = QtWidgets.QFrame(DialogEditNodesWindow)
        self.ENTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ENTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ENTitle.setObjectName("ENTitle")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ENTitle)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ENverticalTitle = QtWidgets.QHBoxLayout()
        self.ENverticalTitle.setContentsMargins(-1, 10, -1, 10)
        self.ENverticalTitle.setObjectName("ENverticalTitle")
        self.ENltNameNode = QtWidgets.QLabel(self.ENTitle)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENltNameNode.setFont(font)
        self.ENltNameNode.setObjectName("ENltNameNode")
        self.ENverticalTitle.addWidget(self.ENltNameNode)
        self.ENeNameNode = QtWidgets.QLineEdit(self.ENTitle)
        self.ENeNameNode.setMinimumSize(QtCore.QSize(0, 35))
        self.ENeNameNode.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENeNameNode.setFont(font)
        self.ENeNameNode.setObjectName("ENeNameNode")
        self.ENverticalTitle.addWidget(self.ENeNameNode)
        self.ENSave = QtWidgets.QPushButton(self.ENTitle)
        self.ENSave.setMinimumSize(QtCore.QSize(0, 35))
        self.ENSave.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENSave.setFont(font)
        self.ENSave.setObjectName("ENSave")
        self.ENverticalTitle.addWidget(self.ENSave)
        self.ENLoad = QtWidgets.QPushButton(self.ENTitle)
        self.ENLoad.setMinimumSize(QtCore.QSize(0, 35))
        self.ENLoad.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENLoad.setFont(font)
        self.ENLoad.setObjectName("ENLoad")
        self.ENverticalTitle.addWidget(self.ENLoad)
        self.ENLoadCMD = QtWidgets.QPushButton(self.ENTitle)
        self.ENLoadCMD.setMinimumSize(QtCore.QSize(0, 35))
        self.ENLoadCMD.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENLoadCMD.setFont(font)
        self.ENLoadCMD.setObjectName("ENLoadCMD")
        self.ENverticalTitle.addWidget(self.ENLoadCMD)
        self.ENAddParam = QtWidgets.QPushButton(self.ENTitle)
        self.ENAddParam.setMinimumSize(QtCore.QSize(35, 35))
        self.ENAddParam.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENAddParam.setFont(font)
        self.ENAddParam.setObjectName("ENAddParam")
        self.ENverticalTitle.addWidget(self.ENAddParam)
        self.gridLayout_3.addLayout(self.ENverticalTitle, 1, 0, 1, 1)
        self.ENverticalPath = QtWidgets.QHBoxLayout()
        self.ENverticalPath.setObjectName("ENverticalPath")
        self.ENltPathRun = QtWidgets.QLabel(self.ENTitle)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENltPathRun.setFont(font)
        self.ENltPathRun.setObjectName("ENltPathRun")
        self.ENverticalPath.addWidget(self.ENltPathRun)
        self.ENePathRun = QtWidgets.QLineEdit(self.ENTitle)
        self.ENePathRun.setMinimumSize(QtCore.QSize(0, 35))
        self.ENePathRun.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENePathRun.setFont(font)
        self.ENePathRun.setObjectName("ENePathRun")
        self.ENverticalPath.addWidget(self.ENePathRun)
        self.gridLayout_3.addLayout(self.ENverticalPath, 2, 0, 1, 1)
        self.ENverticalmain.addWidget(self.ENTitle)
        self.ENscrollAreaParam = QtWidgets.QScrollArea(DialogEditNodesWindow)
        self.ENscrollAreaParam.setWidgetResizable(True)
        self.ENscrollAreaParam.setObjectName("ENscrollAreaParam")
        self.ENscrollAreaParamContents = QtWidgets.QWidget()
        self.ENscrollAreaParamContents.setGeometry(QtCore.QRect(0, 0, 772, 200))
        self.ENscrollAreaParamContents.setObjectName("ENscrollAreaParamContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ENscrollAreaParamContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.ENgridParam = QtWidgets.QGridLayout()
        self.ENgridParam.setObjectName("ENgridParam")
        self.ENltValueParam = QtWidgets.QLabel(self.ENscrollAreaParamContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENltValueParam.setFont(font)
        self.ENltValueParam.setObjectName("ENltValueParam")
        self.ENgridParam.addWidget(self.ENltValueParam, 0, 1, 1, 1)
        self.ENltBool = QtWidgets.QLabel(self.ENscrollAreaParamContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENltBool.setFont(font)
        self.ENltBool.setAlignment(QtCore.Qt.AlignCenter)
        self.ENltBool.setWordWrap(True)
        self.ENltBool.setObjectName("ENltBool")
        self.ENgridParam.addWidget(self.ENltBool, 0, 2, 1, 1)
        self.ENltNameParam = QtWidgets.QLabel(self.ENscrollAreaParamContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ENltNameParam.setFont(font)
        self.ENltNameParam.setObjectName("ENltNameParam")
        self.ENgridParam.addWidget(self.ENltNameParam, 0, 0, 1, 1)
        self.ENltDelButton = QtWidgets.QLabel(self.ENscrollAreaParamContents)
        self.ENltDelButton.setText("")
        self.ENltDelButton.setObjectName("ENltDelButton")
        self.ENgridParam.addWidget(self.ENltDelButton, 0, 3, 1, 1)
        self.ENgridParam.setColumnStretch(0, 1)
        self.ENgridParam.setColumnStretch(1, 2)
        self.gridLayout_4.addLayout(self.ENgridParam, 0, 0, 1, 1)
        self.ENscrollAreaParam.setWidget(self.ENscrollAreaParamContents)
        self.ENverticalmain.addWidget(self.ENscrollAreaParam)
        self.ENmaingrid.addLayout(self.ENverticalmain, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.ENmaingrid, 0, 0, 1, 1)
        self.ENhorizontalSaveChanged = QtWidgets.QHBoxLayout()
        self.ENhorizontalSaveChanged.setObjectName("ENhorizontalSaveChanged")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ENhorizontalSaveChanged.addItem(spacerItem1)
        self.ENSaveChanged = QtWidgets.QPushButton(DialogEditNodesWindow)
        self.ENSaveChanged.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENSaveChanged.setFont(font)
        self.ENSaveChanged.setObjectName("ENSaveChanged")
        self.ENhorizontalSaveChanged.addWidget(self.ENSaveChanged)
        self.gridLayout.addLayout(self.ENhorizontalSaveChanged, 1, 0, 1, 1)

        self.retranslateUi(DialogEditNodesWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogEditNodesWindow)

    def retranslateUi(self, DialogEditNodesWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogEditNodesWindow.setWindowTitle(_translate("DialogEditNodesWindow", "???????????????? ??????????"))
        self.ENltNameNode.setText(_translate("DialogEditNodesWindow", "???????????????? ????????"))
        self.ENSave.setText(_translate("DialogEditNodesWindow", "??????????????????"))
        self.ENLoad.setText(_translate("DialogEditNodesWindow", "??????????????????"))
        self.ENLoadCMD.setText(_translate("DialogEditNodesWindow", "?????????????????? cmd"))
        self.ENAddParam.setText(_translate("DialogEditNodesWindow", "+"))
        self.ENltPathRun.setText(_translate("DialogEditNodesWindow", "???????? ?? ???????????????????????? ??????????"))
        self.ENltValueParam.setText(_translate("DialogEditNodesWindow", "???????????????? ??????????????????"))
        self.ENltBool.setText(_translate("DialogEditNodesWindow", "?????????????? ????????????"))
        self.ENltNameParam.setText(_translate("DialogEditNodesWindow", "???????????????? ??????????????????"))
        self.ENSaveChanged.setText(_translate("DialogEditNodesWindow", "?????????????????? ??????????????????"))
