#Define a list of names
names = ["Harry", "Ron", "Ravi", "Aryan"]

names.append("Ravanan")

names.sort()

print(names)
#create an empt seet
s = set()

#add elements to set
s.add(1)
s.add(2)
s.add(4)
s.add(3)
s.add(4)

print(s)
s.remove(2)
print(s)


print(f"The set has {len(s)} elements.")