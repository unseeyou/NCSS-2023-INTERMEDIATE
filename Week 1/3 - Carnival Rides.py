def tall_enough(height):
  # Write your function here.
  height = int(height)
  if height >= 130:
    print("You can ride the ship of the desert!")
  elif height >= 100:
    print("You can ride the pony!")
  else:
    print("You can ride the teacups!")
# Write the rest of your program here.
h = input("How tall are you? ")
tall_enough(h)
