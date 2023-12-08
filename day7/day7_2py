from collections import Counter

def hand_to_value(hand): # Calcula el valor de la ma
    counts = sorted(Counter(hand).values()) # Compte les cartes de la ma i les ordena
    num_jokers = hand.count("J") # Comptem els jokers
    
    if num_jokers and num_jokers < 5: # Si hi ha jokers i són menys de 5
        counts.remove(num_jokers) # Eliminem els jokers
        counts[-1] += num_jokers # I sumem els jokers a la carta més alta

    if counts == [5]: # Si hi ha 5 cartes iguals
        return 7 
    elif counts == [1, 4]: # Si hi ha 4 cartes iguals
        return 6
    elif counts == [2, 3]: # Si hi ha 3 cartes iguals i una parella
        return 5
    elif counts == [1, 1, 3]: # Si hi ha 3 cartes iguals
        return 4
    elif counts == [1, 2, 2]: # Si hi ha 2 parelles
        return 3
    elif counts == [1, 1, 1, 2]: # Si hi ha 1 parella
        return 2
    elif counts == [1, 1, 1, 1, 1]: # Si no hi ha res
        return 1

def tiebreaker(hand):  # Calcula el valor de cada carta de la ma
    card_values = "J23456789TQKA" # Valors de les cartes
    tiebreak_scores = [] 
    for c in hand: # Per cada carta de la ma
        tiebreak_scores.append(card_values.index(c)) # Afegim el valor de la carta
    return tuple(tiebreak_scores) # Retornem el valor de cada carta

def calculate_score(): # Calculem la puntuació total
    scored_hands = [] # Llista de mans amb puntuació

    with open("day7/input", "r") as file:
        for line in file: # Per cada línia del fitxer
            hand, bid = line.strip().split() # Separem la hand i la bid
            hand_value = hand_to_value(hand) # Calculem el valor de la hand 
            tiebreak_score = tiebreaker(hand) # Calculem el valor de cada carta de la hand
            bid_value = int(bid) # Convertim la bid a int
            scored_hands.append((hand_value, tiebreak_score, bid_value)) # Afegim la ma, el valor de la hand i la bid
            
    # Ordenem les hands en funcio del primer element del tuple (valor de la hand) i en cas d'empat, en funció del segon element del tuple (valor de cada carta de la hand) que a la vegada consultarà el valor de la primera carta, la segona, etc.
    scored_hands.sort() 
    total_score = 0 # Puntuació total
    for idx, scored_hand in enumerate(scored_hands):
        bid = scored_hand[2]  # Agafem la bid (tercer eelment del tuple)
        total_score += (idx + 1) * bid

    return total_score

print(calculate_score())
