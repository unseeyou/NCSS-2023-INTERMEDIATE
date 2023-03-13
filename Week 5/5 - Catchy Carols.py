def get_replacements(replacements_filename):
  # Given the name of a file containing word-replacement pairs, 
  # return a dictionary that contains these pairs. The original words should
  # be dictionary keys and the replacement words should be the values.
  pass


def convert_word(word, replacements):
  # Given a single word, returns the replacement word in the same case if a 
  # replacement exists for this word. If there is no replacement, then it
  # returns the original word.
  pass


def convert_line(line, replacements):
  # Given a string line and the replacements dictionary, returns the line 
  # as a string with the words changed to their replacements and a space in 
  # between each word. 
  pass


def print_new_song(carol_filename, replacements):
  # Given the name of the file containing the carol and a replacement words
  # dictionary, prints out the title and lyrics of the new song
  pass


# Screw the functions

# Write the rest of your program here
filename = input("Filename of carol lyrics: ")
with open(filename, 'r') as file:
  lyrics = file.readlines()
  file.close()
  
filename = input("Filename of replacement words: ")
replacements = {}
with open(filename, 'r') as file:
  lines = file.readlines()
  for l in lines:
    secret = l.split()
    replacements[secret[0]] = secret[1]
  file.close()
print("")
intro = "MY CHRISTMAS SONG!"
sentence = []
for word in intro.split(' '):
  if word.lower() in replacements:
    if word == word.upper():
      sentence.append(replacements[word.lower()].upper())
    if word == word.lower():
      sentence.append(replacements[word.lower()].lower())
    if word == word.title():
      sentence.append(replacements[word.lower()].title())
  else:
    sentence.append(word)
      
print(' '.join(sentence))
      
for i in lyrics:
  words = i.strip().split(' ')
  sentence = []
  for word in words:
    word = word.strip()
    if word.lower() in replacements:
      if word == word.upper():
        sentence.append(replacements[word.lower()].upper())
      if word == word.lower():
        sentence.append(replacements[word.lower()].lower())
      if word == word.title():
        sentence.append(replacements[word.lower()].title())
    else:
      sentence.append(word)
  print(' '.join(sentence))
