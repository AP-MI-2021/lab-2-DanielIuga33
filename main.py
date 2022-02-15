# Problema 1

def IsPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def get_largest_prime_below(n):
    for i in range(n - 1, 1, -1):
        if IsPrime(i):
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(12) == 11
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(8) == 7


# Problema 5
def is_palindrome(n):
    cn = n
    inv = 0
    while cn > 0:
        inv = inv * 10 + cn % 10
        cn = cn // 10
    if inv == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(122) is False
    assert is_palindrome(22) is True
    assert is_palindrome(10) is False


# Problema 11
def get_leap_years(start: int, end: int):
    lista = []
    while start <= end:
        if start % 4 == 0:
            lista.append(start)
        start += 1
    return lista

def test_get_leap_yars():
    assert get_leap_years(2000, 2002) == [2000]
    assert get_leap_years(2002, 2008) == [2004, 2008]
    assert get_leap_years(1996, 2000) == [1996, 2000]


def runMenu():
    while True:
        print('1. Problema 1')
        print('2. Problema 5')
        print('3. Problema 11')
        print('x. Iesire')

        optiune = input('Dati optiunea: ')
        if optiune == '1':
            n = int(input("n= "))
            print(get_largest_prime_below(n))
        elif optiune == '2':
            n = int(input("n= "))
            print(is_palindrome(n))
        elif optiune == '3':
            start = int(input("start= "))
            end = int(input("end= "))
            print(get_leap_years(start, end))
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita, te rog reincearca !')


def main():
    test_get_largest_prime_below()
    test_is_palindrome()
    test_get_leap_yars()

    runMenu()


main()
