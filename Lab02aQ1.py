#Ý 1 Câu Q1
def func1(*n):
    for i in n:
        print(i)
func1(20,40,60)
func1(80,100)
#Ý 2 Câu Q1
def calculation (a,b):
    sum = a + b
    dif = abs(a - b)
    return sum, dif
res = calculation(40,10)
print(res)