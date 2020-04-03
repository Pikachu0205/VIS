import thulac
from opencc import OpenCC

thu = thulac.thulac()
tt = OpenCC('s2t')
ss = OpenCC('t2s')

chapters = 41
character_names = set()

with open('./CondorHeroes/names_combine_simple.txt','r',encoding='utf-8') as name_file:
  name = name_file.readline()
  while name:
    character_names.add(name.strip())
    name = name_file.readline()

for i in range(1, chapters):
    chapter = './CondorHeroes/' + str(i) + '.txt'
    with open(chapter, 'r', encoding='utf-8') as in_file:
        # text = in_file.read()
        # word_lists = jieba.cut(text)
        # for word in word_lists:
        #     if word in character_names:
        #         print(1)
        print(chapter)
        line = in_file.readline()
        while line:
            line = ss.convert(line)
            word_list = thu.cut(line)
            for word_pos in word_list:
                if word_pos[0] in character_names:
                    print(word_pos[0])
            line = in_file.readline()
