people = [
    {"name": "Ravana", "house": "srilanka"},
    {"name": "Ravi", "house": "Tamil"},
     {"name": "viyan", "house": "Andra"}
    ]

people.sort(key=lambda person: person["name"])
print(people)
