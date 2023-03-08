def sum_numbers(start: int, end: int) -> int:
    total = sum(range(start, end + 1))
    
    return total

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

if start > end:
    start, end = end, start

total_sum = sum_numbers(start, end)
print(f"The sum of integers from {start} to {end} is {total_sum}")