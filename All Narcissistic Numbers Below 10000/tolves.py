import time


def run(num):
	num = abs(num)

	results = []

	for i in range(0,num):

		length = len(str(i))

		x = list(str(i))

		sum = 0

		for item in x:

			sum = sum + pow(int(item),int(length))

			if(sum > i):

				break

		if(sum == i):

			results.append(sum)

	print(results)


start = time.clock()

run(100000)

elapsed = (time.clock() - start)

print("Time used:",elapsed)