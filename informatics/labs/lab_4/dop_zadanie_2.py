import re
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
    stroka = re.sub(r'",','"',stroka) #замена replace
    stroka = re.sub(r'"','',stroka)
  n = 0
  if re.findall('\{', stroka):
    stroka = stroka.split()
    count = len(stroka)
    for x in range(count):
      arr.append(stroka[x])
  elif re.findall('\[', stroka):
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
  if (count == 1) and (re.findall('\w+',arr[i])):
    print(arr[i])
  if (count == 2) and (re.findall('^[^f]\w+',arr[i])):
    print('  ', arr[i])
  if (count == 2) and (re.findall('^f',arr[i])):
    print('   -',arr[i])
  if (count == 3) and (re.findall('\w+',arr[i])):
    print('      ',arr[i])
  if (count == 4) and (re.findall('^s',arr[i])):
    print('   -',arr[i])
  if (count == 5) and (re.findall('\w+',arr[i])):
    print('      ',arr[i])

print(f'Прошло {time.perf_counter() - start_time}')



      




     

