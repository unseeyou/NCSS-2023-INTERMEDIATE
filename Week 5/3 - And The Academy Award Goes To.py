filename = input("Enter an award file: ")
print("And the nominees are...")

with open(filename, 'r') as file:
  names = file.readlines()
  for i in names:
    names[names.index(i)] = i.strip()
  nominees = sorted(set(names))
  file.close()

for i in nominees:
  print(f"🎬 {i}")
