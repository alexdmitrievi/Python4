'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл 
многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

from random import randrange

k = int(input('введите натуральную степень '))
f = open('file.txt','w') 
a = []
a.append(randrange(1, 100))
for i in range(1,k+1):
    a.append(randrange(0, 100))
print(a)
for i in range(k + 1):
    if a[i] != 0:
        if k-i == 1:
            f.write(str(a[i]) + '*' + 'x' + ' + ' )
        elif k-i == 0:
            f.write(str(a[i]) + ' = 0' )
        else:
            f.write(str(a[i]) + '*' + 'x' + '^' +  str(k-i) + ' + ' )
        


