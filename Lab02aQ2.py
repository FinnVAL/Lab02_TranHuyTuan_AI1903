#Ý 1 câu Q2
def showEmployee(n,s = 9000):
    print("Name: ",n," salary: ", s)
showEmployee("Ben", 12000)
showEmployee("Jessy")
#Ý 2 câu Q2
def outer_fun(a,b):
    def inner_fun(x,y):
        return x+ y
    sum = inner_fun(a,b)
    return sum +5
result = outer_fun(5,10)
print(result)