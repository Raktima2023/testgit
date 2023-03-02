"""
This is a testing file for github    
"""
print("This is a test for git bash commands")

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else :
        return (n*factorial(n-1))
    
val = int(input("Input a number: "))

fact = factorial(val)

print('Factorial of {} : {}'.format(val, fact))