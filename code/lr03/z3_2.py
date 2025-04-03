from lr00.z9_2 import Rem_new as Power


def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def phi(a):
    result = []
    for i in range(1, a+1):
        if gcd(a, i) == 1:
            result.append(i)
    return len(result)


def inverse(a, m):
    x = "no"
    if gcd(a, m) == 1:
        x = (a ** (phi(m)-1)) % m
    return x


def test():
    for i in range(2, 30):
        # print(phi(i), "|", i)
        print(i, 5, "|", inverse(i, 5))


test()
