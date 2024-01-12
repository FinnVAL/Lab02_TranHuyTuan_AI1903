try:
    num = int(input("original number "))
    x=num
    y=0
    while(num>0):
        y=y*10+num%10
        num=num//10
    if(x==y):
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
except:
    print("Enter a positive integer!")