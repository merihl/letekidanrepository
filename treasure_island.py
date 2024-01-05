# Treasure Island: treasure finder program

directions = input("which direction do you want to go? left or right.\n")
action = input("Do want to swim or go to the wall? choose swim or wall.\n")
door_choice = input("Which door do you want to choose? yellow, red or blue.\n")

if directions is left:
  if action is wall:
    if door_choice is yellow:
      print("You Win!!!!!!!!!!!")
    elif door_choice is red:
      print("Burned by fire \n", "Game Over!")
    elif door_choice is yellow:
      print("Eaten by beasts.\n", "Game Over")
    else:
      print("Game Ober!")

  else:
    print("Attacked by trout.\n", "Game Over")

else:
  print("Fall into a hole.\n", "Game Over!")


      
    

