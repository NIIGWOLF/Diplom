import sys, os
import re

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

    def replace(self,node):
        self.name=node.name
        self.run=node.run
        self.dict=node.dict