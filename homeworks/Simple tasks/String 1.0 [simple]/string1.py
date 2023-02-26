def search_substr(substr, st):
    if substr.lower() in st.lower():
        return print("There is a contact!")
    else:
        return print("By!")
    
substr = str(input("Enter a substring: "))
st = str(input("Enter a string: "))

search_substr(substr, st)
