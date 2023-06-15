#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
    "France" : {"cities_visited": ["Paris", "Dijon", "Lille"],
                "total_visits": 12},
    "Germany" : {"cities_visited":["Berlin", "Hamburg", "Stuttgart"],
                 "total_visits": 5},
}

print(travel_log)

#Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Dijon", "Lille"],
        "total_visits": 12},
    {
        "country": "Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5},
]