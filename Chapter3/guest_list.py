guests = ["Einstein", "Oppenheimer", "Plank", "Heisenberg"]
for i in range(len(guests)):
    print(f"Hello, {guests[i]}, you are invited to the dinner!")

print("\n")

cant_make_it = guests.pop()
guests.append("Bohr")
print(f"Unfortunately, {cant_make_it} can't make it. So I invited {guests[3]} to the dinner!")
for i in range(len(guests)):
    print(f"Hello, {guests[i]}, you are invited to the dinner!")

print("\n")

print("I've found a bigger dinner table and will be inviting new guests!")
guests.insert(0, "Newton")
guests.insert(2, "Curie")
guests.append("Coulomb")
for i in range(len(guests)):
    print(f"Hello, {guests[i]}, you are invited to the dinner!")

print("\n")

print("Now I can only invite 2 people for the dinner. Sorry guys!")
for i in range(len(guests) - 2):
    popped = guests.pop()
    print(f"You can't make it, {popped}!")
for i in range(len(guests)):
    print(f"{guests[i]}, see you at the dinner!")