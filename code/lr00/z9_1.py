import re


def calc(a):
    x1 = (0.5 + 0.5 * pow((4 * a * a - 3), 0.5)) / a * (-1)
    x2 = (0.5 - 0.5 * pow((4 * a * a - 3), 0.5)) / a * (-1)
    x3 = 0.5 * ((1+pow((4 * a * a - 3), 0.5))/a)
    x4 = -0.5 * ((-1 + pow((4 * a * a - 3), 0.5)) / a)
    x = [x1, x2, x3, x4]
    result = re.sub("[^0-9]", '', str(min(x)))[:6]
    while len(result) < 6:
        result += '0'
    return result


b = []
for i in range(1, 235):
    b.append(calc(i))
c = 0
for i in range(len(b)):
    for j in range(i, len(b)):
        if (b[i] == b[j]) and i != j:
            c += 1


print(c)
print(len(b)/12)

for i in range(12):
    print(calc(i+1))