from opencc import OpenCC
s2t = OpenCC('s2t')


for i in range(2, 41):
    file = str(i)+'.txt'
    with open('./CondorHeroes/'+ file, 'r', encoding='utf-8') as in_file, open('./CondorHeroes/newFiles/'+ file, 'a', encoding='utf-8') as out_file:
        line = in_file.readline()
        while line:
            if line == '\n':
                line = in_file.readline()
                continue
            line = s2t.convert(line)
            out_file.write(line)
            line = in_file.readline()