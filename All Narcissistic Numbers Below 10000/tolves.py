import time
def run(num):
	num = abs(num)

	result = []

	for i in range(0,num):

		length = len(str(i))

		x = list(str(i))

		sum = 0

		for item in x:

			sum = sum + pow(int(item),int(length))

			if(sum > i):
				break

		if(sum == i):
			result.append(sum)

	print(result)
start = time.clock()
run(100000)
elapsed = (time.clock() - start)
print("Time used:",elapsed)