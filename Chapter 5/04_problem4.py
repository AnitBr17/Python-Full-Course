s = set()
s.add(20)
s.add(20.0)
s.add("20") # length of set will be 2 as 20 and 20.0 are considered same in set

print(len(s))  # prints 2