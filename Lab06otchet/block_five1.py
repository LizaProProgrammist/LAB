def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("¬ведите натуральное число n (больше 2): "))

print(f"ѕары простых чисел-близнецов на отрезке [{n}, {2 * n}]:")
for x in range(n, 2 * n - 1):
    if is_prime(x) and is_prime(x + 2):
        print(f"({x}, {x + 2})")

