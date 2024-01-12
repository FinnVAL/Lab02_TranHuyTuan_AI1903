try:
    f = input()
    n = f.split()
    max=0
    for i in range (0, len(n)):
        if int(n[i]) > max:
            max = int(n[i])
    print(max)
except:
    print('Hãy nhập vào 1 dãy số nguyên!')