import random

def eqv(a: float, b: float) -> bool:
    # Calculate the sum of a and b
    sum_ab = a + b
    
    # Calculate the accuracy of eps
    eps = 0.0001 * max(a, b)

    # Set the value of c
    c = sum_ab + random.uniform(0.0001, 0.9999)
    
    # Check if the absolute difference between sum_ab and c is less than or equal to eps
    if abs(sum_ab - c) <= eps:
        return True
    else:
        return False

# Generate two random fractional numbers greater than 1000 and less than 99999
a = random.uniform(1000, 99999)
print("This is number A: ", a)

b = random.uniform(1000, 99999)
print("This is number B: ", b)

# Print the result
print("Result: ", eqv(a, b))
