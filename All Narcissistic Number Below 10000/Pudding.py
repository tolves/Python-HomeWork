def PowSum(power,numbers,digit):
    Sum=0
    New_list=iteration(numbers,digit)
    for n in range(0,digit):
        Sum=New_list[n]**power+Sum
    return Sum

def flower(Power,Numbers,Digit):
    if PowSum(Power,Numbers,Digit)==Numbers:
        print(Numbers,'\n')

def iteration(numb,times=4):
    Origin_list=[]
    for i in range(0,times):
        Origin_list.append((numb//(10**(times-1-i)))%10)
    return Origin_list

def digits(nu):
    for i in range(0,100):
        if nu//(10**i)==0:
            return i

for num in range(0,10000):
    list1=iteration(num,digits(num))
    flower(digits(num),num,digits(num))
