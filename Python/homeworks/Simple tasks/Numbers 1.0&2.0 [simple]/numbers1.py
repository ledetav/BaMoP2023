from typing import List
import random

def magic(seq: List[int], x: int) -> bool:
    # Calculate the sum of the sequence numbers
    seq_sum = sum(seq)
    
    # Check if the sum can be divided by X without remainder
    if seq_sum % x == 0:
        return True
    else:
        return False
    
# Generate a random sequence of numbers
seq = [random.randint(0, 9999) for _ in range(random.randint(5, 100))]
print("Your sequence of numbers: ", seq)

# Set the value of X
X = int(input("Enter X: "))

# Call the magic() function to check if the sum of the sequence numbers can be divided by X without remainder
result = magic(seq, X)

# Print the result
print("Result:", magic(seq, X))