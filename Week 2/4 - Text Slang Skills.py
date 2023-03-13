slang = ['GTG', 'LOL', 'IMD', 'IDK', 'IDC', 'CTC?', 'BTW', 'TBH', 'LMK', 'NVM']
msg = input("Text message: ").replace(',',' ').replace('.', ' ').replace('!', ' ').split(' ')
count = 0

for i in msg:
  if i in slang:
    count += 1
    
print(f"Number of slang words used: {count}")
