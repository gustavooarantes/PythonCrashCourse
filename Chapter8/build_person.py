def build_person(first_name, last_name, age=""):
    person = {
        "first": first_name,
        "last": last_name,
    }
    if age:
        person["age"] = age
    return person

musician = build_person("Jimi", "Hendrix", 27)
print(musician)