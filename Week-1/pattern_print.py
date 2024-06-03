# lower triangular
print("==========LOWER TRIANGULAR==========")
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()


# upper triangular
print("==========UPPER TRIANGULAR==========")
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()


# pyramid
print("==========PYRAMID==========")
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
