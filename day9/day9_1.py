def calculate_differences(nums): # Calculem la diferència entre els valors consecutius de la llista
    return [nums[i+1] - nums[i] for i in range(len(nums)-1)]

def find_next_value(nums):
    # Convertim els valors de la llista a int
    nums = list(map(int, nums))

    sequences = [nums] # Afegim la llista de valors a la llista de llistes
    while not all(x == 0 for x in sequences[-1]): # Mentre no tots els valors de l'ultim element de la llista de llistes siguin 0
        sequences.append(calculate_differences(sequences[-1])) # Afegim la diferència entre els valors consecutius de la llista

    # Calculem el valor de la següent llista
    next_value = nums[-1] # Agafem l'ultim valor de la llista
    for seq in reversed(sequences[1:]): # Per cada llista de la llista de llistes començant per la segona
        next_value += seq[-1] # Sumem l'últim num de la sequencia actual a next_value

    return next_value

with open("day9/input.txt", "r") as file:
    document = file.readlines()

result = 0
for line in document:
    nums = line.strip().split(" ")

    next_value = find_next_value(nums)
    result += next_value

print(result)  

