import time


def run(num):
	
	num = abs(num)

	results = []

	max_length = len(str(num))

	dic = [([0] * (max_length+1)) for i in range(10)]

	#calculate the 0-9 first
	for i in range(10):

		for j in range(max_length + 1):

			dic[i][j] = pow(i, j)

	for i in range(0, num):

		length = len(str(i))

		x = list(str(i))

		sum = 0

		for item in x:

			#almost 0.036s
			# sum = sum + pow(int(item),int(length))

			#directly use the calculated dic to read the value
			#0.028s
			sum = sum + dic[int(item)][int(length)]

			if(sum > i):

				break

		if(sum == i):

			results.append(sum)

	print(results)


start = time.clock()

run(10000)

elapsed = (time.clock() - start)

print("Time used:",elapsed)