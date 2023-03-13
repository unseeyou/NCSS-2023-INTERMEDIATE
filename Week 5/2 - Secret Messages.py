with open('book.txt', 'r') as file:
  lines = file.readlines()
  file.close()

pw = input("Password: ")
secret = []

for line in lines:
  if pw.lower() in line.lower():
    secret.append(line.lower().split()[0])
  else:
    pass

for i in secret:
  print(i)
