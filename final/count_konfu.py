import jieba


jieba.load_userdict('./CondorHeroes/output/dict.txt')

for i in range(1, 41):
    with open('./CondorHeroes/' + str(i) + '.txt', 'r', encoding='utf-8') as in_file, open(
        './CondorHeroes/output/konfuList.txt', 'a', encoding='utf-8') as out_file:
        line = in_file.readline()
        while line:
            line = line.strip()
            segList = jieba.cut(line)
            print(' '.join(segList))
            line = in_file.readline()