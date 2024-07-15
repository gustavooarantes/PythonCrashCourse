responses = {}

while True:
    name = input("What's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        break

print("\n--Poll Results--")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")