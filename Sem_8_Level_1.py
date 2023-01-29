# Вычислить значение выражения

# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

n = '12 + 15'
m = n.split()

def calc(a, b, ch):

    if ch == '+': return a + b
    elif ch == '-': return a - b
    elif ch == '/': return a / b
    elif ch == '*': return a * b

result = int(m[0])

for i in range(1, len(m) - 1, 2):
    result = calc(result, int(m[i + 1]), m[i])
print(result)