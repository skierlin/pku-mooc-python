
x, y , sign = input().split()

if (sign == '+'):
    print(int(x)+int(y))
elif (sign == '-'):
    print(int(x)-int(y))
elif (sign == '*'):
    print(int(x)*int(y))
elif (sign == '/'):
    if(int(y) == 0):
        print("Divided by zero!")
    else:
        print(int(int(x)/int(y)))
else:
    print("Invalid operator!")