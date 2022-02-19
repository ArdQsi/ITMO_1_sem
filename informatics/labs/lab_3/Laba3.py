import re
eyes = [":",";","X","8","="]
nose = ["-","<","-{","<{"]
mouth = ["(",")","O","|","\\","/","P"]
isu = 291782
print(eyes[isu % 5]+nose[isu % 4]+mouth[isu % 7])

#Cчет количества смайликов в предложенном тексте
text1 = 'Смайлики такие: X-{), =-('
text2 = 'Нам попались необычные смайлики: 8<{P, 8-P, 8<{|'
text3 = 'X-{), X-{), X-{), X-{), X-{), X-{)'
text4 = ':-(, ;<\, =-O'
text5 = 'Этот смайлик мне очень нравится =-{)'
res1 = len(re.findall(r'X-{\)', text1))
print ("Количество вхождений смайлика - " + str(res1) +' в тексте: '+ text1)
res2 = len(re.findall(r'X-{\)', text2))
print ("Количество вхождений смайлика - " + str(res2) +' в тексте: '+ text2)
res3 = len(re.findall(r'X-{\)', text3))
print ("Количество вхождений смайлика - " + str(res3) +' в тексте: '+ text3)
res4 = len(re.findall('X-{\)', text4))
print ("Количество вхождений смайлика - " + str(res4) +' в тексте: '+ text4)
res5 = len(re.findall('X-{\)', text5))
print ("Количество вхождений смайлика - " + str(res5) +' в тексте: '+ text5)

#Дополнительное задание 1
print(f"Вариант: {isu % 6}")
text = 'А ты знал, что ВТ - лучшая кафедра в ИТМО?'
textres = re.finditer(r"ВТ[\s\-]+(\w+\s){,4}ИТМО",text)
for textres in textres:
    print(textres[0])

#Дополнительное задание 2
print(f"Вариант: {isu % 4}")
def f(x):
    return 3*x**2+5
v1 = '20+22=42'
a = re.search(r".*(?=\+)",v1)
b = re.search(r"(?<=\+).*(?=\=)",v1)
s = re.search(r"(?<=\=).*",v1)
print(v1)
print(str(f(int(a[0])))+ "+" + str(f(int(b[0]))) + "=" + str(f(int(s[0]))))
print()
v1 = '1+3=4'    
a = re.search(r".*(?=\+)",v1)
b = re.search(r"(?<=\+).*(?=\=)",v1)
s = re.search(r"(?<=\=).*",v1)
print(v1)
print(str(f(int(a[0])))+ "+" + str(f(int(b[0]))) + "=" + str(f(int(s[0]))))
print()
v1 = '2+7=9'
a = re.search(r".*(?=\+)",v1)
b = re.search(r"(?<=\+).*(?=\=)",v1)
s = re.search(r"(?<=\=).*",v1)
print(v1)
print(str(f(int(a[0])))+ "+" + str(f(int(b[0]))) + "=" + str(f(int(s[0]))))
print()
v1 = '40+36=76'
a = re.search(r".*(?=\+)",v1)
b = re.search(r"(?<=\+).*(?=\=)",v1)
s = re.search(r"(?<=\=).*",v1)
print(v1)
print(str(f(int(a[0])))+ "+" + str(f(int(b[0]))) + "=" + str(f(int(s[0]))))
print()
v1 = '100+3=103'
a = re.search(r".*(?=\+)",v1)
b = re.search(r"(?<=\+).*(?=\=)",v1)
s = re.search(r"(?<=\=).*",v1)
print(v1)
print(str(f(int(a[0])))+ "+" + str(f(int(b[0]))) + "=" + str(f(int(s[0]))))






