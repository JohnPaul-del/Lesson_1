res = []
buf = 0
summ = 0
summ2 = 0
summ3 = 0

for i in range(1, 1000, 2):
    buf = str(i ** 3)
    char: str
    for char in buf:
        summ += int(char)
        if summ % 7 == 0:
            summ2 = str(summ + 17)
            for char in summ2:
                summ3 += int(char)
                if summ3 % 7 == 0:
                    res.append(summ3)

print(res)
