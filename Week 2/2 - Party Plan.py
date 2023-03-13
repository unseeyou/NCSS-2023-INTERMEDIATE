emoji = "🥳"
theme = input("Party theme: ")
supplies = input("Supplies needed: ").split(' ')
print(f"The {theme} party is coming up soon!")
print("We will need to get...")
for i in supplies:
  print(f"{emoji} {i}")
print(f"Remember to invite your {theme} buddies!")
