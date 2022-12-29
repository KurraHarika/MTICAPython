def checkEvenOdd(num1):
    if num1%2==0:
        return "Even"
    else:
        return "Odd"

for i in range(3):
    num=int(input("Enter a no:"))
    print(num,"is",checkEvenOdd(num))
