s, s1, s2 = input().split(',')

if (s1 in s) and (s2 in s):
    index1 = s.find(s1)
    # print(index1)
    index2 = s.rfind(s2)
    # print(index2)
    if (index1 + len(s1) <= index2):
        print(index2-index1-len(s1))
    else:
        print(-1)
else:
    print(-1)