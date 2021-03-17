# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array


# Print out type of np_baseball
print(type(np_baseball))

import requests
request=requests.get(http://api.open-notify.org/astros.json)
data= request.json()

for p in data['people']:
    print(p['craft'])











