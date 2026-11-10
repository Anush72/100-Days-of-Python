# Nesting Lists and Dictionaries

capitals = {
    'France' : "Paris",
    "Germany" : "Berlin"
}

# Nested List in Dictionary
travel_log = {
    'France' : ["Paris","Lille","Dijon"],
    'Germany' : ["Stuttgart","Berlin"]
}

# print out Lille
print(travel_log['France'][1])

# nested list
nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

# nested dictionaries
travel_log = {
    'France' :
        {   "cities_visited" : ["Paris","Lille","Dijon"],
            "total visits" : 8
        },
    'Germany' :
        { "cities_visited" : ["Stuttgart","Berlin"],
          "total visits" : 18
        }
}
# printing Stuttgart
print(travel_log["Germany"]["cities_visited"][0])