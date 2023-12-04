with open("day4/input", "r") as file:
    document = file.readlines()

total_sum = 0
for line in document:
    parts = line.strip().split(" | ")
    elf_cards = set(parts[0].split())
    my_cards = set(parts[1].split())

    matches = elf_cards.intersection(my_cards)
    if matches:
        total_sum += 2 ** (len(matches) - 1)

print(total_sum)
