guests = ['Jane', 'Johnno', 'Dazza', 'Beryl', 'Kylie', 'Noa', 'Ainjewel', 'Brie', 'Wengie']

# Add your code after this.
q = input("Guest name: ")
if q.title() in guests:
  print(f"{q} is on the list!")
else:
  print(f"{q} is not invited.")
