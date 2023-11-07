print("just a test for github")

print("just a test for an emergency fix")


print("just a test for remote repo")

number = int(input("calculate factorial of:"))

def factorial(n):
	if(n <= 1):
		return 1
	else:
		return n*factorial(n-1)

print(factorial(number))
