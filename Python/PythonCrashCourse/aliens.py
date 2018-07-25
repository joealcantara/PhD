alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print(aliens)

aliens = []

for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

print("...")

print("Total number of aliens " + str(len(aliens)))
