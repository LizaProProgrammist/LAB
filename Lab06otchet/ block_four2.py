n = int(input("������� ���������� ��������� �������: "))

arr = []
for i in range(n):
    element = float(input(f"������� ������� {i + 1}: "))
    arr.append(element)

average = sum(arr) / n

for i in range(n):
    if arr[i] == 0:
        arr[i] = average

print("������ ����� ������ ������� ���������:", arr)
