# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')


# prime - функция проверки числа на простоту
def prime(number):
    # Проверим число на простоту
    for i in range(2, number):
        if not number % i:
            return False

    return True


primes = []  # primes - список простых чисел
not_primes = []  # not_primes - список составных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers - список чисел

# Отсортируем числа
for i in range(len(numbers)):
    if i > 0:
        is_prime = prime(numbers[i])
        primes.append(numbers[i]) \
            if is_prime \
            else not_primes.append(numbers[i])

# Выведем списки чисел
print('\nСПИСКИ ЧИСЕЛ')
print('\nСписок простых чисел:', primes, end='.\n')
print('Список составных чисел:', not_primes, end='.\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
