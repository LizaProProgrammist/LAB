n = int(input("������� ���������� ��������� �������: "))

arr = []
for i in range(n):
    element = int(input(f"������� ������� {i + 1}: "))
    arr.append(element)

max_element = max(arr)

print("������������ ������� �������:", max_element)
print("������ � �������� �������:", arr[::-1])
