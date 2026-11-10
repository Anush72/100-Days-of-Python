# Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# getting value using key in dictionary
print(programming_dictionary["Bug"])

# adding the keys and values
programming_dictionary["Loop"] = "The action of doing over and over"
print(programming_dictionary)

#creating the empty dictionary
empty_dictionary = {}

# wiping down dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit the item
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
