import time

def PowSum(numbers):
    Sum=0
    New_list=iteration(numbers)
    x=digits(numbers)
    
    for n in range(0,x):
        Sum=int(New_list[n])**x+Sum
    return Sum

def flower(Numbers):
    if PowSum(Numbers)==Numbers:
        print(Numbers,'\n')

def iteration(numb):
    # Origin_list=[]
    # for i in range(0,times):
    #     Origin_list.append((numb//(10**(times-1-i)))%10)
    # return Origin_list

    return list(str(numb))

def digits(nu):
    for i in range(0,100):
        if nu//(10**i)==0:
            return i
    # return 4

start = time.clock()



for num in range(0,10000):
	# x = digits(num)
	# list1=iteration(num,int(x))
    # list1=iteration(num,digits(num))
	flower(num)
    # flower(digits(num),num,digits(num))

elapsed = (time.clock() - start)

print("Time used:",elapsed)
