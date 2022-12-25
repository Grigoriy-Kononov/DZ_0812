# Дан список интов,повторяющихся элементов в списке нет.
# Нужно преобразовать этомножество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
#  Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4" 

a = sorted(set([1,4,2,5,3,9,8,11,0]))
print(a)
count = 0
b = []
[0, 1, 2, 3, 4, 5, 8, 9, 11, 14]
for i in range(1,len(a)):
    if a[i] == a[i-1]+1:
        count +=1
    else:
        if count == 0:
            b.append((str(a[i-1]) + ', '))
        else:
            b.append((str(a[i-1-count]) + ' -'))
            b.append(str(a[i-1]) + ', ')
            count = 0
    if i == len(a)-1:
        if count == 0:
            b.append(str(a[i]))
        else:
            b.append(str(a[i-count]) + ' -')
            b.append(str(a[i]))
print('"'," ".join(b),'"')


# Дана строка (возможно, пустая), состоящая из букв A-Z: 
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB 
# Нужно написать функцию RLE, которая на выходе даст строку вида: 
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка. 
# Пояснения: Если символ встречается 1 раз, он остается без изменений; 
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.


def rle_code(data):
    coding = ''
    prev_char = ''
    count = 1
    if not data: return 'EROR'
    for char in data:
        if char != prev_char:
            if prev_char:
                if count == 1:
                    coding += prev_char
                else:
                    coding += prev_char + str(count)
            count = 1
            prev_char = char
        else:
                count += 1
    else:
        coding += prev_char + str(count)
        return coding

f = open('D:\УЧЕБА\PYTON\DZ\DZ_0812\dfile.txt', 'r+')
g = open('D:\УЧЕБА\PYTON\DZ\DZ_0812\dresult.txt', 'r+')

g.write(rle_code(f.read()))

f.close()
g.close()