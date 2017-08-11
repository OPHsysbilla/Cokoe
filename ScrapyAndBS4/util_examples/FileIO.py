# coding:utf-8

import os ,os.path
import csv
import codecs
import collections
import  ScrapyAndBS4.util_examples.OSPath as oP
import ScrapyAndBS4.util_examples.config as cfg

"""
os.path.walk()与os.walk()产生的文件名列表不同：
os.walk() 只产生文件路径
os.path.walk()    产生目录树下的目录路径和文件路径
"""
# 方法1：递归遍历目录
def visitDir1(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):  # 判断路径是否为文件，如果不是继续遍历
            visitDir1(pathname)
        else:
            print(pathname)

# 方法3： 函数递归os.walk()
def getFile(dirpath,frontNum = 0):
    for root, dirs, files in os.walk(dirpath):
        for fileName in files:
            yield(os.path.join(root, fileName))


# \u3000 全角空格
def load_one_txt(filepath,delTopLinesNum=0):
    with open(filepath, 'r',encoding='utf-8') as f:
        #  跳过头部delTopLinesNum行
        lines = f.readlines()
        content = []
        for line in lines:  #  确定中文范围 : [\u4e00-\u9fa5]，范围内可能有表情符
            content.append(line.strip()
                           .replace("\u3000"," ")    # 全角空格
                           .replace("\ue40c"," "))   # 表情符
        return content[delTopLinesNum:]
        # 返回字典 {"content": ,"title":  }

def writelines_file(filepath,lines):
    with open(filepath, 'w') as f:
        #  跳过头部delTopLinesNum行
        f.writelines(lines)

def writev_dict_csv(storePath,writeDict):
    # 从字典写入csv文件，没用到
    with open(storePath,'w', newline='') as csvFile3:
        writer2 = csv.writer(csvFile3)
        for key in writeDict:
            writer2.writerow([key, writeDict[key]])

# 将重复10行的文本 extracted_news 以 标题内容 的形式 写入 csv 文件
def write_News_csv(path,BanList=None):
    with codecs.open(os.path.join(path,"res.csv"), 'w', 'utf_8_sig') as csvFile3:
        writer2 = csv.writer(csvFile3,dialect='excel')
        writer2.writerow([u'标题',u'内容'])
        for filepath in getFile(path):
            #        -----             剔除前9行
            content = load_one_txt(filepath, 9)
            if BanList:
                #  如果内容不为空
                if content:
                    # 剔除 标题在BanList中的广告
                    title = content[0]
                    if not title in BanList:
                        writer2.writerow(content)
            else:
                if content:
                        writer2.wlriterow(content)

def loadFile(parentpath, filename):
    if str(filename).endswith(".csv"):
        raise NotImplementedError(
            "FileIO.loadFile: please use loadCSV() to load '.csv' file, or you will encounter with encoding problem")
    filepath = oP.pathJoin(parentpath,filename)
    with open(filepath, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        content = []
        for line in lines:
            content.append(line.strip())
        return content
        # 返回字典 {"content": ,"title":  }

def saveFile(parentpath, filename,data):
    if str(filename).endswith(".csv"):
        raise NotImplementedError(
            "FileIO.saveFile: please use saveCSV() to save '.csv' file, or you will encounter with encoding problem")
    filepath = oP.pathJoin(parentpath,filename)

    with open(filepath, 'w',encoding='utf-8') as f:
        if isinstance(data,str):
            f.write(data)
            f.flush()
        elif isinstance(data,collections.Iterable):
            f.writelines(data)
            f.flush()
        print("saveFile sucess:",filepath)


def loadCSV(parentpath, filename):
    with codecs.open(oP.pathJoin(parentpath, filename), 'w', 'utf_8_sig') as csvFile3:
        return csvFile3.reader(dialect='excel')


if __name__ == "__main__":
    path = cfg.stopWords_parent_dir
    s2700 = set(loadFile(path,'stopwords2700.txt'))
    s1800 = set(loadFile(path,'stopwords1800.txt'))
    s1500 = set(loadFile(path,'stopwords1500.txt'))
    print(s1800-s1500)

