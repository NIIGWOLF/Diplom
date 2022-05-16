import os,sys
def ReplaceConstParam(text, imageFolder):
    text = text.replace("{PreImageFolder}", os.path.dirname(imageFolder))
    text = text.replace("{AliceFolder}", "D:/Meshroom-2021.1.0/aliceVision")
    text = text.replace("{BaseFolder}", os.path.dirname(sys.argv[0]))
    text = text.replace("{ImageFolder}", imageFolder)
    text = text.replace("{NameImageFolder}", os.path.basename(imageFolder))
    return text