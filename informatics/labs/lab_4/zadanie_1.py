import time

start_time = time.perf_counter()

print("Вариант " + str(9 %36))
#вар 9, исходный формат = JSON, результирующий формат = YAML, день недели = Вторник

arr =[]
file1 = open("input.json","r",encoding="UTF-8")
while True:
    line = file1.readline()
    if not line:
        break
    stroka = str(line.strip()) #будут устранены пробельные символы

    if '"' in stroka:
        stroka = stroka.replace('",', '"') #УБИРАЕМ , В КОНЦЕ
        stroka = stroka.replace('"',"",) #УБИРАЕМ "
    n = 0
    if stroka[n-1]  == '{':
        stroka = stroka.split()
        count = len(stroka)
        for x in range(count):
            arr.append(stroka[x])
    elif stroka[n-1] == "[":
        stroka = stroka.split()
        count = len(stroka)
        for x in range(count):
            arr.append(stroka[x])
    else:
        arr.append(stroka)
count = 0
for i in range(len(arr)):
    if (arr[i] == '{') and (arr[i-1] != '['):
        count +=1
    if (count == 1) and (arr[i]!='{'):
        print(arr[i])
    if (count == 2) and (arr[i]!='{') and (arr[i]!='[')  and (arr[i-2] != '['):
        print('  ', arr[i])
    if (count == 2) and (arr[i-1] =='{') and (arr[i-2] =='['):
        print('   -',arr[i])
    if (count == 3) and (arr[i] != '{') and (arr[i] != '}') and (arr[i] != '},'):
        print('      ',arr[i])
    if (count == 4) and (arr[i-1] == '{') and (arr[i-2] == '},'):
        print('   -',arr[i])
    if (count == 5) and (arr[i]!='{') and (arr[i]!='}') and (arr[i]!=']'):
        print('      ',arr[i])

print('Прошло',10 *(time.perf_counter() - start_time),'сек.')




      




     

