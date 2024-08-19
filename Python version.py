print("""
*******************************************************************************
           _                     _       _         
        | |                   | |     | |      
     ___| |__   ___   ___ ___ | | __ _| |_ ___ 
    / __| '_ \ / _ \ / __/ _ \| |/ _` | __/ _ \ 
   | (__| | | | (_) | (_| (_) | | (_| | ||  __/
The \___|_| |_|\___/ \___\___/|_|\__,_|\__\___| FACTORY!!!...Made by Betty Okwedadi         

I want to melt you down,                     
into a chocolate fountain             /) (\     
and then drink you!   *happy sighs*  ((,,,))   
                                 \,//(((((((\,/
  (I've always been addicted      (((  ^ ^  )))
  to chocolate in all forms       ))))  -   ((((
  I know it's really wicked but  (()(\ )-( /))()
  I've fallen for its charms)    ))))/`-\~\.((((  Betty, 
                                 ((( \/==\_\ )))  The Giant Chocolate Monster!!!
*******************************************************************************
""")
print("Welcome to The Chocolate Factory!")
print("Your mission is to find and capture, Betty, the Giant Chocolate Monster, while she's sleeping.")


def choice3actions():
    choice3 = input("You arrive at the door covered in gooey, dripping chocolate, Yum!.\n "
                    "You open the door and you find 3 more doors... OOOh!.\n "
                    "one red, one yellow and one blue.\n "
                    "Which colour do you choose?\n").lower()
    if choice3 == "red":
        print("You have been melted down into Hot Chocolate and drank by Betty.\n Game Over, Delicious You!")
    elif choice3 == "blue":
        print("You have been turned into a blue candy and eaten by Betty.\nGame Over, Delicious You!")
    elif choice3 == "yellow":
        print(
            "Bravo!!! \n You have found and captured Betty, the Giant Chocolate Monster, while sleeping. \n You will have free chocolate for the rest of your life.\n You Win!")
    else:
        print("You made a choice that led you straight into Betty's mouth.\nGame Over, Delicious You!")


choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a chocolate fountain. '
                    'There is a door on the other side of it, to get to the door, \n'
                    'you have to make the right choice. \n '
                    'Will you "Drink" from or "Bath" in the fountain? \n').lower()
    if choice2 == "bath":
        choice3actions()
    else:
        print("You got attacked and eaten by a Monster Chocolate Bird named Betty.\nGame Over, Delicious You!")
elif choice1 == "right":
    choice4 = input("OOPS!!!"
                    "You have fallen into a chocolate lake."
                    "Will you Swim or Fly?\n").lower()
    if choice4=="swim":
        choice3actions()
    else:
        print("You got attacked and eaten by a Monster Chocolate Bird named Betty.\nGame Over, Delicious You!")
else:
    print("You made a choice that led you straight into Betty's mouth.\nGame Over, Delicious You!")
