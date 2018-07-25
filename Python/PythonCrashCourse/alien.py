alien_0 = {'colour' : 'green', 'points' : 5}

print(alien_0['colour'])
print(alien_0['points'])
print(alien_0)

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("The colour of alien_0 is: " + alien_0['colour'] + ".")
alien_0['colour'] = 'yellow'
print("The colour of alien_0 is: " + alien_0['colour'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move alien to the right
# Determine how far to move the alien based on it's current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position of the alien is the old position + the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)