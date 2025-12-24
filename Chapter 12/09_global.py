a = 89

def func():
    # global a
    a = 3
    print(a)  # this will print local a
    
func()
print(a)  # this will print global a

