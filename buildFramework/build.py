#!/usr/bin env python
# -*- coding: UTF-8 -*-
import sys
import getopt
import json
import os
import shutil

#处理JSON
def handleJSONStr(jsonStr):

    userModuleArr = json.loads(jsonStr)
    #递归补全MVC文件夹
    for i, dic in enumerate(userModuleArr):
        recursiveCreateModuleMVC(dic)
        userModuleArr[i] = dic

    #读取主框架的位置
    arrPath = "./buildArchitecture/build.json"
    buildArrStr = readJSONFile(arrPath)
    buildArr = json.loads(buildArrStr)

    #替换对应的模块位置并替换
    index = -1
    for i, dic in enumerate(buildArr): 
        if 0 == cmp(dic.get("name"), "Modules"):
            index = i
            break

    if index > -1:
        modules = buildArr[index]
        modules["children"] = userModuleArr
        buildArr[index] = modules
        
    #判断是否存在文件夹。存在则删除文件夹及文件夹下所有文件
    if os.path.exists('./Architecture'):
        shutil.rmtree('./Architecture')

    #创建文件夹
    os.makedirs('./Architecture')

    basePath = './Architecture'
    for dic in buildArr:
        recursiveCreateFile(dic, basePath)

#创建文件夹
def recursiveCreateFile(dic, basePath):
    if dic.get('children') is None:
        path = "%s/%s" % (basePath, dic.get('name'))
        if not os.path.exists(path):
            #创建文件夹
            os.makedirs(path)
            #创建占位文件
            placeholderPath = path + '/placeholder.txt'
            file = open(placeholderPath, 'w')
            file.close()
    else:
        children = dic.get('children')
        path = "%s/%s" % (basePath, dic.get('name'))
        for childDic in children:
            recursiveCreateFile(childDic, path)
    
def recursiveCreateModuleMVC(dic):
    if dic.get('children') is None:
        arr = [
            {"name": "Controllers"},
            {"name": "Models"},
            {"name": "Views"}
        ]
        dic["children"] = arr
        return dic
    else:
        children = dic.get("children")
        for i, childDic in enumerate(children):
            childDic = recursiveCreateModuleMVC(childDic)
            children[i] = childDic
        dic["children"] = children
        return dic


#读取JSON
def readJSONFile(path):
    f = open(path, 'r')
    strFile = f.read()
    f.close()
    return strFile

def main(argv):
    opts, args = getopt.getopt(argv, "hi:v:", ["help", "version","ifile="])
    for opt,value in opts:
        if opt in ('-v', "--version"):
            print("Verison is 1.0.0")
            sys.exit()

        if opt in ('-h', "--help"):

            print "build.py -i <inputfile>"
        if opt in ('-i', '-ifile'):
            path = "./%s" % value
            jsonStr = readJSONFile(path)
            handleJSONStr(jsonStr)

if __name__ == "__main__":
    main(sys.argv[1:])
