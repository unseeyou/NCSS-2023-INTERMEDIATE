file = input("Novel file: ")

with open(file, 'r') as book:
  content = book.read()
  words = content.split()
  for i in words:
    if len(i) > 6:
      print(i)
    else:
      pass
  book.close()
