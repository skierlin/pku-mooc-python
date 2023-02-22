def TenToSeven(num):
    s = ''
    while abs(num):
        s, num = str(abs(num) % 7) + s, abs(num) // 7
    return s

def TenToNine(num):
    s = ''
    while abs(num):
        s, num = str(abs(num) % 9) + s, abs(num) // 9
    return s

result1, result2, result3 = 0, 0, 0
for i in range(100,999):
    if (TenToSeven(i) == TenToNine(i)[::-1]):
        print(i)
        print(int(TenToSeven(i)))
        print(int(TenToNine(i)))
        break