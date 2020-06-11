import jieba
from opencc import OpenCC

tt = OpenCC('s2t')


jieba.load_userdict('./CondorHeroes/output/dict.txt')
with open('../CondorHeroes/output/konfu_all.txt', 'r', encoding='utf-8') as file:
    konfuList = file.read().splitlines()
    with open('../CondorHeroes/rawFiles/1.txt', 'r', encoding='utf-8') as in_file:
            # open('./CondorHeroes/output/konfuList.txt', 'a', encoding='utf-8') as out_file:
        # line = in_file.readline()
        # while line:
        #     line = line.strip()
        #     segList = jieba.cut(line)
        #     for word in segList:
        #         if word in konfuList:
        #             print(word)
        #     line = in_file.readline()
        text = tt.convert(in_file.read())
        text = jieba.cut(text)
        for i, word in enumerate(text):
            if word in konfuList:
                print(i, word)