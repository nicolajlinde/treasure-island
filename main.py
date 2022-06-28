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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
left_or_right = input("You're at a crossroad. Where do you want to go? " 'Type "left" or "right"')

if left_or_right == "left":
  wait_or_svim = input("You've come to a lake. There is an island in the middle of the lake. " + 'Type "wait" to wait for a boat. Type "swim" to swim across.')

  if wait_or_svim == "wait":
    red_yellow_blue = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

    if red_yellow_blue == "yellow":
      print("You found the treasure! You Win!")

      jungle_or_mountain = input("You're so close, you can feel it deep inside. You stand before an arching cliff with two possible routes. First one is through a wildly, exotic green jungle pass with water glistering from every leaf. Palms blooming with cooled, yellow to green bananas just deliciously riped for the taking. \n Second route is a rocky mountain pass with rocks, little fourlegged creatures, which seems to be some kind of leguanas. The harsh terrain is almost impossible climb, but you can manage. In the far distance you can see smoke and volcanic ash. So do you choose 'jungle' or 'mountain'")
      if jungle_or_mountain == "jungle":
        print("Congratulation you won the game and arrived at paradise island! You lived the life of a rich pirate and had plenty of adventures on the island and nearby seas")
      else: 
        print("You've arrived at Doomsday Mountain, the road obstructed by rocks and rocks and rocks. You start you're long, hard journey ahead but suddenly hear a crash. From the ledge above rains stones and boulders and a medium sized boulder hit you at the right side of your head. You fell unconsious and with your last breaths you see your family waiting for you.")
    elif red_yellow_blue == "red":
      print("It's a room full of fire. Game Over.")
    else:
      print("You enter a room of beasts. Game Over.")
  else:
    print("Game over")    
else:
  print("Game over")