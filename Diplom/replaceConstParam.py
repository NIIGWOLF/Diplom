import os,sys

from PyQt5 import QtWidgets


class ReplaceConstParam:
    pathMeshroom=""

    @staticmethod
    def ReplaceParam(text, imageFolder):
        if not os.path.exists(ReplaceConstParam.pathMeshroom):
            QtWidgets.QMessageBox.critical("Ошибка", "Путь к Meshroom.exe указан не верно")
            return 1

        text = text.replace("{PreImageFolder}", os.path.dirname(imageFolder))
        text = text.replace("{AliceFolder}", "D:/Meshroom-2021.1.0/aliceVision")
        text = text.replace("{BaseFolder}", os.path.dirname(sys.argv[0]))
        text = text.replace("{ImageFolder}", imageFolder)
        text = text.replace("{NameImageFolder}", os.path.basename(imageFolder))
        return text