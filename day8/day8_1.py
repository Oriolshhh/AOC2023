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

with open("day8/input.txt", "r") as file:
    document = file.readlines()

instructions = document[0].strip()  # Agafem les instruccions
map = create_network(document[1:])  # Agafem la resta de línies per crear el mapa a partir de la linia 2

intstructions = document[0].strip()
current_location = "AAA" # Comencem a AAA
steps = 0
while current_location != "ZZZ":  # Mentre no arribem a ZZZ
    direction = instructions[steps % len(instructions)] # Fem el mòdul perquè si ens passem de la llargada de les instruccions, tornem a començar
    current_node = map[current_location]
    if direction == "L": # Si la direcció és L, anem a l'esquerra
        current_location = current_node.get_left() 
    elif direction == "R": # Si la direcció és R, anem a la dreta
        current_location = current_node.get_right()
    steps += 1

print(steps) 