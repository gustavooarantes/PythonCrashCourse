age = int(input("How old are you? "))

if age < 2:
    print("You're a baby")
elif age >= 2 and age < 4:
    print("you're a toddler")
elif age >= 4 and age < 13:
    print("You're a kid")
elif age >= 13 and age < 20:
    print("You're a teenager")
elif age >= 20 and age < 65:
    print("You're an adult")
else:
    print("You're an elder")