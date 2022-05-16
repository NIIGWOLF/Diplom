

import mainwindow
import fun_dialogeditnodeswindow
import fun_dialogrunbuild
import nodes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import pickle
import subprocess
import datetime
from threading import Thread

class Event_MainWindow(QtWidgets.QMainWindow):
    def InitUI(self):
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.listNode = []
        self.listFastOption = []
        self.listFolder = []
        self.isChangedFastOption = False;

        self.DialogWindow = fun_dialogeditnodeswindow.Event_DialogEditNodesWindow()
        self.DialogWindow.InitUI()

        self.DialogRunBuild = fun_dialogrunbuild.Event_DialogRunBuild()
        self.DialogRunBuild.InitUI()

        self.ui.PDadd.clicked.connect(lambda: self.__AddNode(0,None))
        self.ui.PDnew.clicked.connect(self.__DelAllNode)
        self.ui.PDsave.clicked.connect(self.__SaveFile)
        self.ui.PDload.clicked.connect(self.__LoadFile)
        self.ui.PLallRun.clicked.connect(lambda: self.__RunThreadAllFolderBuild(datetime.datetime.now()))
        self.ui.tabWidget.currentChanged.connect(self.onChangeTabWidget)

        self.setAcceptDrops(True)

        self.ui.PIleftScrollArea.setAcceptDrops(True)

        if not os.path.exists("logs"): os.makedirs("logs")

        if os.path.exists("./profile/temp.pcl"):
            ifile = open("./profile/temp.pcl", 'rb')
            list = pickle.load(ifile)
            ifile.close()
            self.__ParsNodesToForm(list)

    def isMeshroomExsist(self):
        if not os.path.exists(self.ui.eMeshroom):
            QtWidgets.QMessageBox.information("Title", "Content")

    def onChangeTabWidget(self, i):
        if (i==0):
            if (self.isChangedFastOption):
                print("Changed Option")
                self.ClearAndAddFastOptionAllNode()
                self.isChangedFastOption=False

    def closeEvent(self,event):
        if not os.path.exists("profile"): os.makedirs("profile")
        oFile=open("./profile/temp.pcl", 'wb')
        pickle.dump(self.listNode, oFile)
        oFile.close()

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        for path in e.mimeData().urls():
            p:QtCore.QUrl=path
            if os.path.isdir(p.path().strip('/')):
                listFolderImage = []
                self.__SearchFolderImages(p.path().strip('/'),0,2,listFolderImage)
                for fl in listFolderImage:
                    self.__AddImageFolder(fl.replace('/','\\'))

    def __UpdateProgressBarFolder(self):
        n = len(self.listNode)
        for fl in self.listFolder:
            fl[1].setValue(0)
            fl[1].setMaximum(n)

    def __SearchFolderImages(self,folder,i,maxi,listFolderImage):
        folderCount=0
        pngCount = 0
        jpgCount = 0
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, file)):
                if i == maxi:
                    return
                self.__SearchFolderImages(os.path.join(folder, file),i+1,maxi,listFolderImage)
            folderCount+=1
            if file.endswith((".png",".PNG")):
                pngCount+=1
            if file.endswith((".jpg",".JPG")):
                jpgCount+=1
        if folderCount>0 and (pngCount==folderCount or jpgCount==folderCount):
            listFolderImage.append(folder)

    def __RunOneFolderBuild(self,fl,dt):
        if not os.path.exists("logs\\"+os.path.basename(fl[0])): os.makedirs("logs\\"+os.path.basename(fl[0]))
        fl[1].setValue(0)
        for node in self.listNode:
            if (self.DialogRunBuild.state==1): #process stop
                self.DialogRunBuild.ChangedStateStop()
            while(self.DialogRunBuild.state==2): #stop
                if (self.DialogRunBuild.isEnd):
                    return
            codeRun=node.runBuild(fl[0],self.DialogRunBuild,dt)
            if (codeRun!=0):
                print(codeRun,': Для нода "',node.name,'" указан не корректный путь!')
                self.DialogRunBuild.ChangedStateComplite()
                return
            if (self.DialogRunBuild.isEnd):
                return
            self.DialogRunBuild.AddProgressBarNode()
            fl[1].setValue(fl[1].value()+1)
        self.DialogRunBuild.AddProgressBarFolder()
        self.DialogRunBuild.ChangedStateComplite()

    def __RunThreadOneFolderBuild(self,fl,dt):
        th = Thread(target=self.__RunOneFolderBuild, args=(fl, dt,))
        th.start()
        self.DialogRunBuild.ShowUI([fl],self.listNode,th)


    def __RunAllFolderBuild(self,dt):
        for fl in self.listFolder:
            if not os.path.exists("logs\\" + os.path.basename(fl[0])): os.makedirs("logs\\" + os.path.basename(fl[0]))
            fl[1].setValue(0)
            for node in self.listNode:
                if (self.DialogRunBuild.state == 1):  # process stop
                    self.DialogRunBuild.ChangedStateStop()
                while (self.DialogRunBuild.state == 2):  # stop
                    if (self.DialogRunBuild.isEnd):
                        return
                codeRun = node.runBuild(fl[0], self.DialogRunBuild, dt)
                if (codeRun != 0):
                    print(codeRun, ': Для нода "', node.name, '" указан не корректный путь!')
                    self.DialogRunBuild.ChangedStateComplite()
                    return
                if (self.DialogRunBuild.isEnd):
                    return
                self.DialogRunBuild.AddProgressBarNode()
                fl[1].setValue(fl[1].value() + 1)
            self.DialogRunBuild.AddProgressBarFolder()
            self.DialogRunBuild.ClearProgressBarNode()
        self.DialogRunBuild.ChangedStateComplite()

    def __RunThreadAllFolderBuild(self, dt):
        th = Thread(target=self.__RunAllFolderBuild, args=(dt,))
        th.start()
        self.DialogRunBuild.ShowUI(self.listFolder, self.listNode, th)

    def __RunBuild(self,folder,dt):
        if not os.path.exists("logs\\" + os.path.basename(folder)): os.makedirs("logs\\" + os.path.basename(folder))
        for node in self.listNode:
            codeRun = node.runBuild(folder, dt)
            if (codeRun != 0):
                print(codeRun, ': Для нода "', node.name, '" указан не корректный путь!')
                return

    # region PD
    def __SaveFile(self):
        if not os.path.exists("profile"): os.makedirs("profile")
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "./profile", "All Files(*.pkl)")
        if ok:
            oFile=open(filename, 'wb')
            pickle.dump(self.listNode, oFile)
            oFile.close()

    def __LoadFile(self):
        if not os.path.exists("profile"): os.makedirs("profile")
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "./profile", "All Files(*.pkl)")
        if ok:
            iFile=open(filename, 'rb')
            list = pickle.load(iFile)
            iFile.close()
            self.__ParsNodesToForm(list)
            self.__UpdateProgressBarFolder()

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
        self.ClearAndAddFastOptionAllNode()
        label.setText(self.listNode[self.__GetPosFrame(frame)].name)

    def __DelNode(self,frame):
        self.isChangedFastOption=True
        x= self.__GetPosFrame(frame)
        del self.listNode[x]
        frame.deleteLater()
        self.__UpdateProgressBarFolder()

    def __DelAllNode(self):
        self.isChangedFastOption = True
        for i in range(0,self.ui.PDverticalNode.count()-1):
            self.ui.PDverticalNode.itemAt(i).widget().deleteLater()
        self.listNode.clear()
        self.__UpdateProgressBarFolder()

    def __MoveUpNode(self,frame):
        self.isChangedFastOption = True
        x = self.__GetPosFrame(frame)
        if x>0:
            self.ui.PDverticalNode.insertWidget(x-1,frame)
            self.listNode[x], self.listNode[x-1] = self.listNode[x-1], self.listNode[x]

    def __MoveDownNode(self, frame):
        self.isChangedFastOption = True
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

        self.__UpdateProgressBarFolder()


    # endregion

    # region PIRight

    def ClearAndAddFastOptionAllNode(self):
        for gb in self.listFastOption:
            gb.deleteLater()
        self.listFastOption.clear()
        for node in self.listNode:
            self.__AddFastOption(node)

    def __AddFastOption(self,node):
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setPointSize(10)
        flag = 0
        i = 0

        TempRightgroupBox = QtWidgets.QGroupBox(self.ui.PIrightscrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempRightgroupBox.sizePolicy().hasHeightForWidth())
        TempRightgroupBox.setSizePolicy(sizePolicy)

        TempRightgroupBox.setFont(font)
        gridLayout_7 = QtWidgets.QGridLayout(TempRightgroupBox)
        gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        gridLayout_7.setContentsMargins(5, 0, 5, 5)
        TempRightgridLayout = QtWidgets.QGridLayout()

        TempRightgroupBox.setTitle(_translate("MainWindow", node.name))

        for key in node.dict:
            if node.dict.get(key)[1]:
                self.__GenerateElemGroupBox(TempRightgroupBox,key,node.dict.get(key)[0],
                                            gridLayout_7,TempRightgridLayout,i,node,key)
                i=i+1
                flag = 1

        if flag:
            self.listFastOption.append(TempRightgroupBox)
            self.ui.PIrightverticalLayout.insertWidget(self.ui.PIrightverticalLayout.count() - 1, TempRightgroupBox)
        else:
            TempRightgroupBox.deleteLater()

    def __GenerateElemGroupBox(self, groupBox, name, value, grid, layout, pos,node,key):
        font = QtGui.QFont()
        font.setPointSize(8)

        TempRightlabel = QtWidgets.QLabel(groupBox)
        TempRightlabel.setFont(font)
        layout.addWidget(TempRightlabel, pos, 0, 1, 1)
        TempRightlabel.setText(name)

        TempRightlineEdit = QtWidgets.QLineEdit(groupBox)
        TempRightlineEdit.setText(value)
        layout.addWidget(TempRightlineEdit, pos, 1, 1, 1)

        grid.addLayout(layout, pos, 0, 1, 1)

        TempRightlineEdit.textChanged.connect(lambda: self.__EventChangedValueFastOption(node, key, TempRightlineEdit.text()))

    def __EventChangedValueFastOption(self,node,key,text):
        node.dict.get(key)[0]=text



    # endregion

    # region PILeft
    def __DelImageFolder(self,folder,groupBox):
        groupBox.deleteLater()
        for fl in self.listFolder:
            if fl[0]==folder:
                self.listFolder.remove(fl)
                return

    def __AddImageFolder(self,folder):
        font = QtGui.QFont()
        font.setPointSize(12)
        print(folder)

        for fl in self.listFolder:
            if fl[0]==folder:
                return

        TempLeftgroupBox = QtWidgets.QGroupBox(self.ui.PIleftscrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftgroupBox.sizePolicy().hasHeightForWidth())
        TempLeftgroupBox.setSizePolicy(sizePolicy)


        TempLeftgroupBox.setFont(font)
        gridLayout_10 = QtWidgets.QGridLayout(TempLeftgroupBox)
        gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        gridLayout_10.setContentsMargins(5, 0, 5, 0)
        TempLeftprogressBar = QtWidgets.QProgressBar(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftprogressBar.sizePolicy().hasHeightForWidth())
        TempLeftprogressBar.setSizePolicy(sizePolicy)


        TempLeftprogressBar.setFont(font)
        TempLeftprogressBar.setMaximum(len(self.listNode))
        TempLeftprogressBar.setProperty("value", 0)
        TempLeftprogressBar.setTextVisible(True)
        TempLeftprogressBar.setOrientation(QtCore.Qt.Horizontal)
        TempLeftprogressBar.setInvertedAppearance(False)
        TempLeftprogressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        gridLayout_10.addWidget(TempLeftprogressBar, 1, 0, 1, 1)
        TempLefthorizontalLayout = QtWidgets.QHBoxLayout()
        TempLefthorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        TempLeftlabel = QtWidgets.QLabel(TempLeftgroupBox)
        TempLeftlabel.setMinimumSize(QtCore.QSize(0, 35))


        TempLeftlabel.setFont(font)
        TempLefthorizontalLayout.addWidget(TempLeftlabel)
        TempLeftpushButton_Warning = QtWidgets.QPushButton(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftpushButton_Warning.sizePolicy().hasHeightForWidth())
        TempLeftpushButton_Warning.setSizePolicy(sizePolicy)
        TempLeftpushButton_Warning.setMinimumSize(QtCore.QSize(35, 35))


        TempLeftpushButton_Warning.setFont(font)
        TempLeftpushButton_Warning.setIconSize(QtCore.QSize(5, 5))
        TempLefthorizontalLayout.addWidget(TempLeftpushButton_Warning)
        TempLeftpushButton_Run = QtWidgets.QPushButton(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftpushButton_Run.sizePolicy().hasHeightForWidth())
        TempLeftpushButton_Run.setSizePolicy(sizePolicy)
        TempLeftpushButton_Run.setMinimumSize(QtCore.QSize(35, 35))


        TempLeftpushButton_Run.setFont(font)
        TempLeftpushButton_Run.setIconSize(QtCore.QSize(5, 5))
        TempLefthorizontalLayout.addWidget(TempLeftpushButton_Run)
        TempLeftpushButton_3D = QtWidgets.QPushButton(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftpushButton_3D.sizePolicy().hasHeightForWidth())
        TempLeftpushButton_3D.setSizePolicy(sizePolicy)
        TempLeftpushButton_3D.setMinimumSize(QtCore.QSize(35, 35))


        TempLeftpushButton_3D.setFont(font)
        TempLeftpushButton_3D.setIconSize(QtCore.QSize(5, 5))
        TempLefthorizontalLayout.addWidget(TempLeftpushButton_3D)
        TempLeftpushButton_Dir = QtWidgets.QPushButton(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftpushButton_Dir.sizePolicy().hasHeightForWidth())
        TempLeftpushButton_Dir.setSizePolicy(sizePolicy)
        TempLeftpushButton_Dir.setMinimumSize(QtCore.QSize(35, 35))


        TempLeftpushButton_Dir.setFont(font)
        TempLeftpushButton_Dir.setIconSize(QtCore.QSize(5, 5))
        TempLefthorizontalLayout.addWidget(TempLeftpushButton_Dir)
        TempLeftpushButton_Del = QtWidgets.QPushButton(TempLeftgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TempLeftpushButton_Del.sizePolicy().hasHeightForWidth())
        TempLeftpushButton_Del.setSizePolicy(sizePolicy)
        TempLeftpushButton_Del.setMinimumSize(QtCore.QSize(35, 35))


        TempLeftpushButton_Del.setFont(font)
        TempLeftpushButton_Del.setIconSize(QtCore.QSize(5, 5))
        TempLefthorizontalLayout.addWidget(TempLeftpushButton_Del)
        TempLefthorizontalLayout.setStretch(0, 1)
        gridLayout_10.addLayout(TempLefthorizontalLayout, 0, 0, 1, 1)
        self.ui.PIleftverticalLayout.insertWidget(self.ui.PIleftverticalLayout.count() - 1, TempLeftgroupBox)

        TempLeftpushButton_Warning.setVisible(False)
        TempLeftpushButton_Dir.clicked.connect(lambda: subprocess.Popen(f'explorer "{folder}"'))
        TempLeftpushButton_Del.clicked.connect(lambda: self.__DelImageFolder(folder,TempLeftgroupBox))
        TempLeftpushButton_Run.clicked.connect(lambda: self.__RunThreadOneFolderBuild([folder,TempLeftprogressBar],datetime.datetime.now()))
        self.listFolder.append([folder,TempLeftprogressBar])


        _translate = QtCore.QCoreApplication.translate
        TempLeftgroupBox.setTitle(os.path.basename(folder))
        TempLeftprogressBar.setFormat(_translate("MainWindow", "%v/%m"))
        TempLeftlabel.setText(_translate("MainWindow", "Статус:"))
        TempLeftpushButton_Warning.setText(_translate("MainWindow", "!?"))
        TempLeftpushButton_Run.setText(_translate("MainWindow", ">"))
        TempLeftpushButton_3D.setText(_translate("MainWindow", "3D"))
        TempLeftpushButton_Dir.setText(_translate("MainWindow", "..."))
        TempLeftpushButton_Del.setText(_translate("MainWindow", "-"))
    # endregion