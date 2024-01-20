#Ý 1 câu Q1:

while True:
    try:
        n = int(input("Nhập một số nguyên n > 5: "))
        break
    except:
        print("Bạn đã nhập sai, hãy nhập lại!")
while n <= 5:
    while True:
        try:
            n = int(input("Hãy nhập lại một số nguyên n sao cho n > 5: "))
            break
        except:
            print("Bạn đã nhập sai, hãy nhập lại!")

#Ý 2 câu Q1:
            
S1 = 0
for i in range (1, n+1):
    S1 += i
print("S1 = ",S1)

#Ý 2 câu Q1:

def GiaiThua(n):
    if n == 0:
        return 1
    else:
        return n * GiaiThua(n-1)
S2 = GiaiThua(n)
print("S2 = ",S2)

#Ý 3 câu Q1:

S3 = 0
for i in range (1, n+1):
    S3 += 1/i
print("S3 = ",S3)

#Ý 4 câu Q1:

while True:
    try:
        n = int(input("Nhập lại số nguyên n: "))
        break
    except:
        print("Bạn đã nhập sai, hãy nhập lại!")
def check(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False  
    return True
if check(n):
    print("Số n là số nguyên tố")
else:
    print("Số n không phải số nguyên tố")
