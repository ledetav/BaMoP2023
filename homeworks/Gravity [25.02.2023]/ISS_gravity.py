import requests
import math

# Get current position of the ISS
iss_location_response = requests.get('http://api.open-notify.org/iss-now.json')
iss_location_data = iss_location_response.json()
iss_latitude = float(iss_location_data['iss_position']['latitude'])
iss_longitude = float(iss_location_data['iss_position']['longitude'])

# Calculate distance between the ISS and the center of the Earth
earth_radius = 6371 # in km
iss_altitude = 408 # in km
distance = earth_radius + iss_altitude
latitude_radians = math.radians(iss_latitude)
longitude_radians = math.radians(iss_longitude)
x = distance * math.cos(latitude_radians) * math.cos(longitude_radians)
y = distance * math.cos(latitude_radians) * math.sin(longitude_radians)
z = distance * math.sin(latitude_radians)
earth_iss_distance = math.sqrt(x**2 + y**2 + z**2) * 1000 # convert to meters

# Calculate gravitational force between the Earth and the ISS
G = 6.6743 * math.pow(10, -11) # gravitational constant
earth_mass = 5.9722 * math.pow(10, 24) # in kg
iss_mass = 420000 # in kg
gravitational_force = (G * earth_mass * iss_mass) / (earth_iss_distance**2)

# Print the result
print('The gravitational force between the Earth and the ISS at noon today is: {:.2f} N.'.format(gravitational_force))