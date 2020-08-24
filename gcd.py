#!/usr/bin/python3.6

def gcd(x, y):
    #print("Func call")
    #print("x = ", x)
    #print("y = ", y)
    if y == 0:
        return x
    else:
        #print("x1 = ", x)
        #print("y1 = ", y)
        return gcd(y, x % y)

def user_input():
    check = False
    print("Please input an integer value:")
    while not check:
        try:
            value = int(input())
            check = True
            if value < 0:
                print("\nYou have provided a negative value. Ommiting sign.", end="")
                value = value * -1
        except:
            print("\nThe value you have provided can not be converted to integer.\nPlease try again:")
    print()
    return value

a = user_input()
print("Your first number is:", a, "\n")
b = user_input()
print("Your second number is:", b)
if a < b:
    temp = a
    a = b
    b = temp
    del(temp)

print("\nGreatest common divisor of ", a, " and ", b, " is:\n", gcd(a, b), sep="")