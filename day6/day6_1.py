with open("day6/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

for line in document:
    if line.startswith("Time:"):
        times = line.split()[1:] # Obtenim els temps com a llista
    elif line.startswith("Distance:"):
        distances = line.split()[1:] # Obtenim les distàncies com a llista

result = 1  # Inicialitzem a 1 per poder multiplicar
for i in range(len(times)):
    time = int(times[i])
    record = int(distances[i])

    runDistances = [0] * time  # Inicialitzem runDistances a 0

    for j in range(time): # Calculem la distància per a cada possible temps que el boto esta premut
        runDistances[j] = j * (time - j)

    counter = 0
    for distance in runDistances: # Comparem cada distanca amb el record
        if distance > record:
            counter += 1

    result *= counter if counter > 0 else 1

print(result)