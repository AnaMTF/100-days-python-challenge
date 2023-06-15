#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
    "France" : {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visits": 12},
    "Germanry" : {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log)