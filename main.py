first = input("First Player Enter:")
second = input("Second Player Enter:")

if first == "S" and second == "P":
  print("first won")
elif first == "P" and second == "S":
  print("second won")
elif first == "P" and second == "P":
  print("Draw")
elif first == "S" and second == "S":
  print("Draw")
elif first == "R" and second == "S":
  print("first won")
elif first == "S" and second == "R":
  print ("second won")
elif first == "R" and second == "R":
  print("Draw")
elif first == "P" and second == "R":
  print("first won")
elif first == "R" and second == "P":
  print("second won")
else:
  print("Play again")
