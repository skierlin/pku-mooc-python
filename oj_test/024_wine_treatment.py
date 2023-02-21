n = int(input())
origin_data = list(map(int,input().split()))
origin_rate = origin_data[1] / origin_data[0]
for i in range(n-1):
    x, y = map(int,input().split())
    if (origin_rate - y/x >0.05):
        print("worse")
    elif (y/x - origin_rate > 0.05):
        print("better")
    else:
        print("same")

