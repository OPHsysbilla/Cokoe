# encoding=utf-8

import csv
import codecs
import re
import jieba
import  ScrapyAndBS4.util_examples.FileIO as FIO
import  ScrapyAndBS4.util_examples.OSPath as oP
import  ScrapyAndBS4.util_examples.JieBa as Jba
# 将重复10行的文本 extracted_news 以 标题内容 的形式 写入 csv 文件


def cut_word_into_matrix(path,BanList=None):
    # 除去全角的所有新闻条目   .csv
    parent_dir = oP.split(path)[0]
    csvFile_path = oP.join(parent_dir, "allNews.csv")
    csvFile =codecs.open(csvFile_path, 'w', 'utf_8_sig')
    writer2 = csv.writer(csvFile, dialect='excel')
    writer2.writerow([u'标题', u'内容'])

    # 分词后的文件
    fseg_path = oP.join(parent_dir, "seg_list.txt")
    with open(fseg_path, 'w', encoding='utf-8') as fseg:
        for filepath in FIO.getFile(path):
            #        -----             剔除txt文件前9行的重复标题
            for content in FIO.load_one_txt(filepath, 9):
                #  如果内容不为空
                if content and len(content)>1:
                    # 文字处理 去除全角
                    title =  FullToHalf(content[0])
                    article = FullToHalf(content[1])
                    news = [title, article]
                    writer2.writerow(news)
                    csvFile.flush()
                    # 剔除 标题在BanList中的广告
                    if BanList and not isAds(title):
                        total_content = " ".join(news)
                        dropPunc_content = dropPunctuation(total_content)
                        seg_list = Jba.JieBaWordDealt(dropPunc_content)  # 默认是精确模式
                        for seg in seg_list:
                            fseg.write(seg)
                            fseg.write('|')
                        # os.linesep 可以根据系统自动选择换行符
                    fseg.flush()
    csvFile.close()





""" 字符串去除符号，用','断句，没有其他符号 """
def dropPunctuation(s):

    # # 去除逗号句号分号，改用","断句
    # stopSym = r'[/.，,。]'
    # dropStopSym = reSub(pattern=stopSym, repl=',', string=s)

    # # 去除符号(不匹配,)
    # dropOtherSym = r'(?!,)\W+'
    # temp = reSub(pattern=dropOtherSym,repl = ' ',string=dropStopSym)

    # 去除符号(所有符号)
    dropOtherSym = r'\W+'
    temp = reSub(pattern=dropOtherSym,repl = ' ',string=s)

    # 去除连续空格
    blank_space = r'\s+'
    res = reSub(pattern=blank_space,repl = ' ',string=temp)

    return res

def dropComma(s):
    comma = r','
    res = reSub(pattern=comma,repl = ' ',string=s)
    print(res)
    return res


""" 封装的re.sub函数 """
def reSub(pattern,string,repl):
    comp = re.compile(pattern= pattern,
                     flags=re.U)
    res = comp.sub(repl=repl,string=string)
    return res


""" 符号替换 英-中 或者 对应映射替换 """
def replaceCnToEn(s):
    import string
    # cn_punctuation = r'！？“”#$&‘’（）*+-，。、：；《》=@……——·~{|}【】⊙'
    # en_punctuation = r'!?""#$&''()*+-,.,:;<>=@^_``{|}[]-'
    fromstr = r'！？‘’，、。“”'
    tostr = r'.."",,.""'
    transtab = s.mak(fromstr,tostr)
    return (s.translate(transtab))

""" 判断是否是广告（未完善）  """
def isAds(title,BanList=None):
    #  如果内容不为空
    flagIsAds = False
    # 剔除 标题在BanList中的广告
    if title:
        if BanList:
            if title in BanList:
                flagIsAds = True
    return flagIsAds

""" 字符串全角转半角  """
def FullToHalf(ustring) :
    strList = []
    for ch in ustring:
        inside_code=ord(ch)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        else:
            strList.append(ch)
            continue
        strList.append(chr(inside_code))
    return "".join(strList)

if __name__ == "__main__":
    path = r"D:\My\PyProject\extracted_news"
    BanList = ['出租','出售','搜狐房产'] # 剔除 标题在BanList中的广告
    cut_word_into_matrix(path,BanList=BanList)

    # seg_list = jieba.cut(totalStr)  # 默认是精确模式
    # fseg.write(seg_list.join(","))
    # fseg.write(r'\n')
    # print(", ".join(seg_list))

