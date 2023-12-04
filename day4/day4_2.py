with open("day4/input", "r") as file:
    document = file.readlines() # Llegim el fitxer i el guardem en una llista

allCards = {num+1: 1 for num in range(len(document))} # Inicialitzem el hashmpa a 1 per cada carta començant per 1 (id)

for line in document: 
    parts = line.split(": ") # Separem la línia en dos parts, card id i les cartes
    card_id = int(parts[0].split(" ")[-1]) # Obtenim el card id
    cards = line.strip().split(" | ") # Separem les cartes en una llista es separen per |
    elf_cards = set(cards[0].split())
    my_cards = set(cards[1].split())
     
    repetead_carts = my_cards.intersection(elf_cards) # Obtenim les cartes repetides

    for i in range(1, len(repetead_carts) + 1): #Per tantes repeticions com tingum augmentem el valor de la carta superior en base al numero de repeticions
            allCards[card_id + i] += allCards[card_id]

total_sum = 0
for card in allCards.keys():
    total_sum += allCards[card]

print(total_sum)