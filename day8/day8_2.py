import math

# Fent servir lcm amb alguna pista de Reddit, la meva primera implementacio al fer servir bruteforce era massa lenta tot i funcionar.

# Els nodes de A a Z segueixen tots un patro, la idea es trobar el numero de pasos per cada node que acaba amb A fins 
# a trobar un node que acabi amb Z i fer el mcm de tots els pasos

class Direction: 
    def __init__(self, location, left, right): 
        self.location = location
        self.left = left
        self.right = right
    
    def get_right(self): 
        return self.right
    
    def get_left(self):
        return self.left

def create_network(document):
    map = {}
    for line in document: # Per cada línia
        parts = line.strip().split(" = ") # Separem la línia en dos parts, la ubiccio i les connexions
        if len(parts) == 2:
            location, connections = parts
            left, right = connections.strip("()").split(", ")
            map[location] = Direction(location, left, right) # Creem la Direction amb la ubicació, la connexió esquerra i la connexió dreta
    return map

def path_length_to_Z(start_location, instructions, map):
    current_location = start_location
    steps = 0
    while not current_location.endswith("Z"):
        direction = instructions[steps % len(instructions)]
        current_node = map[current_location]
        current_location = current_node.get_left() if direction == "L" else current_node.get_right()
        steps += 1
    return steps

def find_starting_locations(map): 
    current_locations = []
    for location in map: # Per totes les ubicacions
        if location[-1] == "A": # Si acaben amb A
            current_locations.append(location) # Les afegim a la llista d'ubicacions actuals
    return current_locations

with open("day8/input.txt", "r") as file:
    document = file.readlines()

map = create_network(document[1:])
instructions = document[0].strip()
starting_locations = find_starting_locations(map)
path_lengths = [path_length_to_Z(location, instructions, map) for location in starting_locations]

total_steps = math.lcm(*path_lengths)
        
print(total_steps)