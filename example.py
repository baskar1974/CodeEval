#write a python function for sum of first 10 natural numbers
# sum_10 = 1+2+3+...+10

def sum_10(n):
    total = 0
    for i in range(0,n+1):
        total += i
    return total

print(sum_10(10))

# 2. Write a python function for multiplication of two numbers
# multip = 2*3

def multip(x,y):
    total = 