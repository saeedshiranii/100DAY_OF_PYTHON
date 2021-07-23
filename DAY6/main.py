# a program for check prime number

def prime_checker(d):
    b = d - 1
    while(b>1):
        c = d%b
        b = b-1
        if c == 0:
            print("{d} is not prime")
            break
    if c != 0:
        print(f"{d} is prime")



n = int(input("Check this number: "))
prime_checker(n)
#prime_checker(number=n)
