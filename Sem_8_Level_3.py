# Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3

n = '12 - 4 * 2 + 6 / 3'
m = n.split()
m2 = []

if m[0].isdigit():
    m.insert(0, '+')

result = 0

for i in range(0, len(m) - 1, 2):
    if m[i] == '*':
        multyply = int(m2[-1]) * int(m[i + 1])
        m2[-1] = multyply
    elif m[i] == '/':
        division = int(m2[-1]) / int(m[i + 1])
        m2[-1] = division
    else:
        m2.append(m[i])
        m2.append(m[i + 1])

for i in range(0, len(m2) -1, 2):
    if m2[i] == '+':
        result += int(m2[i+1])
    elif m[i] == '-':
        result -= int(m2[i+1])
    else:
        continue
print(f'{n} = {result}')
