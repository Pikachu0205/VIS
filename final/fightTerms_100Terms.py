import jieba
import os

# 自訂字典
jieba.load_userdict('./CondorHeroes/source/dict.txt')

# 建路徑
try:
    os.mkdir('./CondorHeroes/output/statistics/fightTerms_100Terms/')
except FileExistsError:
    pass

# 打鬥詞
with open('CondorHeroes/source/fightDict.txt', 'r', encoding='utf-8') as dict_file:
    fight_dict = dict_file.readlines()

    # 章節
    for i in range(1, 41):
        chapter = str(i) + '.txt'
        with open('./CondorHeroes/Stories/' + chapter, 'r', encoding='utf-8') as in_file, open(
                './CondorHeroes/output/statistics/fightTerms_100Terms/' + str(i) + '.csv', 'a',
                encoding='utf-8') as out_file:
            texts = in_file.read()
            wordList = jieba.lcut(texts)

            # 初始計算
            terms = 0
            fightTerms = 0
            # 詞
            for word in wordList:
                if word not in ['“', '”', '，', '。', '』', '『', '：',
                                '！', '？', '…', '；', ' ', '\t', '\n', '　']:
                    terms += 1

                if word + '\n' in fight_dict:
                    # 紫色的字
                    fightTerms += 1
                    print('\033[1;35m' + word + '\033[0m', end=' ')
                else:
                    print(word, end=' ')

                # 文件輸出
                if terms == 100:
                    writeLine = str(fightTerms) + ',' + str(terms) + '\n'
                    out_file.write(writeLine)
                    terms = 0
                    fightTerms = 0
