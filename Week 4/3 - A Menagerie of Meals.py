loop = 0
food_items = []  # unnecessary but funny
book = {}
while loop != 5:
  name = input("Friend: ")
  recipe = input("Which recipe did they recommend? ")
  if recipe not in food_items:
    loop += 1
    food_items.append(recipe)
    book[recipe] = name
    print(f"{name} recommended {recipe}!")
  else:
    print("Someone else already recommended that.")
  

print("Cookbook complete! Recipes include:")
for i in book:
  print(f"{i}: recommended by {book[i]}")
