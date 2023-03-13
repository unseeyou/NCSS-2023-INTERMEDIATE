ppl = {}
print("Let's start the walk-a-thon!")
name = input("Who has recorded a walk? ")
total_dist = 0
while name:
  dist = float(input("How far did they walk? "))
  total_dist += dist
  if name not in ppl:
    print(f"That's a first time for {name}! They walked {dist} km!")
    ppl[name] = dist
    
  else:
    print(f"Another walk from {name}. Well done on another {dist} km!")
    ppl[name] += dist
  
  name = input("Who has recorded a walk? ")
  
print(f"Thanks for taking part in the walk-a-thon! We walked a total of {total_dist} km!")
print("Here is a list of merit certificate winners:")
winners = []
for i in ppl:
  winners.append(i)
  
for i in sorted(winners):
  print(f"🏅 {i}")
