dir = '1900.txt'
with open('./olympic_shotpush_data/scores/'+dir ,'r') as in_file:
    data = in_file.readline()
    for d in data:
        print(d)