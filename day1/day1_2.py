def wordToDig(): # Funció que retorna el digit corresponent a la paraula, posem la primera lletra i l'ultima en cas que hi hagin dos digits que compartexin la mateixa lletra
    return {
        'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
        'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
    }

def getDigits(string):
    digit_dict = wordToDig() # Obtenim el diccionari de paraules i digits
    for word, digit in digit_dict.items(): # Iterem per cada paraula i digit
        string = string.replace(word, digit) # Replace la paraula pel digit
    return string

def getValue(line): # Funció que retorna el valor corresponent a la línia
    string = getDigits(line) # Passem les paraules a digits
    digits = [d for d in string if d.isdigit()]  # Obtenim els digits de la línia
    if not digits: # Si no hi ha digits, retornem 0
        return 0
    first_digit = digits[0] # Obtenim el primer digit
    last_digit = digits[-1] # Obtenim l'ultim digit
    return int(first_digit + last_digit) # Retornem el valor corresponent a la línia

with open("day1/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

total_sum = 0

for line in document:
    total_sum += getValue(line)

print(total_sum)
