import sys, os
import re
import replaceConstParam
import subprocess
import datetime



def SilentMkdir(theDir):
    try:
        os.mkdir(theDir)
    except:
        pass
    return 0

def pars(str):
    arr = str.split()
    currentParam = ''
    strParam = ''
    dict = {}
    for x in range(1, len(arr)):
        if (re.match(r'--*', arr[x])):
            if (currentParam!=''):
                dict[currentParam] = [strParam.strip(),0]
            #print(currentParam+' '+ strParam.strip())
            currentParam = arr[x]
            strParam = ''
        else:
            strParam += ' ' + arr[x]
    #print(currentParam+' '+ strParam.strip())
    dict[currentParam] = [strParam.strip(), 0]
    node = Node(arr[0], arr[0], dict)
    return node



class Node:
    def __init__(self, name, run, dict):
        self.name = name
        self.run = run
        self.dict = dict

    def output(self):
        str = self.run
        for key in self.dict:
            str += ' ' + key + ' ' + self.dict.get(key)[0]
        return str

    def searchAndCreateFolder(self,folder):
        for key in self.dict:
            path = replaceConstParam.ReplaceConstParam.ReplaceParam(self.dict.get(key)[0],folder).strip("'").strip('"')
            path = os.path.normpath(path)
            if (re.match(r'([A-Za-z]:\\)((?:.*\\)?)', path)):
                if not(os.path.exists(path)):
                    if (re.match(r'([A-Za-z]:\\)((?:.*\\)?)([\w\s]+\.\w+)', path)):
                        if not(os.path.exists(os.path.dirname(path))):
                            os.makedirs(os.path.dirname(path))
                    else:
                        print("Create: ", path)
                        os.makedirs(path)


    def replace(self,node):
        self.name=node.name
        self.run=node.run
        self.dict=node.dict

    def runBuild(self,folder,DialogRunBuild,dt: datetime.datetime):

        if not(os.path.exists(replaceConstParam.ReplaceConstParam.ReplaceParam(self.run,folder))):
            return 1;

        if not os.path.exists("logs\\" + os.path.basename(folder)+"\\"+self.name): os.makedirs("logs\\" + os.path.basename(folder)+"\\"+self.name)

        print(dt.strftime("log %d-%m-%y %H.%M.%S"))
        ofile=open("logs\\" + os.path.basename(folder)+"\\"+self.name+"\\log"+dt.strftime(" %d-%m-%y %H.%M.%S")+".txt", 'w')

        a = self.output()
        cmdLine = replaceConstParam.ReplaceConstParam.ReplaceParam(self.output(),folder)
        self.searchAndCreateFolder(folder)

        warn = 0

        try:
            print(cmdLine)
            ofile.writelines(cmdLine)
            with subprocess.Popen(cmdLine, stderr=subprocess.PIPE, universal_newlines=True) as process:
                for line in process.stderr:
                    if (DialogRunBuild.isEnd):
                        process.terminate()
                        return 4
                    print(line.replace('!', '#'), end='')
                    ofile.writelines(line.replace('!', '#'))
                    if line.__contains__("[fatal]"):
                        print("fatal error")
                        warn = 2

            #(out, err) = proc.communicate()

        except subprocess.CalledProcessError as err:
            print(err)
            ofile.writelines(err)
            return 3

        finally:
            ofile.close()

        return warn