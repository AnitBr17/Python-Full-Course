try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("2.txt not found")

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
