print("Введите число n:")
n = int(input())

ar = list()
i = 0

while i <= n:
    if i < n / 2:
        ar.append(i * 2)
        i = i + 1
    else:
        break

print(ar)
