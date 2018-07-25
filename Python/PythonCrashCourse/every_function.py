colours = ['Red', 'Black', 'White', 'Green', 'Blue']
print(len(colours))

print(colours)
colours.reverse()
print(colours)
colours.reverse()
print(colours)
print(sorted(colours))
print(sorted(colours, reverse=True))
print(colours)

colours.append('Purple')
print(colours)
del colours[-1]
print(colours)
colours.insert(0, 'Purple')
print(colours)
colours.remove('Purple')
print(colours)

last_colour = colours.pop()
print(last_colour)
print(colours)
colours.append('Blue')

colours.sort()
print(colours)
colours.sort(reverse=True)
print(colours)