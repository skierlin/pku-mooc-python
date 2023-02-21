#import math

chart = input()
for i in range(3):
    str_total = abs(i-2) * " " + (5-abs(2*(i-2))) * chart
    print(str_total)