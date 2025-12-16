marks ={
    "Harry": 100,
    "Rohan": 56,
    "Aakash": 23,
    0: "Harry"
  }

# print(marks.items()) # returns a list of tuples of key-value pairs
# print(marks.keys())  # returns a list of all the keys in the dictionary
# print(marks.values())# returns a list of all the values in the dictionary
# marks.update({"Ankit": 45, "Renuka": 100})  # Adding a new key-value pair to the dictionary
# print(marks)

print(marks.get("Harry2"))  # Prints None if the key is not found
print(marks["Harry2"])  # Raises KeyError if the key is not found