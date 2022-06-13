import os,sys
from PyQt5 import QtWidgets
class ReplaceConstParam:
    pathMeshroom=""
    path3DObject=""
    @staticmethod
    def ReplaceMeshroom(folder):
        return ReplaceConstParam.ReplaceParam(ReplaceConstParam.pathMeshroom,folder)
    @staticmethod
    def Replace3DObject(folder):
        return ReplaceConstParam.ReplaceParam(ReplaceConstParam.path3DObject,folder)
    @staticmethod
    def ReplaceParam(text, imageFolder):
        if not os.path.exists(ReplaceConstParam.pathMeshroom):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            msgBox.setText("Путь к Meshroom.exe указан не верно")
            msgBox.setWindowTitle("Ошибка")
            msgBox.exec();
            return 1
        text = text.replace("{PreImageFolder}", os.path.dirname(imageFolder))
        text = text.replace("{AliceFolder}", "D:/Meshroom-2021.1.0/aliceVision")
        text = text.replace("{BaseFolder}", os.path.dirname(sys.argv[0]))
        text = text.replace("{ImageFolder}", imageFolder)
        text = text.replace("{NameImageFolder}", os.path.basename(imageFolder))
        return text