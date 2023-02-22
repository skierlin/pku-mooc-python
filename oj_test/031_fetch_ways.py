def ways(m, n, s):
    # 第一类，各种特殊情况
    if s < 0 or n < 0 or m <= 0:  # 当输入数据小于0时，取法为0
        return 0
    elif n == 0 and s == 0:  # 当n==0且s==0时，只有1种取法
        return 1
    elif n == 0 and s > 0:  # 当取0个，但是s>0时，取法为0
        return 0
    elif n == 1:  # 判断n=1的情况
        if m >= s:
            return 1  # 若m>=s,只有1种取法
        else:
            return 0  # 若m<s,则取法为0
    elif m >= n and s == 0:  # 当m>=n 并且 s=0时 ，只有1种取法
        return 1
    elif n > 1 and s == 1:  # 当n>1且s=0时 ，取法为0
        return 0

    # 第二类，讨论大类
    elif m > s:  # 当m>s时
        if n == s or n > s:
            return 0
        elif 1 < n < s:
            return ways(s - 1, n, s)
    elif m < s:  # 当m<s时
        return ways(m - 1, n - 1, s - m) + ways(m - 1, n, s)  # 当取m时 与 不取m时 的和
    elif m == s:  # 当m=s时
        if n > m:
            return 0
        else:
            return ways(m - 1, n, s)


t = eval(input())  # t组数
for i in range(t):
    m, n, s = map(int, input().split())
    print(ways(m, n, s))
