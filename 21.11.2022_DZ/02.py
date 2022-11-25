# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("\033[H\033[J")

print(f'x\t y\t z\t ¬(X ⋁ Y ⋁ Z)\t ¬X ⋀ ¬Y ⋀ ¬Z\t Проверка')
for i in range(2):
    x = bool(i)
    i +=1
    for j in range(2):
        y = bool(j)
        j +=1
        for k in range(2):
            z = bool(k)
            k +=1
            expression_1 = bool(not(x and y and z))
            expression_2 = bool(not(x) or not(y) or not(z))
            if expression_1 == expression_2:
                comparison = bool(True)
            else:
                comparison = bool(False)
            print(f'{x}\t {y}\t {z}\t {expression_1}\t\t {expression_2}\t\t {comparison}')
