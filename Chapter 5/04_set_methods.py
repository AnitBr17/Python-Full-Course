s = {1, 5, 32, 54, 5,5,5,5, "Harry"}

print(s, type(s))  # sets are unordered collections of unique elements

s.add(546)  # Adding an element to the set
print(s, type(s)) # prints the set with the new element added
s.remove(1) # Removing an element from the set
print(s, type(s)) # prints the set with the element removed