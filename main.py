def factorial(n):
    #if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial of n is n times the factorial of (n-1)
        return n * factorial(n - 1)
num=int(input("Enter a value:"))
result = factorial(num)
print("The factorial of {} is {}".format(num,result))  
