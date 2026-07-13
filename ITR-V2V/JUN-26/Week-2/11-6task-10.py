# VARIOUS FUNTION OF SETS
# creation of dictionary
person = {
    "name" : "Alice",
    "age" : "25"
}
print("Dictionary : ",person)

#accesing elements
print("\nAccessing element : ",person["name"])

#adding another pair
person["city"] = "NY"
print("\nAfter Adding a pair : ",person)

#changing values
person["age"] = "26"
print("\nAfter Changing : ", person)

#removing a pair
person.pop("age")
print("\nAfter Removing a pair : ", person)

#Keys & Pairs
print("Keys : ",person.keys())
print("Values : ",person.values())
