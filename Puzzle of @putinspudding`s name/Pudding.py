#utf-8
target = open('Hun.txt')
for i in range(0,25):
    list=target.readline()
    for i in list:
        if i!="\n":
            print (i+'日天')
