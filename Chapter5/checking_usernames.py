current_users = ["Gustavo", "Camila", "Sorele", "Matheus", "Priscilla"]
new_users = ["Diego", "Lincoln", "Matheus", "Guilherme", "Priscilla"]

for user in new_users:
    if user in current_users:
        print("User already exists")
    else:
        print(f"Welcome, {user}")