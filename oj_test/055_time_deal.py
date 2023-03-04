import datetime
s=[]
t=[]
while True:
    try:
        s.append(input())
    except:
        break
for i in range(len(s)):
    if i%2==0:
        if len(s[i].split())==5:
            a=datetime.datetime.strptime(s[i],'%Y %m %d %H %M')
        else:
            a = datetime.datetime.strptime(s[i], '%m-%d-%Y %H:%M %p')
    else:
        ss=s[i].split()
        if len(ss)==1:
            a+=datetime.timedelta(seconds=int(ss[0]))
        else:
            a+=datetime.timedelta(days=int(ss[0]),hours=int(ss[1]),minutes=int(ss[2]))
        t.append(a)
for i in t:
    print(i)