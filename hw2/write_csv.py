import os

with open('olympic_shotpush_data/scores.csv', 'a') as out_file:
    dirs = os.listdir('./olympic_shotpush_data/scores')
    for dir in dirs:
        with open('./olympic_shotpush_data/scores/'+dir, 'r') as data_file:
            data = data_file.readline()
            while data:
                out_file.write(dir[:-4])
                out_file.write(',')
                out_file.write('10,')
                out_file.write(data.strip())
                out_file.write('\n')
                data = data_file.readline()