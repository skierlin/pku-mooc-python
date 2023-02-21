x, a, b ,c, d = map(float, input().split())

result = a*pow(x,3) + b*pow(x,2) + c*x + d
print('%.7f' % result)