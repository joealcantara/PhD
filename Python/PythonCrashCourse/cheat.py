spell = [i for i in range (1, 21)]
spell_count = []

for i in range(1, 21):
    total = i*(i+1)/2
    spell_count.append(total)

print(spell)
print(spell_count)