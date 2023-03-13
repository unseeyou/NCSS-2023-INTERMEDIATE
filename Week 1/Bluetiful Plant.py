colour = input("Which colour did you find? ")
tins = input("Number of tins: ")

if 'blue' in colour.lower():
  print("Excellent! We'll soon have enough paint for the sky!")

elif int(tins) < 4:
  print(f"We're running out of {colour.lower()} paint. Let's restock!")

else:
  print(f"Great! We have {int(tins)} tins of {colour.lower()} paint.")
  
