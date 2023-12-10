def is_prime(n: int) -> bool:
    '''Простое или нет'''
    if (n != 2) and (n % 2 == 0):
        return False
    for delitel in range(2, n, 2):
        if n % delitel == 0:
            return False
    return True


def prime_numbers(n: int):
    for i in range(1, n+1):
        if is_prime(i):
            yield i
for p_number in prime_numbers(100):
    print(p_number)



print(*prime_numbers(100), sep='\n')