try:
    def Rem(n, m, b):
        if m == 0:
            result = 1
        elif m % 2 == 0:
            result = Rem((n * n) % b, m // 2, b)
        else:
            result = n * Rem((n * n) % b, (m - 1) // 2, b)
        # print(n, m, b, result)
        return result % b
except Exception as e:
    print("Base error:", e)


try:
    def Rem_new(n, m, b):
        m = str(dec_to_bin(m))[1:]
        result = n % b
        while len(m) > 0:
            result = (result * result) % b
            if m[0] == '1':
                result = (result * n) % b
            m = m[1:]
        return result
except Exception as e:
    print("New error:", e)


try:
    def dec_to_bin(n):
        if n == 0:
            return 0
        else:
            return n % 2 + 10 * dec_to_bin(n // 2)
except Exception as e:
    print("dec to bin error", e)


def straight(n, m, b):
    print('Check', pow(n, m) % b)


def test():
    x, y, z = int(input('n:')), int(input('m:')), int(input('b:'))
    print('Old: ', Rem(x, y, z))
    print('New: ', Rem_new(x, y, z))
    # straight(x, y, z)
