# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')


# prime - the function of checking the number for simplicity
def prime(number):
    # Let's check the number for simplicity
    for i in range(2, number):
        if not number % i:
            return False

    return True


primes = []  # primes - list of prime numbers
not_primes = []  # not_primes - list of composite numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers - list of numbers

# Let's sort the numbers
for i in range(len(numbers)):
    if i > 0:
        is_prime = prime(numbers[i])
        primes.append(numbers[i]) \
            if is_prime \
            else not_primes.append(numbers[i])

# Let's output lists of numbers
print('\nLISTS OF NUMBERS')
print('\nList of prime numbers:', primes, end='.\n')
print('List of composite numbers:', not_primes, end='.\n\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
