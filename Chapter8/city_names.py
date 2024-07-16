def main():
    city = input("Enter a citY: ")
    country = input("Enter a country: ")
    formatted_string = city_country(city, country)
    print(formatted_string)

def city_country (city, country):
    return (f"{country}, {city}")

main()