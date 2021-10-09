#Problema 1
def get_largest_prime_below(x):
    if(x<=1):
        return False
    if(x==2):
        return True
    if(x%2==0):
        return False
    i=3
    while(i*i<=x):
        if(x%i==0):
            return False
        i+=2
    return True
n=int(input("n="))
for i in range (n-1,1,-1):
    if (get_largest_prime_below(i)):
        print("numarul {} este prim".format(i))
        break
def test_get_largest_prime_below(x):
    n = int(input("n="))
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(10)==7
    assert get_largest_prime_below(8)==5
    m=test_get_largest_prime_below(n)
    print(m)
test_get_largest_prime_below()

#Problema 5
def is_palindrome(n):
    cn=n
    inv=0
    while cn>0:
        inv=inv*10+cn%10
        cn=cn//10
    ok=False
    if inv==n:
        ok=True
    if ok==True:
        print("da")
    else:
        print("nu")
def test_is_palindrome(n):
    assert is_palindrome(121) is True
    assert is_palindrome(122) is False
    assert is_palindrome(22) is True
    assert is_palindrome(10) is False
    n=int(input("n= "))
    m=is_palindrome(n)
    print(m)
test_is_palindrome()

#Problema 11
def get_leap_years(start: int, end: int):
    while start<=end:
        if start%4==0:
            print(start)
        start+=1
def test_get_leap_yars(start:int,end: int)
    assert test_get_leap_yars(2000,2002)==2000
    assert test_get_leap_yars(2002,2008)==2004 2008
    assert test_get_largest_prime_below(1996,2000)==1996 2000
    start=int(input("start="))
    end=int(input("end="))
    m=get_leap_years(start,end)
    print(m)
main()