def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

usernum = input("Number Please: ")

print(factorial(int(usernum)))