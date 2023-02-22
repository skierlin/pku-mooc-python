data = input()
data_new = ''
if data[0] =='-':
    data_new = '-' + data[1:][::-1]
else:
    data_new = data[::-1]

print(int(data_new))