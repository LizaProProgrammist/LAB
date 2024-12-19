def find_max_index(arr, n, max_index=0):
    if n == 0: 
        return max_index
    if arr[n - 1] > arr[max_index]:  
        max_index = n - 1
    return find_max_index(arr, n - 1, max_index)

n = int(input("¬ведите количество элементов массива: "))
arr = []
for i in range(n):
    element = int(input(f"¬ведите элемент {i + 1}: "))
    arr.append(element)

max_index = find_max_index(arr, n)
print(f"»ндекс максимального элемента: {max_index} (значение: {arr[max_index]})")

