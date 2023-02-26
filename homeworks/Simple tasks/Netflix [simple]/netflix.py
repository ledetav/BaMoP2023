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
                return print(f"{people[i][0]} and {people[j][0]} should buy the Netflix subscription.")
    return print("No one can buy the subscription")

X = int(input("Enter amount of money for Alice: "))
Y = int(input("Enter amount of money for Bob: "))
Z = int(input("Enter amount of money for Charlie: "))
COST = int(input("Enter the cost of the subscription: "))

buy_netflix(X, Y, Z, COST)