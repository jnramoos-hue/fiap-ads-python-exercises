contacts = {
    "Clark Kent":
        {"Celphone": "1234",
        "E-mail":"super@krypton.com"},

    "Bruce Wayne":
        {"Celphone": "4321",
         "E-mail":"bat@caverna.com.br"}
}

for name, types_contacts in contacts.items():
    print(f"{name}")
    for types, contacts in types_contacts.items():
        print(f"{types}: {contacts}")
    print("------------------------")
  