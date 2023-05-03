print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice = input("Your at a cross road. Where do yo want to go? Type 'left' or 'right'\n ").lower()

if choice == "left":
    choice2 = input ("You come across a lake inside the dungeon. Do you 'swim' to get to the other side, or 'wait' for the ferryman to take you across.\n").lower()
    if choice2 == "wait":
        choice3 = input ("You are safely taken to the island. You walk up a path to a house with three doors. 'red', 'blue', 'yellow', which door do you chose?\n").lower()
        if choice3 == "red":
            print("You enter a room with red smoke. You then fall unconcious. Game Over!")
        elif choice3 == "blue":
            print("You enter a room full of traps. You step on one and trigged the floor vanishing and you fall into a tank of sharks. Game Over!")
        elif choice3 == "yellow":
            print("You have found the room with the treasure. You win!")
        else:
            print("You chose a door that does not exsit. Something creeps behind you and knocks you out. Game Over!")
    else:
        print("You chose to take your chances with the sea monsters. While swimming across the sea you get a cramp and get eaten. Game Over!")
else:
    print("You continue down a path you can't return, you starve to death.")



