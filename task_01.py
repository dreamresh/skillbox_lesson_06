print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.

# просим степень
degree = int(input('Введите степень числа: ')) # degree = 3
# просим число
numbers = int(input('Введите число, до которого необходимо вывести результаты возведения в ' + str(degree) + ' степень: '))
# считаем числа по порядку
numbers_count = 0
# числов в степени
numbers_degree = 0

while numbers_count <= numbers: # порядок чисел
    numbers_degree = numbers_count ** degree

    if degree == 0 or numbers_count == 0:
        numbers_degree = 1
    print('Число "' + str(numbers_count) + '", возведённое в степень "' + str(degree) + '", будет "' + str(numbers_degree) + '".')
    numbers_count += 1