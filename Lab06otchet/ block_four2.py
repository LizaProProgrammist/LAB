n = int(input("Введите количество элементов массива: "))

arr = []
for i in range(n):
    element = float(input(f"Введите элемент {i + 1}: "))
    arr.append(element)

average = sum(arr) / n

for i in range(n):
    if arr[i] == 0:
        arr[i] = average

print("Массив после замены нулевых элементов:", arr)
