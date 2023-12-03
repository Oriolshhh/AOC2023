with open("day2/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

idsum = 0
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

for line in document:
    parts = line.split(": ") # Separem la línia en dos parts, el game_id i les extraccions
    game_id = int(parts[0].split(" ")[1])
    extractions = parts[1].split("; ") # Separem les extraccions en una llista es separen per ;

    possible = True
    for extraction in extractions:  # Iterem per cada extracció
        counts = {'red': 0, 'green': 0, 'blue': 0} # Inicialitzem el hasmap de colors
        for color in counts.keys(): # Iterem per cada color
            for segment in extraction.split(", "): # Iterem per cada segment de la extracció (color)
                if color in segment: # Si el color es troba
                    count = int(segment.split(" ")[0]) # Obtenim el nombre de cubos
                    counts[color] = max(counts[color], count)  # Actualitzem el hashmap de colors

        #Comprovem si es possible
        for color, count in counts.items():
            if count > max_cubes[color]:
                possible = False
                break

        if not possible:
            break

    if possible:
        idsum += game_id

print(idsum)