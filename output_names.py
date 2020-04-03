# import jieba.posseg as pseg
# from opencc import OpenCC
#
# names = set()
#
# for i in range(1, 41):
#     print('chapter: ', i)
#     with open('./CondorHeroes/'+ str(i) +'.txt', 'r', encoding='utf-8') as in_file, \
#             open('./CondorHeroes/characters_jieba.txt', 'a') as out_file:
#         lines = in_file.readlines()
#         cc = OpenCC('t2s')
#
#         for line in lines:
#             line = cc.convert(line)
#             words = pseg.cut(line)
#             for w in words:
#                 if w.flag == 'nr':
#                     if w.word not in names:
#                         names.add(w.word)
#                         tt = OpenCC('s2t')
#                         name = tt.convert(w.word)
#                         out_file.write(name+' ')
import thulac
from opencc import OpenCC

thu = thulac.thulac()
names = set()

tt = OpenCC('s2t')
cc = OpenCC('t2s')

for i in range(1, 41):
    print('chapter: ', i)
    with open('./CondorHeroes/'+ str(i) +'.txt', 'r', encoding='utf-8') as in_file, \
            open('./CondorHeroes/noblank.txt', 'a') as out_file:
        lines = in_file.readlines()

        for line in lines:
            line = cc.convert(line)
            words_pair_list = thu.cut(line)
            for word_pair in words_pair_list:
                if word_pair[1] == 'np':
                        if word_pair[0] not in names:
                            names.add(word_pair[0])
                            name = tt.convert(word_pair[0])
                            out_file.write(name)

