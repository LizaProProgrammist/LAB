
text = input("������� ������: ")

n = len(text)
half_n = n // 2
result = ""
for i in range(n):
    if i < half_n and text[i] == "�":
        result += "*"
    else:
        result += text[i]

print("��������������� ������:", result)
