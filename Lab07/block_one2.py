with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

longest_words = []
for line in lines:
    words = line.split()
    if words:
        longest_word = max(words, key=len)
        longest_words.append(longest_word)
    else:
        longest_words.append("")  

with open("output.txt", "w", encoding="utf-8") as outfile:
    for word in longest_words:
        outfile.write(word + "\n")

print("Самые длинные слова записаны в файл output.txt.")

