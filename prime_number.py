# Day 1 Question:
#Write a function that takes a number and returns whether it is a prime number or not.

def primenumber(n):
    if n<=1:
        return "Number is not prime"
    for i in range (2, n):
        if n % i == 0 :
            return "Number is not prime"
    return "Number is prime"
n = int(input("Enter a number:"))
print(primenumber(n))

