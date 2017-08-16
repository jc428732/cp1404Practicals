name = str(input("What is your name?"))
if len(name) > 0:
  for letter in range(0, len(name)):
    if letter % 2 == 1:
      print(name[letter])
