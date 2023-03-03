n = int(input())
totol_data = {}
for i in range(n):
    name, score = input().split()
    totol_data[name] = int(score)
sort_data_key = sorted(totol_data.items())
sort_data = sorted(sort_data_key, key=lambda x: x[1], reverse=True)
for name, score in sort_data:
    print(name + " " + str(score))

# print(sort_data)
