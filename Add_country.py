# Add new country to an existing dictionary
# Create a dictionary

country = input("What is the country you visited: ")
visits = int(input("How many times you visited: "))
list_of_cities = eval(input("What are the cities you visited: "))

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "Country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(name, times_visits, cities_visited):
  new_country = {}
  new_country["country"] = name 
  new_country["visits"] = times_visits
  new_country["cities"] = cities_visited

  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(travel_log)
