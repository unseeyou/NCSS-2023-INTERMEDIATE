init_pop = int(input("Initial population: "))
final_pop = int(input("Final population: "))
years = 0

while init_pop < final_pop:
  init_pop = init_pop * 1.37
  years += 1

print(f"It would take {years} years for there to be {final_pop} rabbits.")
