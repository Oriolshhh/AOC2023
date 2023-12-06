with open("day6/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

for line in document:
    if line.startswith("Time:"):
        time = "".join(line.split()[1:]) # Unim els temps en un sol string
    elif line.startswith("Distance:"):
        distance = "".join(line.split()[1:]) # Unim les distàncies en un sol string

result = 1  # Inicialitzem a 1 per poder multiplicar
counter = 0
for i in range(int(time)):
    runDistance = i * (int(time) - i) # Calculem la distància per a cada possible temps que el boto esta premut

    if runDistance > int(distance): # Comparem cada distanca amb el record
        counter += 1

result *= counter if counter > 0 else 1

print(result)
