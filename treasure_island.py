directions = input("which direction do you want to go? left or right.\n")

if directions == "right":
  print("Fall into a hole.\n", "Game Over!")
  
elif directions == "left":
  action = input("Do want to swim or go to the wall? choose swim or wall.\n")
  
  if action == "swim":
    print("Attacked by trout.\n", "Game Over")
  elif action == "wall":
    door_choice = input("Which door do you want to choose? yellow, red or blue.\n")
    
    if door_choice == "yellow":
      print("You Win!!!!!!!!!!!")
    elif door_choice == "red":
      print("Burned by fire \n", "Game Over!")
    elif door_choice == "blue":
      print("Eaten by beasts.\n", "Game Over")
    else:
      print("Game Ober!")
  else:
    print("Game Over!!")
  
else:
  print("Game Over!!")
