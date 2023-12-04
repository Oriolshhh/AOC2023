def isSymbol(char):
    return not char.isdigit() and char != '.'

def checkForSymbols(x, y, length):
    # Mirem dreta i esquerra del numero
    if y > 0 and isSymbol(grid[x][y - 1]) or y + length < len(grid[x]) and isSymbol(grid[x][y + length]):
        return True

    # Mirem dalt, baix i en diagonal del numero
    for i in range(max(y - 1, 0), min(y + length + 1, len(grid[x]))):
        if x > 0 and isSymbol(grid[x - 1][i]):
            return True
        if x < len(grid) - 1 and isSymbol(grid[x + 1][i]):
            return True

    return False

with open("day3/input", "r") as file:
    document = file.readlines()
 
grid = [list(line.strip()) for line in document] # Creem la matriu
part_numbers = []

for x in range(len(grid)): # Per cada fila
    y = 0
    while y < len(grid[x]): # Per cada columna
        if grid[x][y].isdigit(): # Si es un numero
            start = y
            while y < len(grid[x]) and grid[x][y].isdigit(): # Mentre sigui un numero
                y += 1
            num_length = y - start
            if checkForSymbols(x, start, num_length): # Si hi ha simbols al voltant
                part_numbers.append(int(''.join(grid[x][start:y]))) # Afegim el numero a la llista
        else:
            y += 1 # Si no es un numero, avancem

total_sum = sum(part_numbers) # Sumem tots els numeros de la llista
print(total_sum)