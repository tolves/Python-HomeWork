def flower(i,list=[0,0,0,0]):
    if list[0]**i+list[1]**i+list[2]**i+list[3]**i==list[0]*1000+list[1]*100+list[2]*10+list[3]:
        print(list[0]*1000+list[1]*100+list[2]*10+list[3],'\n')

def Judge(list,i=4):
    for k in range(0,i):
        if list.pop(0)==0:
            i=i-1
        else:
            break
    return i
    

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                list1=[a,b,c,d]
                list2=[a,b,c,d]
                flower(Judge(list1),list2)
