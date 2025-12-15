letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>", "Anit").replace("<|DATE|>", "20th June 2024"))

# The replace() method is used to replace a specified phrase with another specified phrase.