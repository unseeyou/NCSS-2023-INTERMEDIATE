def calculate_iron(ore):
  # Calculate the Iron from Ore, to 1 decimal place
  pass

# Write the rest of your program here
ore = float(input("Ore: "))
iron = round(ore * (5/13), 1)


def e(n):  # my function is just better
  if n < 5:
    return "Useless lump"
  elif 20 > n >= 5:
    return "Pickaxe"
  elif 20 <= n < 35:
    return "Sword"
  elif 35 <= n < 45:
    return "Fancy shield"
  elif n >= 45:
    return "Magic amulet"
  
  
item = e(iron)

print(f"{iron} Iron - {item}")

