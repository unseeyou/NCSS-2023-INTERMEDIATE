dais = 0
props = []

while dais < 3:
  user = input("Username: ")
  if 'dais' in user.lower():
    props.append(user)
    dais += 1
  else:
    pass

props = sorted(props)
print(f"Proposals: {', '.join(reversed(props))}")  
