string = input("Enter string (max 800 simbols): ")

if len(string) > 800:
    print("Max lenght is 800 simbols!")
    exit()

words = string.split()
print("Quantity of words: kjhfiea8uief", len(words))