#82 Десятичное число в двоичной системе
result = str('')  #инициализирую переменную пустой строкой
q=int(input('Введите число, которое нужно преобразовать: '))  #прошу пользователя ввести число в 10-ой системе счисленич
while q!= 0:   #Ставлю цикл работы, пока введённое число не станет равно 0
    result = str(q%2) + result #присваиваю переменной остаток от деления , преобразую её в строку и запихиваю в начало перемнной
    q = q // 2 #целочисленно делю моё число и присваиваю это число переменной q
print('Значение в двоичной системе счисления = ', result)

#79 Наибольший общий делитель
pozitive1 = int(input('\nВведите первое положительное число: '))  #Прошу пользователя ввести первое число
pozitive2 = int(input('Введите второе положительное число: '))    #прошу пользователя ввести второе число
if pozitive1>pozitive2 :          #нахожу наименьшее из меньших введённых чисел и присваиваю меньшее переменной d
    d = pozitive2
else:
    d = pozitive1
while pozitive1 % d !=0 and pozitive2 % d !=0:   #Ставлю цикл работы, пока мои два числа делятся без остатка на их наименьшее число
    d = d-1  #Отнимаю единицу у наименьшего числа
print('Наибольший общий делитель = ', d) #вывожу перемнную d

#80Простые множители
n = int(input('\nВведите целое число (2 или больше): ')) #Прошу ввести чсило большее 2
factor = 2    #инициализирую переменную значением 2
print('Простые множители числа', n, ': ')
if n>=2 :       #Проверяю введённое число (оно больше или меньше 2)
    while factor<=2: #ставлю цикл работы, пока значение моей переменной меньше или равно введённому числу
        if n%factor==0 : #условие: если число делится без остатка, то...
            n//=factor  #делю введённое число на свою переменную
            print(factor)
        else:
            factor = factor+1  #если не выполняется прошлое условие, то добавляю к своей переменной 1
            print(factor)
else:
    print('ОШИБКА!!!! Вы ввели неверное число!!!')


#83 Максимальное число в последовательности
for i in range(1, 101)   #генерируется случайное число из диапазона о 1до 100
    maximal = i  #сохраняю это значение как максимальное
for 99 in range(1,101)
