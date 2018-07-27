responses = {}

poll_live = True
while poll_live:
    name = input("\nWhat is your name?")
    response = input("If you could visit any place in the world, where would it be?")
    responses[name] = response

    keep_going = input("Would you like someone else to take the poll? (yes/no)")
    if keep_going.lower() == 'yes':
        continue
    else:
        poll_live = False

print("Here are the responses")
for k, v in responses.items():
    print(k.title() + " would like to go to " + v.title())
    
    