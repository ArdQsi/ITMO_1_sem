#json -> csv формат
import re

all =[]
spisok =[]
file1 = open("input.json","r",encoding="UTF-8")
for x in range(31):
    f = file1.readline()
    if 6 <= x <= 25: 
        if x == 6:
            kl1 =re.findall('\w+',f)
        if 7 <=x <=13:
            key = re.search('\w+',f)
            #print(key.group())
            #print(kl.group() +'/' + key.group() +',')
            all.append(key.group())
            val1 = re.search(': "[\w\s,-.:]+',f)
            s = val1.group().replace(': "', '')
            spisok.append(s)
        if x== 17:
            kl2 = re.findall('\w+',f)
        if 18<=x<=24:
            val2 = re.search(': "[\w\s,-.:]+',f)
            s = val2.group().replace(': "', '')
            spisok.append(s)
for x in range(7):
    x = kl1[0] + '/' + all[x] + ';'
    print(x, end = '')
for x in range(7):
    y = kl2[0]+ '/' + all[x] + ';'
    if x==6:
         print(kl2[0]+ '/' + all[x])    
    else:
        print(y, end = '')
for x in range(14):
    if 0<=x<=6:
        print(spisok[x]+ ';',end ='')
    if x==6:
        print(spisok[x]+ ';'+';'*7)
    if x== 7:
        print(';'*7, end='')
    if 7<=x<=12:
        print(spisok[x]+ ';',end ='')
    if x ==13:
        print(spisok[x])





