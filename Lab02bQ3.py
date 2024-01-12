#Ý 1 câu Q3:
while True:
    try:
        n = int(input("Nhập một số nguyên n: "))
        break
    except:
        print("Bạn đã nhập sai, hãy nhập lại!")

#Ý 2 câu Q3:
        
bin_n = bin(n)
print("Dạng số nhị phân của n là: ",bin_n.replace("0b",""))

#Ý 3 câu Q3:

n = int(input("Nhập lại số nguyên n: "))
s = sum(int(i) for i in str(n))
print("Tổng cách chữ số trong số n là: ",s)

#Ý 4 câu Q3:

m = 0
while n > 0:
    t = n % 10
    m = m * 10 + t
    n = n // 10
print("m = ", m)