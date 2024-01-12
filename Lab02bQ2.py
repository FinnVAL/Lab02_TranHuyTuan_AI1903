m = int(input("Nhập vào số m: "))
n = int(input("Nhập vào số n: "))

#Ý 1 câu Q2:

def check(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def result(m, n):
    USC = []
    for i in range(2, min(m, n) + 1):
        if m % i == 0 and n % i == 0 and check(i):
            USC.append(i)
    return USC

def main():
    output = result(m, n)
    print("Ước số chung là số nguyên tố của m và n:", output)

if __name__ == "__main__":
    main()

#Ý 2 câu Q2:

import math
x = math.gcd(m, n)
print("Ước chung lớn nhất của 2 số m và n là: ",x)

#Ý 3 câu Q2:

y = math.lcm(m, n)
print("Bội chung nhỏ nhất của 2 số m và n là : ",y)