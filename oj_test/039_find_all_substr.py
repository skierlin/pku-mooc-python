# 4
# ababcdefgabdefab ab
# aaaaaaaaa a
# aaaaaaaaa aaa
# 112123323 a

n = int(input())
temp = ''
for i in range(n):
    a, b = input().split()
    if b not in a:
        print("no")
    else:
        temp = a
        last_index = 0
        len_b = 0
        while b in a[last_index+len_b:]:
            # print(a[last_index+len_b:])
            index = int(a.find(b, last_index+len_b))
            print(index, end=" ")
            # print(index+last_index)
            last_index = index
            len_b = len(b)
            # temp = a[index+len(b):]
            # print(temp)
        print()