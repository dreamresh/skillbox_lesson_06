print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

print('без цикла')
ticket = int(input('Введите номерок билетика: '))
if (ticket // 100000) + ((ticket // 10000) % 10) + ((ticket // 1000) % 10) == \
    ((ticket // 100) % 10) + ((ticket // 10) % 10) + ((ticket // 1) % 10):
    print('Билетик счастливенький - приятного аппетита!')
else:
    print('Билет простой, можно его не кушать.')

print('цикл`s')
number_tiket = int(input('Введите номер билета: '))
count_number_digit = 0 # считает количество цифр
count_number = 0 # считает количество цифр для сравнения
left_number = 0
rich_number = 0
number_tiket_count = number_tiket # для проверки на чётность
while number_tiket_count !=0:
    count_number_digit += 1
    # print('Кол-во цифр:', count_number_digit)
    number_tiket_count //= 10
if count_number_digit % 2:
    print('Количество цифр нечётное...')
else:
    print('Количество цифр чётное.')
    count_number_half = count_number_digit / 2
    while count_number != count_number_digit:
        count_number += 1
        ticket = number_tiket % 10
        number_tiket //= 10
        if count_number_half >= count_number:
            rich_number += ticket
        else:
            left_number += ticket
    if left_number == rich_number:
        print('Билетик счастливенький - приятного аппетита!')
    else:
        print('Билет простой, можно его не кушать.')