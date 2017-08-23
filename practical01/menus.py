# get name
# display menu
# get choice
# while choice != Q
#  if choice == H
#  display "hello" name
#  else if choice == G
#  display "goodbye" name
#  else
#  display invalid message
#  display menu
#  get choice
# display finished message

name = str(input("Enter name: "))
user_choice = str(input("(H)ello\n(G)oodbye\n(Q)uit\n"))
while user_choice[0] != "Q" and user_choice[0] != "q":
    if user_choice[0] == "H" or user_choice[0] == "h":
        print("Hello, {}.".format(name))
    elif user_choice[0] == "G" or user_choice[0] == "g":
        print("Goodbye, {}.".format(name))
    elif user_choice[0] != "Q" and user_choice[0] != "q":
        print("Invalid choice.")
    user_choice = str(input("(H)ello\n(G)oodbye\n(Q)uit\n"))
print("Finished")