for i in range(1,41):
    with open('./CondorHeroes/Stories/' + str(i) + '.txt', 'r') as in_file:
        line = in_file.readline()
        while line:
            dialog = False
            for word in line:
                if word == '“':
                    dialog = True
                if word == '”':
                    dialog = False
                if dialog == False:
                    print(word, end='')
                if dialog == True:
                    print('\033[1;31m' + word + '\033[0m', end='')
            line = in_file.readline()