def Factorial(n):
    assert(n >= 0),"Factorial of negative number is not defined"
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
    
try:
    print(Factorial(-45))
except Exception as ob:
    print(ob)
try:
    print(Factorial(45))
except Exception as ob:
    print(ob)

print("Thank You")
