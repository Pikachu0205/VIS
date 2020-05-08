import jieba
from opencc import OpenCC
jieba.load_userdict('./CondorHeroes/output/dict.txt')
s2t = OpenCC('s2t')

with open('CondorHeroes/output/fightDict.txt', 'r') as dict_file:
    fight_dict = dict_file.readlines()
    for i in range(1, 41):
        chapter = str(i) +'.txt'
        with open('./CondorHeroes/'+ chapter, 'r', encoding='utf-8') as in_file:
            textLines = in_file.readlines()
            for line in textLines:
                if line == '\n':
                    continue
                wordList = jieba.cut(line)

                for word in wordList:
                    word = s2t.convert(word)
                    if word+'\n' in fight_dict:
                        print('\033[1;35m' + word + '\033[0m', end=' ')
                        continue
                    print(word, end=' ')