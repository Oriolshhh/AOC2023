class Hand: # Classe Hand amb els seus atributs i funcions per saber quin tipus es/si es millor que una altre
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = self.find_type()

    def is_pair(self):
        return self.cards.count(self.cards[0]) == 2 or self.cards.count(self.cards[1]) == 2 or \
               self.cards.count(self.cards[2]) == 2 or self.cards.count(self.cards[3]) == 2 or \
               self.cards.count(self.cards[4]) == 2

    def is_two_pairs(self):
        pairs = 0
        for card in set(self.cards):
            if self.cards.count(card) == 2:
                pairs += 1
        return pairs == 2

    def is_three_of_kind(self):
        return any(self.cards.count(card) == 3 for card in set(self.cards))

    def is_full_house(self):
        return self.is_three_of_kind() and self.is_pair()

    def is_four_of_kind(self):
        return any(self.cards.count(card) == 4 for card in set(self.cards))

    def is_five_of_kind(self):
        return len(set(self.cards)) == 1

    def find_type(self):
        if self.is_five_of_kind():
            return 6
        elif self.is_four_of_kind():
            return 5
        elif self.is_full_house():
            return 4
        elif self.is_three_of_kind():
            return 3
        elif self.is_two_pairs():
            return 2
        elif self.is_pair():
            return 1
        else:
            return 0

    def better_hand(self, other_hand):
        priority_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] # Prioritat de les cartes

        if self.type < other_hand.type: # Si la ma és millor
            return False 
        elif self.type > other_hand.type: # Si la ma és pitjor
            return True
        else:
            for i in range(5):
                if priority_cards.index(self.cards[i]) < priority_cards.index(other_hand.cards[i]):
                    return True
                elif priority_cards.index(self.cards[i]) > priority_cards.index(other_hand.cards[i]):
                    return False
            return False

def updateList(hands_list, new_hand): 
    for i, hand in enumerate(hands_list): # Per cada ma de la llista
        if new_hand.better_hand(hand): # Si la nova ma es millor que la ma de la llista
            hands_list.insert(i, new_hand) # Afegim la nova ma a la llista
            return
    hands_list.append(new_hand) # Si no hem afegit la ma a la llista, la afegim al final

with open("day7/input", "r") as file:
    document = file.readlines()

hands_list = [] # Llista de hands
for line in document: # Per cada línia
    parts = line.strip().split(" ")
    cards = parts[0] # Obtenim les cartes
    bid = parts[1] # Obtenim la bid

    #Creem la nova ma
    hand = Hand(cards, bid)
    updateList(hands_list, hand) # Actualitzem la llista de hands

# Calculem el resultat
total_result = 0
for i, hand in enumerate(hands_list):
    total_result += hand.bid * (len(hands_list) - i)  # El ranking es invers al de la llista

print(total_result)
