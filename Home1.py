'''Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.'''

a = float(input('введите число ')) # создал переменную с типом данных float и вложил в неё функцию инпут для ввода числа с консоли
d = input('введите точность числа') # создал переменную и вложил в неё функцию инпут для ввода точности числа
# listt = {'',''}
# listt = d.split('.')  
print(round(a,len(d.split('.')[1]))) # использовал функцию принт для вывода данных и вложил в неё функцию роунд а в качестве аргументов функции
# положил переменную а, для использовал функцию лен и в качестве аргументов этой функции вложил функцию сплит, которая будет разделять число по
# признаку точки и и вызываем элемент с индексом 1, т.е. строку после запятой
