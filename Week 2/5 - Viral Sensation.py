dances = ['ballet', 'tap', 'jazz', 'belly', 'contemporary', 'ballroom', 'salsa', 'step', 'swing', 'irish', 'modern', 'shuffle', 'floss', 'twisting', 'macarena', 'interpretive', 'wobble', 'flick', 'stomp', 'tango']

def viral_check(name):
  #Find how viral this dance will go
  level = ''
  
  if name in dances:
    level = 'nowhere, the dance already exists'
  elif len(name) == 8:
    level = 'not viral'
  elif 'j' in name:
    level = 'somewhat viral'
  elif len(name) < 4:
    level = 'slightly viral'
  else:
    level = None
    
  return level


#Write the rest of your program after this.
names = input("Enter names: ").split(" ")
ultra = 0
if names[0] != '':
  for i in names:
    v = viral_check(i)
    if v is not None:
      print(f"The '{i}' will go {v}!")
    else:
      ultra += 1

print(f"Ultra Viral names: {ultra}")
  
