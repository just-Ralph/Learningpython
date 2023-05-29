import os
os.system('clear')
#my own fizbuzz code

fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0

for num in range(1,1000001):
	if (num % 3 == 0) and (num % 5 == 0):
		print(str(num) + " Fizzbuzz!")
		fizzbuzzcount += 1

	elif (num % 3 == 0):
		print(str(num) + " Fizz!")
		fizzcount += 1

	elif (num % 5 == 0):
		print(str(num) + " Buzz!")
		buzzcount += 1

	else:
		print(str(num) + " .")


print ("_____________________")
print ("Fizz\t\tBuzz\t\tFizzbuzz")
print (str("{:,}".format(fizzcount)) + "\t\t" + str("{:,}".format(buzzcount)) + "\t\t" + str("{:,}".format(fizzbuzzcount)))


