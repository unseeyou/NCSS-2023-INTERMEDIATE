key = {}

with open('midi.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    thing = line.split()
    key[thing[0]] = thing[1]  # 'number': 'letter and number combo'
  file.close()
  
msg = input("Secret Message: ")
result = []
secret = msg.split()

for i in secret:
  try:
    result.append(key[i])
  except KeyError:
    pass

print(f"Translation: {' '.join(result)}")
