import time

def PowSum(power,numbers):
    Sum=0
    New_list=iteration(numbers,power)

    for n in range(0,power):
        Sum=int(New_list[n])**power+Sum
    return Sum

def flower(Power,Numbers):
    if PowSum(Power,Numbers)==Numbers:
        print(Numbers,'\n')

def iteration(numb,times=4):
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
	flower(digits(num), num)
    # flower(digits(num),num,digits(num))

elapsed = (time.clock() - start)

print("Time used:",elapsed)