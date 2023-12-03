def getValue(cadena):
    digits = [d for d in cadena if d.isdigit()]
    if not digits:
        return 0
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)

with open("day1/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

total_sum = 0

for line in document:
    total_sum += getValue(line)

print(total_sum)