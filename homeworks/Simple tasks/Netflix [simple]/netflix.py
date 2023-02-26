def buy_netflix(X, Y, Z, COST):
    # Create a list of tuples containing the names and amounts of money for each person
    people = [('Alice', X), ('Bob', Y), ('Charlie', Z)]
    
    # Sort the list in descending order by amount of money
    people.sort(key=lambda x: x[1])
    
    # Iterate through every combination of two people
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            # Calculate the total amount of money of the two people
            total_money = people[i][1] + people[j][1]
            
            # If the total amount is greater than or equal to the cost, return the two names
            if total_money >= COST:
                return people[i][0], people[j][0]

X = int(input("Enter amount of money for Alice: "))
Y = int(input("Enter amount of money for Bob: "))
Z = int(input("Enter amount of money for Charlie: "))
COST = int(input("Enter the cost of the subscription: "))

names = buy_netflix(X, Y, Z, COST)
print(f"{names[0]} and {names[1]} should buy the Netflix subscription.")