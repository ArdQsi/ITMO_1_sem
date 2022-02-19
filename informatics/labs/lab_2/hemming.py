kod = list(map(int,input()))
print("Ввели строку: ", kod)
if len(kod) != 7:
    print("Неправильная запись!!!")
else: 
    S1 = kod[0] ^ kod[2] ^ kod[4] ^ kod[6]
    S2 = kod[1] ^ kod[2] ^ kod[5] ^ kod[6]
    S3 = kod[3] ^ kod[4] ^ kod[5] ^ kod[6]
ind = (S1+S2*2+S3*4)-1
if (kod[ind]) and (ind >=0) == 1:
    kod[ind] = 0
else:
    kod[ind] = 1
print("Правильный вывод: ", kod)
