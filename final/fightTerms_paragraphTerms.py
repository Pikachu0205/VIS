import jieba

# 自訂字典
jieba.load_userdict('./CondorHeroes/source/dict.txt')

# 打鬥詞
with open('CondorHeroes/source/fightDict.txt', 'r', encoding='utf-8') as dict_file:
    fight_dict = dict_file.readlines()

    # 章節
    for i in range(1, 41):
        chapter = str(i) + '.txt'
        with open('./CondorHeroes/Stories/' + chapter, 'r', encoding='utf-8') as in_file, open(
                './CondorHeroes/output/statistics/' + str(i) + '.csv', 'a', encoding='utf-8') as out_file:
            textLines = in_file.readlines()

            # 行
            for line in textLines:
                wordList = jieba.cut(line)

                # 初始計算
                terms = 0
                fightTerms = 0
                # 詞
                for word in wordList:
                    if word not in ['“', '”', '，', '。', '』', '『', '：', '！', '？', '…', '；', ' ', '\t', '\n', '　']:
                        terms += 1

                    if word + '\n' in fight_dict:
                        # 紫色的字
                        print('\033[1;35m' + word + '\033[0m', end=' ')

                        fightTerms += 1
                        continue

                    print(word, end=' ')

                # print(fightTerms, terms)

                # 文件輸出
                writeLine = str(fightTerms) + ',' + str(terms) + '\n'
                out_file.write(writeLine)
