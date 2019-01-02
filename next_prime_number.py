def find_prime(n):
	while True:
		for i in range(sqrt(a)):
			if(n%i==0):
				break
		else:
			return n


while True:
	x = 2
	print(find_prime(x))

	#Ask to get another prime number
	another = input('Do you want to get another prime number? Please enter y or n ':)
	if another[0].lower() == 'y':
		continue
	else:
		break
