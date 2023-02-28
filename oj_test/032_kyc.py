n, na, nb = map(int, input().split())
list_a_sample = list(map(int, input().split()))
list_b_sample = list(map(int, input().split()))

list_a = list_a_sample*(n//na) + list_a_sample[0: n % na]
list_b = list_b_sample*(n//nb) + list_b_sample[0: n % nb]


a_win = 0
b_win = 0
for i in range(n):
    if (list_a[i] == 0 and list_b[i] == 2) or (list_a[i] == 2 and list_b[i] == 5) or (list_a[i] == 5 and list_b[i] == 0):
        a_win += 1
    elif (list_a[i] == 2 and list_b[i] == 0) or (list_a[i] == 5 and list_b[i] == 2) or (list_a[i] == 0 and list_b[i] == 5):
        b_win += 1

if b_win > a_win:
    print("B")
elif b_win < a_win:
    print("A")
else:
    print("draw")




