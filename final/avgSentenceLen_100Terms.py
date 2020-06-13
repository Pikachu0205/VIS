import jieba
import os
import statistics

# 自訂字典
jieba.load_userdict('./CondorHeroes/source/dict.txt')

# 建路徑
try:
    os.mkdir('./CondorHeroes/output/statistics/avgSentenceLen_100Terms/')
except FileExistsError:
    pass

# 章節
for i in range(1, 41):
    chapter = str(i) + '.txt'
    with open('./CondorHeroes/Stories/' + chapter, 'r', encoding='utf-8') as in_file, open(
            './CondorHeroes/output/statistics/avgSentenceLen_100Terms/' + str(i) + '.csv', 'a',
            encoding='utf-8') as out_file:
        texts = in_file.read()
        wordList = jieba.lcut(texts)

        # 初始計算
        terms = 0
        sentenceLen = 0
        sentenceLenList = []

        # 詞
        for word in wordList:
            # print(word, end=' ')

            if word not in ['“', '”', '，', '』', '『', '：',
                            '！', '？', '…', '；', ' ', '\t', '\n', '　']:
                if word != '。':
                    sentenceLen += len(word)
                    terms += 1

                elif word == '。':
                    print(sentenceLen)
                    sentenceLenList.append(sentenceLen)
                    sentenceLen = 0

            # 文件輸出
            if terms == 100:
                try:
                    print('\033[1;35m' + str(round(statistics.mean(sentenceLenList)))+ '\033[0m')
                    writeLine = str(round(statistics.mean(sentenceLenList))) + '\n'
                    out_file.write(writeLine)
                except statistics.StatisticsError:
                    pass
                terms = 0
                sentenceLen = 0
                sentenceLenList = []
