text = input("Введите текст: ")
words = text.split()

if len(words) < 5:
    print("Текст должен содержать не менее 5 слов")
else:
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    most_common = max(freq, key=freq.get)

    longest = max(words, key=len)

    print(most_common, longest)