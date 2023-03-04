import re
n=int(input())
isfirstprint=True
for j in range(n):
    s = input()
    m = '<(.+?)>(.*?)</\\1>'
    result = re.findall(m, s)
    if len(result) == 0:
        if not isfirstprint:
            print("\n",end="")
        print("NONE",end="")
        isfirstprint=False
    else:
        isNone = True
        for x in result:
            # 查找电话号码
            m = '\([0-9]{1,2}\)-[0-9]{3,}'
            phone_maybe = re.findall(m, x[1])
            if len(phone_maybe) == 0:
                continue
            else:
                phone = []
                for tmp in phone_maybe:
                    if len(re.findall('-[0-9]+', tmp)[0]) < 5:
                        phone += re.findall('\(([0-9]{1,2})\)-[0-9]{3,}', tmp)
                if len(phone) > 0:
                    isNone=False
                    if not isfirstprint:
                        print("")
                    isfirstprint=False
                    print("<" + x[0] + ">", end="")
                    isFirstPrinthere=True
                    for tt in phone:
                        if not isFirstPrinthere:
                            print(",", end="")
                        print(tt, end="")
                        isFirstPrinthere=False
                    print("</" + x[0] + ">",end="")
        if isNone==True:
            if not isfirstprint:
                print("")
            print("NONE",end="")
            isfirstprint=Fals