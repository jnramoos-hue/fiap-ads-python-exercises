#criando um dicionario com dados


dictionary = {
    "Yoda":"Jedi Master",
    "Mace Windu": "Jedi Master",
    "Anakin Skywalker":"Jedi Knight",
    "R2-D2":"Droide",
    "Dex":"Clerk"
}

print(dictionary.get("Dex"))

print(dictionary.keys())

for key in dictionary.keys():
    print(dictionary.get(key))

print(len(dictionary.values()))
print("Jedi Master" in dictionary.values())

print(dictionary.items())

for name, category in dictionary.items():
    print(f"The name of character {name} is a {category}")

