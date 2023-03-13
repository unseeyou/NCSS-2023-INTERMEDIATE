lyric = input("Lyric: ")
while lyric:
  if "end" not in lyric.lower() and lyric is not None:
    print(lyric)
    print("Do doo de do do de doo...")
    lyric = input("Lyric: ")
  else:
    print("It's the end")
    break
