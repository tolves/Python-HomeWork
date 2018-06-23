#utf-8

def PFout(lists,OutFile):
    for i in list:
        if i!='\n':
            output = open(OutFile+'.txt','a')
            output.write(i+'日天\n')
    output.close()

def PFterminate(OutFile):
    ORIGIN_doc = open(OutFile+'.txt','w+')
    if ORIGIN_doc.read()!=None:
        ORIGIN_doc.truncate()
    
def Judge():
    try:
        target = open('Hun.txt')
        return target
    except FileNotFoundError:
        print('ERROR')
        raise SystemExit

Infile=Judge()
Title=str(input('Your file name is?\n'))
PFterminate(Title)
for n in range(0,25):
    list=Infile.readline()
    PFout(list,Title)
Infile.close()
Infile.close()
