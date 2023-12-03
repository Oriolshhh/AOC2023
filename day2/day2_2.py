with open("day2/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

totalSum = 0
for line in document:
    parts = line.split(": ") # Separem la línia en dos parts, el game_id i les extraccions
    extractions = parts[1].split("; ") # Separem les extraccions en una llista es separen per ;

    counts = {'red': 0, 'green': 0, 'blue': 0} # Inicialitzem el hashmap de colors

    for extraction in extractions:  # Iterem per cada extracció
        for color in counts.keys(): # Iterem per cada color
            for segment in extraction.split(", "): # Iterem per cada segment de la extracció (color)
                if color in segment: # Si el color es troba
                    count = int(segment.split(" ")[0]) # Obtenim el nombre de cubos
                    counts[color] = max(counts[color], count)  # Actualitzem el hashmap de colors

        #Multipliquem els valors
    gamePower = 1
    for color, count in counts.items():
        gamePower *= max(count, 1)  # Evitem multiplicar per zero
        

    totalSum += gamePower

print(totalSum)