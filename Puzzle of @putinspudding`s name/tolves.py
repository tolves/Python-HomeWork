# -*- coding: utf-8 -*-
class Puzzle:
    def __init__(self):
        
        return None

    def main(self, dic_path, out_path):
        
        f = open(dic_path, encoding='utf-8')
        
        surname = f.readline().split(" ")
        
        #for line in f:
        #    line=line.strip('\n').strip('\t')
        #    surname.append(line)
        #surname = surname[0].split(" ")

        out = '\n'.join(str(x)+'日天' for x in surname)

        #out = list(map(lambda x: x+'日天', surname))

        o = open(out_path, 'w', encoding='utf-8')

        o.write(str(out))
        
        #print(out)
x = Puzzle()
x.main('Hundred_Family_Surnames.txt','tolves_out.txt')

