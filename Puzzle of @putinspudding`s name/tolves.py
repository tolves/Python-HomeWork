# -*- coding: utf-8 -*-
import sys
class Puzzle:
	def __init__(self):
		
		return None

	def run(self, dic_path, out_path):

		try:

			f = open(dic_path, encoding='utf-8')

		except:

			print(sys.exc_info()[1])

		else:

			surname = f.readline().split(" ")

        # the other solution: split str into list
        #for line in f:
        #    line=line.strip('\n').strip('\t')
        #    surname.append(line)
        #surname = surname[0].split(" ")
        
        f.close
        

        out = '\n'.join(str(x) + '日天' for x in surname)

        # the second solution to add 日天
        #out = list(map(lambda x: x+'日天', surname))

        # the third soulution to add 日天
        #out = []
        #for x in surname:
        #    out.append(x + '日天')
        
        o = open(out_path, 'w', encoding='utf-8')

        o.write(str(out))

        o.close
            
x = Puzzle()
x.run('Hundred_Family_Surnames.txt','tolves_out.txt')

