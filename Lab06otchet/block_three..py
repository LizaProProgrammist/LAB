
text = input("Введите строку: ")

n = len(text)
half_n = n // 2
result = ""
for i in range(n):
    if i < half_n and text[i] == "п":
        result += "*"
    else:
        result += text[i]

print("Преобразованная строка:", result)
