name = input("Name: ");
ppl = {};
while name:
  minutes = int(input("Minutes: "));
  if name in ppl:
    ppl[name] += minutes;
  else:
    ppl[name] = minutes;
  name = input("Name: ");
  
print("Exercise total:");
for i in ppl:
  print(f"{i}: {ppl[i]} {'amazing, you will smash that beep test!' if ppl[i] >= 100 else 'keep moving, you can do it!'}")
