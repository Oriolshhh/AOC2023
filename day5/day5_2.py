def get_file_info():
    with open("day5/input", "r") as file:
        lines = file.read().splitlines()

    # Agafem les seeds com a intervals
    seeds_index = next(i for i, line in enumerate(lines) if 'seeds:' in line)
    seed_inputs = list(map(int, lines[seeds_index].split(":")[1].split()))

    seeds = []
    for i in range(0, len(seed_inputs), 2):
        seeds.append([seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]])

    # Agafem els mapes de conversió
    maps = []
    current_map = []
    for line in lines[seeds_index + 1:]:
        if line == "":
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)
    if current_map:
        maps.append(current_map)

    return seeds, maps 

def get_seeds(seeds, maps):
    for block in maps: # Per cada map
        ranges_list = [list(map(int, line.split())) for line in block[1:]] # Obtenim les els rangs de conversio

        new_seeds = []
        while seeds:
            start, end = seeds.pop(0) # Agafem la primera llavor de la llista

            for destination, source, length in ranges_list: # Per cada rang de conversió
                overlap_start = max(start, source) # Calculem l'inici i el final de la llavor convertida
                overlap_end = min(end, source + length) # Si la llavor no es converteix, l'inici i el final seran iguals
 
                if overlap_start < overlap_end: # Si la llavor es converteix
                    new_seeds.append([overlap_start - source + destination, overlap_end - source + destination]) # Afegim la llavor convertida a la nova llista
                    if overlap_start > start: # Si la llavor no es converteix per l'esquerra, afegim la part esquerra de la llavor original a la nova llista
                        seeds.append([start, overlap_start])
                    if overlap_end < end: # Si la llavor no es converteix per la dreta, afegim la part dreta de la llavor original a la nova llista
                        seeds.append([overlap_end, end])
                    break
            else:
                new_seeds.append([start, end]) # Si la llavor no es converteix, la afegim a la nova llista

        seeds = new_seeds # Actualitzem la llista de llavors

    return seeds

seeds, maps = get_file_info()
seeds = get_seeds(seeds, maps)

# Trobem el valor mínim de l'interval que conté el valor mínim de totes les llavors
min_seed_value = float('inf')  # Inicialitzem amb infinit
for interval in seeds:
    if interval[0] < min_seed_value:
        min_seed_value = interval[0]

print(min_seed_value)