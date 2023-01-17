#  Write a Python program to find common divisors between two numbers in a given pair.

def comdivi(a,b):
    bnum = max(a,b)
    i=1
    divisors = []
    while bnum>i:
        if a%i==0 and b%i==0:
            divisors.append(i)
        i+=1
    return divisors

print(comdivi(336,360))