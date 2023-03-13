shopping = ['flour', 'milk', 'eggs', 'sugar', 'butter', 'baking powder']
tick = ' ✅'
print(f"Shopping List ({len(shopping)} items): {', '.join(shopping)}")
item = input("What ingredient did you find? ")
if item in shopping:
  print(f"{item} has been found!")
  print(f"Remaining items: {', '.join(shopping).replace(item, f'{item}{tick}')}")
else:
  print("Whoops, that's not on the list!")
  print(f"Remaining items: {', '.join(shopping)}")
