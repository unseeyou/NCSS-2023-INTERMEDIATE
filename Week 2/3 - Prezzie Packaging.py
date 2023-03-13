base = int(input("Area of base: "))
step = int(input("Step: "))
for i in range(10, 21, step):
  print(f"Height: {i} cm, Volume: {base * i} cm³")
