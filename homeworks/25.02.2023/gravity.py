import math

G = 6.6743 * math.pow(10, -11) # gravitational constant
m1 = 5.9737 * math.pow(10, 24) # earth mass in kg

def gravity_force(m1, m2, distance):
    force = (G*m1*m2)/math.pow(distance, 2)
    
    return force

#get user input
m2 = float(input("Enter mass of the second planet in kilograms (without degree): "))
m2_degree = int(input("Enter degree for mass of the second planet: "))
m2 = m2 * math.pow(10, m2_degree)

distance = float(input("Enter distance to the planet in kilometers (without degree): "))
distance_degree = int(input("Enter degree for distance to the planet: "))
distance = distance*  math.pow(10, distance_degree)
distance = distance * 1000 # convert km to meters

#calculate and print force of gravity
force = gravity_force(m1, m2, distance)
print("The force of gravity is ", "{:.3e}".format(force), "N.")
