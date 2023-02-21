

x = float(input())

if ( x >= 0 and x < 5 ):
    print('%.3f' % (-x+2.5))
elif (x >= 5 and x < 10):
    print('%.3f' % (2-1.5*(x-3)*(x-3)))
else:
    print('%.3f' % (x/2-1.5))