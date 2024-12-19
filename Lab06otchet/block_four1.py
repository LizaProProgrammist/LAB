n = int(input("Введите количество элементов массива: "))

arr = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    arr.append(element)

max_element = max(arr)

print("Максимальный элемент массива:", max_element)
print("Массив в обратном порядке:", arr[::-1])
