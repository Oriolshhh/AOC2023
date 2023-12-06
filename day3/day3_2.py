def number_from_digits(digits: list[str]):
    return int(''.join(digits))

with open("day3/input", "r") as file:
    document = file.readlines()

grid = [list(line.strip()) for line in document] # Creem la matriu

# Ceem hashmap per emmagatzemar gear ratios
gear_ratio_candidates = {}

directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]] # Direccions per buscar simbols

for i in range(len(grid)):
    digits = []
    adjacent = []

    for j in range(len(grid[0])):
        c = grid[i][j]

        # Agafem els digits del numero
        if c.isdigit():
            digits.append(c)

            if adjacent:
                continue

            # Busquem simbols al voltant del numero
            for dx, dy in directions:
                x, y = j + dx, i + dy

                # Comprovem que no surti del rang de la matriu
                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    c = grid[y][x]

                    # Si trobem un simbol, parem de buscar
                    if len(adjacent) == 0 and c == '*':
                        adjacent.append((x, y))  
                        break
        else:
            if len(adjacent) > 0:
                part_number = number_from_digits(digits)
                for xy in adjacent:
                    if xy in gear_ratio_candidates:
                        gear_ratio_candidates[xy].append(part_number)
                    else:
                        gear_ratio_candidates[xy] = [part_number]

            digits = []
            adjacent = []

    # SI al final de la fila hi ha un numero, el guardem
    if len(adjacent) > 0:
        part_number = number_from_digits(digits)
        for xy in adjacent:
            if xy in gear_ratio_candidates:
                gear_ratio_candidates[xy].append(part_number)
            else:
                gear_ratio_candidates[xy] = [part_number]

# Calculem la suma total
total_sum = sum(gears[0] * gears[1] for gears in gear_ratio_candidates.values() if len(gears) == 2)
print(total_sum)
