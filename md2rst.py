#!/usr/bin/python3
import os
import copy
import shutil
import functools

cur_path = os.getcwd()
path = os.path.join(cur_path, 'content')

def getFileName(suffix:str, path:str)->[str,str]:
    '''@:param suffix 代表文件后缀名'''
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(suffix):
                yield [root, name]

def convert():
    '''格式转换'''
    for root, name in getFileName('.md',path):
        sourceFile = os.path.join(root, name)
        outputFile = os.path.join(root, name.replace('md', 'rst'))
        os.system('pandoc ' + sourceFile + ' -o ' + outputFile)

def format():
    for root, name in getFileName("rst",path):
        with open(os.path.join(root, name), mode='r+') as f:
            lines = f.readlines()
            formatText(lines, "**NOTE**:", ".. note:: ")
            formatText(lines, "**TIPS**:", ".. hint:: ")
            formatPara(lines, '###', '~~~~~~~~~~~~~~~~~~~')
            f.seek(0)
            f.truncate()
            f.writelines(lines)

def formatText(lines:[str], startStr:str, replaceStr:str)->[str]:
    is_tabled = False
    i = 0
    while i < len(lines):
        if(lines[i].startswith(startStr)):
            lines[i] = lines[i].replace(startStr, replaceStr)
            is_tabled = True
            i+=1
            continue
        if is_tabled:
            lines[i] = '   ' + lines[i]
        if len(lines[i]) ==0 or lines[i].isspace() and is_tabled:
            is_tabled = False
        i+=1
    return lines

def formatPara(lines:[str], startStr:str, appendStr:str)->[str]:
    i = 0
    while i <len(lines):
        if(lines[i].startswith(startStr)):
            lines[i] = lines[i].replace(startStr, '')
            lines.insert(i+1,appendStr)
        i+=1
    return lines

def moveFile():
    for root, name in getFileName('rst',path):
        des_path = root.replace('content', 'rst')
        if not os.path.exists(des_path) :
            os.makedirs(des_path)
        shutil.move(os.path.join(root, name), os.path.join(des_path, name))

def createIndex():
    # 获取文件列表
    files = dict()
    for root, name in getFileName("rst", os.path.join('rst')):
        root = root.replace('rst/', '')
        if( root == 'rst'):
            continue
        if root not in files.keys():
            files[root] = []
        files[root].append(name.replace('.rst', ''))
    # 对文件夹和文件进行排序
    files2 = dict()
    dirs = list(files.keys())
    dirs.sort(key=functools.cmp_to_key(cmpCustomed))
    for dir in dirs:
        namess = files[dir]
        namess.sort(key=functools.cmp_to_key(cmpCustomed))
        files2[dir] = namess
    filelist = []
    for dir in dirs:
        for name in files2[dir]:
            filelist.append(os.path.join(dir, name))
    # 写入索引文件
    with open(os.path.join(os.path.join(cur_path, 'rst'), 'index.rst'), 'w+') as f:
        print(os.path.join(cur_path, 'rst'))
        start = r'''
CMake Cookbook 中文版
======================

.. toctree::

'''
        f.write(start)
        for line in filelist:
            line = '   ' + line + '\n'
            f.write(line)
        f.close()

def cmpCustomed(x:str, y:str):
    if x.__contains__('preface'):
        return -1
    if y.__contains__('preface'):
        return 1
    x = x.replace('chapter', '')
    y = y.replace('chapter', '')
    x = x.replace('-chinese', '')
    y = y.replace('-chinese', '')
    return float(x) - float(y)

convert() # 将 md 转换为 rst
format() # 将 note, tips, 三级目录转换为 rst 形式
moveFile() # 将转换的文件移动到 rst 文件夹下
createIndex() # 创建 index.rst 文件

