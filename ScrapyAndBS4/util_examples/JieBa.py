import jieba

""" JieBa分词处理，用'|'分割  """
# 返回的seg_list是一个生成器，不是列表
def JieBaWordDealt(string):
    seg_list = jieba.cut(string)  # 默认是精确模式
    # file_name为自定义词典的路径
    # jieba.load_userdict(file_name)
    # 词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
    # file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。

    return  seg_list