def get_file_info():
    with open("day5/input", "r") as file:
        lines = file.read().splitlines()

    # Agafem les seeds
    seeds_index = next(i for i, line in enumerate(lines) if 'seeds:' in line)
    seeds = list(map(int, lines[seeds_index].split(":")[1].split()))

    # Agafem els mapes de conversió
    maps = []
    current_map = []
    for line in lines[seeds_index + 1:]: # Comencem a llegir després de la línia de les llavors
        if line == "": # Si trobem una línia buida, vol dir que hem acabat de llegir un map
            if current_map: # Si el map no està buit, l'afegim a la llista de mapes
                maps.append(current_map)
                current_map = [] # Reiniciem el map
        else: # Si no és una línia buida, afegim la línia al map
            current_map.append(line) 
    if current_map: # Si al final del fitxer no hi ha una línia buida, afegim el map a la llista de mapes
        maps.append(current_map)

    return seeds, maps 

def get_seeds(seeds, maps):
    for block in maps: # Per cada map
        ranges_list = [list(map(int, line.split())) for line in block[1:]] # Obtenim les els rangs de conversio

        new_seeds = [] # Creem una nova llista de llavors
        for seed in seeds: # Per cada llavor
            for destination, source, length in ranges_list: # Per cada rang de conversió
                if seed in range(source, source + length + 1): # Si la llavor es troba dins del rang
                    new_seeds.append(seed - source + destination) # Afegim la llavor convertida a la nova llista
                    break # Un cop hem trobat el rang, no cal seguir buscant
            else: # Si la llavor no es troba dins de cap rang, la llavor no es converteix
                new_seeds.append(seed) # Afegim la llavor a la nova llista

        seeds = new_seeds # Actualitzem la llista de llavors

    return seeds

seeds, maps = get_file_info() # Obtenim les seeds i els mapes de conversió
seeds = get_seeds(seeds, maps) # Obtenim les seeds actualitzades

print(min(seeds))
