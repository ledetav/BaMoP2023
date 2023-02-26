# Get input from user
X = float(input("Enter Jerry's speed (m/s): "))
Y = float(input("Enter Tom's speed (m/s): "))
S = float(input("Enter initial distance between them (m): "))

# Calculate time it takes for Tom to catch Jerry
if Y <= X:
    print("Tom cannot catch Jerry!")
else:
    time_to_catch = S / (Y - X)
    print(f"Tom can catch Jerry in {time_to_catch:.2f} seconds.")