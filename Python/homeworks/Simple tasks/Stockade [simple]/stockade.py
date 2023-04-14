def alternate_case(text):
    result = ''
    capitalize = True
    for char in text:
        if char.isalpha():
            if capitalize:
                result += char.lower()
            else:
                result += char.upper()
            capitalize = not capitalize
        else:
            result += char
    return result

string = str(input("Enter new atring: "))
print("Stockade string:", alternate_case(string))