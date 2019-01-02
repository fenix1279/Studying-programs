from math import sqrt

def find_prime():
	n = 2
	cause = False
	while True:
		#It's variable to check if we need to ask user to continue  
		cause = False

		for i in range(2,int(sqrt(n))+1):
			if(n%i==0):
				cause = True
				n+=1
				break
		else:
			print(n)

		if cause:
			continue
		#Ask to continue finding prime number
		looking = input('Do you want to get another prime number? Please enter y or n: ')
		if looking[0].lower() == 'y':
			n+=1
			continue
		else:
			break

find_prime()
