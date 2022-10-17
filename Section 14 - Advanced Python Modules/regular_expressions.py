from pkgutil import extend_path
import re

text = "My phone number is 30-123-45-56. Call soon!"

print("phone" in text)

pattern = "phone"
print(re.search(pattern, text))  # span (start index, end index)

# csak az első előfordulást írja ki
match = re.search(pattern, text)
print(match.span())
print(match.start())

# több előfordulás kiírása
text2 = "first phone, second phone"
matches = re.findall(pattern, text2)
print(len(matches))

for match in re.finditer(pattern, text2):
    # return each match object
    print(match)
    print(match.group())
