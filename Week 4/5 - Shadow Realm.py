def buy_shadow_tokens(gold):
  # Finish the function to convert gold to shadow tokens
  shadow_tokens = int(gold / 31)
  remainder = gold - shadow_tokens * 31
  return shadow_tokens

# Write the rest of your program here
print("Who dares campaign in the Shadow Realm?")

name = input("Name: ")
profiles = {}
while name:
  start_amt = int(input("Starting amount of gold: "))
  print(f"{name}'s here, starting with {buy_shadow_tokens(start_amt)} shadow tokens of gold!")
  profiles[name] = start_amt
  name = input("Name: ")

print("Let's play!")
player = input("Who played? ")
while player:
  gold_change = int(input("Gold won/lost: "))
  if player in profiles:
    profiles[player] += gold_change
  else:
    profiles[player] = 0
    profiles[player] += gold_change
  player = input("Who played? ") 
  
print("End of the campaign! Let's see how everyone did!")
for i in profiles:
  print(f"{i} has {profiles[i]} gold coins and can buy {buy_shadow_tokens(profiles[i])} shadow tokens.")
