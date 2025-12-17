a = int(input("Enter your age: "))

# If else else ladder

if(a>=18):
    print("You are above the age of consent")
    print("Good  for you!")
    
elif(a>0):
    print("You are entring an invalid negative age")
    
elif(a==0):
    print("You are entrening 0 whihc is not a valid age")
    
else:
    print("You are below the age of consent")
    print("You are not allowed")
    
print("End of program")