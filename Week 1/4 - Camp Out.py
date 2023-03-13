def sale_price(original, discount):
  #Calculate the sale price here.
  pass  # lol I didn;t use this

#Write the rest of your program here
#Grab the input (create the user prompts!)
name = input("Product: ")
og_price = float(input("Original price ($): "))
discount = float(input("Discount (%): "))

#Calculate the new price
print(f"{name} on sale for ${round((1 - discount/100) * og_price, 2)}.")

#Print the new price





