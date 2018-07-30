# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating 3D print from design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for model in completed_models:
    print("\t" + model.title())