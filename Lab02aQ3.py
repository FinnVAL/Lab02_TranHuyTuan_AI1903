#Ý 1 câu Q3
def addition(n):
    if n == 0:
        return 0
    else:
        return n + addition(n-1)
res = addition(10)
print(res)
#Ý 2 câu Q3
def display_student(name, age):
    print(name, age)
display_student("Emma",26)
show_student = display_student
show_student("Emma", 26)