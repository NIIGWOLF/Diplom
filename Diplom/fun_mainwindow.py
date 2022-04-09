import mainwindow
import fun_dialogeditnodeswindow
import nodes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import pickle

class Event_MainWindow(QtWidgets.QMainWindow):
    def InitUI(self):
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.listNode = []

        self.DialogWindow = fun_dialogeditnodeswindow.Event_DialogEditNodesWindow()
        self.DialogWindow.InitUI()

        self.ui.PDadd.clicked.connect(lambda: self.__AddNode(0,None))
        self.ui.PDnew.clicked.connect(self.__DelAllNode)
        self.ui.PDsave.clicked.connect(self.__SaveFile)
        self.ui.PDload.clicked.connect(self.__LoadFile)

        if os.path.exists("./profile/temp.pcl"):
            list = pickle.load(open("./profile/temp.pcl", 'rb'))
            self.__ParsNodesToForm(list)




    def closeEvent(self,event):
        if not os.path.exists("profile"): os.makedirs("profile")
        pickle.dump(self.listNode, open("./profile/temp.pcl", 'wb'))

    def __SaveFile(self):
        if not os.path.exists("profile"): os.makedirs("profile")
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "./profile", "All Files(*.pkl)")
        if ok:
            pickle.dump(self.listNode, open(filename, 'wb'))

    def __LoadFile(self):
        if not os.path.exists("profile"): os.makedirs("profile")
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "./profile", "All Files(*.pkl)")
        if ok:
            list = pickle.load(open(filename, 'rb'))
            self.__ParsNodesToForm(list)

    def __ParsNodesToForm(self,list):
        self.__DelAllNode()
        self.listNode=list

        for elem in list:
            self.__AddNode(1,elem)


    def __GetPosFrame(self,frame):
        for i in range(0,self.ui.PDverticalNode.count()):
            if self.ui.PDverticalNode.itemAt(i).widget()==frame:
                return i

    def __EditNode(self,frame,label):
        self.DialogWindow.ShowUI(self.listNode[self.__GetPosFrame(frame)])
        label.setText(self.listNode[self.__GetPosFrame(frame)].name)

    def __DelNode(self,frame):
        x= self.__GetPosFrame(frame)
        del self.listNode[x]
        frame.deleteLater()

    def __DelAllNode(self):
        for i in range(0,self.ui.PDverticalNode.count()-1):
            self.ui.PDverticalNode.itemAt(i).widget().deleteLater()
        self.listNode.clear()

    def __MoveUpNode(self,frame):
        x = self.__GetPosFrame(frame)
        if x>0:
            self.ui.PDverticalNode.insertWidget(x-1,frame)
            self.listNode[x], self.listNode[x-1] = self.listNode[x-1], self.listNode[x]

    def __MoveDownNode(self, frame):
        x = self.__GetPosFrame(frame)
        if x < self.ui.PDverticalNode.count()-2:
            self.ui.PDverticalNode.insertWidget(x + 1, frame)
            self.listNode[x], self.listNode[x + 1] = self.listNode[x + 1], self.listNode[x]


    def __AddNode(self,flag,node):
        font = QtGui.QFont()
        font.setPointSize(12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        frame_1 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        frame_1.setFrameShape(QtWidgets.QFrame.Box)
        frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_1.setLineWidth(2)
        frame_1.setObjectName("frame_1")

        gridLayout_2 = QtWidgets.QGridLayout(frame_1)
        gridLayout_2.setContentsMargins(0, 7, 0, 7)

        horizontalLayout_4 = QtWidgets.QHBoxLayout()
        gridLayout_2.addLayout(horizontalLayout_4, 0, 0, 1, 1)


        label_1 = QtWidgets.QLabel(frame_1)
        label_1.setFont(font)
        horizontalLayout_4.addWidget(label_1)

        pushButton_7 = QtWidgets.QPushButton(frame_1)
        sizePolicy.setHeightForWidth(pushButton_7.sizePolicy().hasHeightForWidth())
        pushButton_7.setSizePolicy(sizePolicy)
        pushButton_7.setMinimumSize(QtCore.QSize(35, 35))
        pushButton_7.setFont(font)
        horizontalLayout_4.addWidget(pushButton_7)

        pushButton_8 = QtWidgets.QPushButton(frame_1)
        sizePolicy.setHeightForWidth(pushButton_8.sizePolicy().hasHeightForWidth())
        pushButton_8.setSizePolicy(sizePolicy)
        pushButton_8.setMinimumSize(QtCore.QSize(35, 35))
        pushButton_8.setFont(font)
        horizontalLayout_4.addWidget(pushButton_8)

        pushButton_9 = QtWidgets.QPushButton(frame_1)
        sizePolicy.setHeightForWidth(pushButton_9.sizePolicy().hasHeightForWidth())
        pushButton_9.setSizePolicy(sizePolicy)
        pushButton_9.setMinimumSize(QtCore.QSize(35, 35))
        pushButton_9.setFont(font)
        horizontalLayout_4.addWidget(pushButton_9)

        pushButton_10 = QtWidgets.QPushButton(frame_1)
        sizePolicy.setHeightForWidth(pushButton_10.sizePolicy().hasHeightForWidth())
        pushButton_10.setSizePolicy(sizePolicy)
        pushButton_10.setMinimumSize(QtCore.QSize(35, 35))
        pushButton_10.setFont(font)
        horizontalLayout_4.addWidget(pushButton_10)

        #self.ui.PDverticalNode.addWidget()
        self.ui.PDverticalNode.insertWidget(self.ui.PDverticalNode.count()-1,frame_1)

        _translate = QtCore.QCoreApplication.translate

        if (not(flag)):
            label_1.setText(_translate("MainWindow", "Новый нод"))
        else:
            label_1.setText(_translate("MainWindow", node.name))
        pushButton_7.setText(_translate("MainWindow", "^"))
        pushButton_8.setText(_translate("MainWindow", "v"))
        pushButton_9.setText(_translate("MainWindow", "R"))
        pushButton_10.setText(_translate("MainWindow", "-"))

        if (not(flag)):
            self.listNode.append(nodes.Node("Новый нод", "", {}))

        pushButton_7.clicked.connect(lambda: self.__MoveUpNode(frame_1))
        pushButton_8.clicked.connect(lambda: self.__MoveDownNode(frame_1))
        pushButton_9.clicked.connect(lambda: self.__EditNode(frame_1,label_1))
        pushButton_10.clicked.connect(lambda: self.__DelNode(frame_1))


