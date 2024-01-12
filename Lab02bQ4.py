while True:
    try:
        m = int(input("Nhập vào số m: "))
        n = int(input("Nhập vào số n: "))
        if m < n:
            break
        else:
            print("Hãy nhập lại sao cho m < n!")
    except:
        print("Hãy nhập vào số nguyên!")
print("Những số đối xứng trong khoảng từ m tới n là:")
for num in range(m, n + 1):
    check = str(num) == str(num)[::-1]
    if check:
        print(f"{num}")