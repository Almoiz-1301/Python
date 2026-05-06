# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

for i in range(1, 6):
  match i:
    case 1:
      print("One")
    case 2:
      print("Two")
    case 3:
      pass
    case 4:
      print("Four")
    case 5:
      print("Five")
