import time as t
import os

inventorytoget=["knife","gold coin", "brass key", "gold key", "gun", "bullets", "silver bullets", "diamond", "portal key", "key", "potion", "pen", "paper", "keycard"]
inventory=[]
global tigersdead
tigersdead = ""
global lives
lives = 3
global pin
pin = ""
global health
health = 10
global end
end = ""

def reddoor():
    global health
    global lives
    global tigersdead
    if tigersdead == "yes":
        mysterydoor()
    else:
        print()
        print("You have entered a room full of tigers. They are going to attack you!")
        t.sleep(1)
        print()
        haveknife = input("Do you want to check your inventory to see if you have a knife to attack?")
        t.sleep(1)
        if haveknife == "yes":
            print()
            print("Inventory :", inventory)
            if "knife" in inventory:
                print()
                print("Excellent, you have a knife, ready to fight!")
                t.sleep(2)
                print()
                print("You have decided to fight the tigers, you slash at the tigers with the knife and kill one. \nAnother attacks you and bites you, your health decreases by 50")
                health = health -50
                t.sleep(2)
                if health <= 0:
                    print()
                    print("Your health is too low. \nThe tiger over powers you and eats you. \nYou are dead")
                    print()
                    t.sleep(2)
                    lives = lives -1
                    health = 0
                    if lives == 0:
                        print()
                        print("Out of lives, GAME OVER")
                    else:
                        lobby()
                elif health >10:
                    print()
                    print("Your health is ", health)
                    t.sleep(2)
                    print()
                    print("You are wounded but still able to fight, you continue to fight the tigers. \nYou swip and kill the other tiger. Phew!")
                    print()
                    tigersdead = "yes"
                    t.sleep(2)
                    print()
                    print("The knife is damaged beyond repair. \nYou leave it behind")
                    print()
                    inventory.remove("knife")
                    print()
                    t.sleep(1)
                    print("You notice in the room is a bottle of liquid, and a bookcase")
                    print()
                    t.sleep(2)
                    drink = input("You examine the bottle and it says drink me, do you drink it?")
                    print()
                    if drink == "yes":
                        t.sleep(1)
                        print("You decide to drink the liquid.  Phew... its an energy drink. It adds 100 to your health")
                        print()
                        health = health +100
                        print("Your health is ", health)
                        print()
                        bookshelf = input("You look at the bookshelf and apart from being dusty there is not much on it. \nDo you want ot explore further?")
                        if bookshelf == "yes":
                            mysterydoor()
                        elif bookshelf == "no":
                            print()
                            print("You go back down to the hallway")
                            option1()
                    else:
                        print()
                        print("You chose not to drink the bottle")
                        option1()
            elif "knife" == "no":
                print()
                print("The tigers are quick to attack! \nThey eat you! You die")
                lives = lives -1
                if lives == 0:
                    print()
                    print("THE END")
                    print("***********************************************************************************************")
                else:
                    print()
                    print("RESTART")
                    t.sleep(1)
                    lobby()
        else:
            print()
            print("So you don't want to check for a knife.  \nThats ok, you can go back to the hallway")
            option1()

def greendoor():
    print()
    print("Would you like to open the Chest, explore the Basket or inspect the Boot?")
    t.sleep(1)
    print()
    explore = input("What do you want to explore? or X to return to hallway").lower()
    if "chest" in explore or "c" in explore:
        t.sleep(1)
        print()
        if "gold coin" in inventorytoget and "brass key" in inventorytoget:
            print("You opened the chest and find a: \n-Golden coin\n-Brass key. \nYou add them to your inventory")
            inventory.append("gold coin")
            inventory.append("brass key")
            inventorytoget.remove("gold coin")
            inventorytoget.remove("brass key")
            print("Inventory :", inventory)
            print()
            cont = input("You continue to look around the green room. Press enter to continue")
            print()
            greendoor()
        else:
            print("You have collected everything you need to collect from here")
            option1()
    elif "basket" in explore or "bask" in explore:
        t.sleep(1)
        print()
        if "knife" in inventorytoget:
            print("You explore the basket and find a: \n-Knive\nScore! You put it in your inventory")
            inventory.append("knife")
            inventorytoget.remove("knife")
            print("Inventory :", inventory)
            print()
            wait = input("You continue to look at the green room")
            greendoor()
        else:
            print("You have collected everything you need to collect from here")
            option1()
    elif explore == "boot":
        t.sleep(1)
        print()
        if "key" in inventorytoget:
            print("You search the boot and find it to be quite smelly. \nBut you decide to check inside anyway and find a: \n-Key")
            inventory.append("key")
            inventorytoget.remove("key")
            print()
            print("Inventory :", inventory)
            print()
            twosecs = input("You continue to look around the green room")
            print()
            greendoor()
        else:
            print("You have collected everything you need to collect from here")
            option1()
    else:
        print()
        print("You will return to the hall")
        option1()

def orangedoor():
    global health
    t.sleep(2)
    print()
    print("You have entered a bathroom full of food. \nYou are quite hungry so you eat some")
    print()
    print("This adds to your health")
    health =  health + 90
    print("Your health is now: ",health)
    print()
    print("You head back to hallway")
    print()
    option1()

def mysterydoor():
    global lives
    print()
    print("You are in the mystery room")
    print()
    print("You explore the bookshelf further and decide to see whats behind it.  \nYou see a door")
    print()
    print("The door looks like you need to insert a keycard to enter. \nDo you want to check if you have a keycard?")
    t.sleep(1)
    keycard = input()
    if keycard == "yes":
        print("Inventory :", inventory)
        if "keycard" in inventory:
            print()
            print("You have a keycard!")
            print()
            mysterydoor = input("Do you want to try to use the keycard in the door?")
            if mysterydoor == "yes":
                t.sleep(1)
                print()
                print("You insert the keycard and the door opens")
                inventory.remove("keycard")
                print()
                print("You have found yourself in a safe room. You see: \nSilver bullets \nPotion\nGold Key\nPlus a live added to lives. You add to your inventory")
                inventory.append("silver bullets")
                inventory.append("potion")
                inventory.append("gold key")
                inventorytoget.remove("silver bullets")
                inventorytoget.remove("potion")
                inventorytoget.remove("gold key")
                lives = lives +1
                print("Inventory :", inventory)
                t.sleep(1)
                print()
                print("You have finished exploring this room, you return to the hallway")
                option1()
            else:
                print()
                print("You don't want to try mystery door")
                option1()
        else:
            print()
            print("You have no keycard, return to hallway")
            option1()
    else:
        print()
        print("You don't want to check for keycard. Return to hallway")
        option1()
        
def option1():
    t.sleep(1)
    print()
    print("One door is Green, one door is Red, on door is Orange. Which door would you like to go into?")
    print()
    colourDoor = input("Enter choice. X to go back to lobby").lower()
    if "red" in colourDoor:
        t.sleep(2)
        reddoor()
    elif "green" in colourDoor:
        t.sleep(2)
        print()
        print("You enter a bedroom with some interesting things. There is a chest, there is a hanging basket, there is a old boot")
        t.sleep(2)
        greendoor()  
    elif "orange" in colourDoor:
        t.sleep(2)
        orangedoor()
    else:
        t.sleep(2)
        print()
        print("You didn't select a door. Return to lobby")
        t.sleep(2)
        lobby()

def option2():
    global pin
    global lives
    global health
    print()
    lookkey = input("Do you want to check if you have a key to open the safe?")
    t.sleep(1)
    if lookkey == "yes":
        if "key" in inventory:
            t.sleep(1)
            print()
            print("You have a key! You can open the safe!")
            #inventory.remove("key")
            t.sleep(1)
            print()
            bomb = input("You open the safe and there is a bomb! Do you have the code to deactive the bomb?")
            t.sleep(1)
            if bomb == "yes":
                if pin == "1234":
                    print()
                    print("You check for the pin written on the paper. The pin is: ",pin)
                    t.sleep(1)
                    print()
                    code = input("Enter code")
                    if code == "1234":
                        t.sleep(1)
                        print()
                        print("Excellent, you deactived the bomb! Phew! You can now get whats in the safe!")
                        inventory.remove("paper")
                        t.sleep(2)
                        print("***********************************************************************************************")
                        print()
                        print("You find some: \n- Diamonds\n- Gun\n- Keycard\nScore! You add them to your inventory")
                        t.sleep(2)
                        inventory.append("diamond")
                        inventory.append("gun")
                        inventory.append("keycard")
                        inventorytoget.remove("diamond")
                        inventorytoget.remove("gun")
                        inventorytoget.remove("keycard")
                        print()
                        print("Inventory :", inventory)
                        t.sleep(1)
                        print()
                        print("You head back to the lobby")
                        lobby()
                    else:
                        print()
                        print("BOOM! You're dead")
                        health = 0
                        lives = lives -1
                        print("***********************************************************************************************")
                        if lives == 0:
                            t.sleep(1)
                            print()
                            print("GAME OVER")
                            print("***********************************************************************************************")
                        else:
                            print()
                            print("RESTART")
                            print("***********************************************************************************************")
                            lobby()
                else:
                    print("You don't have the pin")
                    print()
                    print("BOOM! You're dead")
                    health = 0
                    lives = lives -1
                    print("***********************************************************************************************")
                    if lives == 0:
                        t.sleep(1)
                        print()
                        print("GAME OVER")
                        print("***********************************************************************************************")
                    else:
                        print()
                        print("RESTART")
                        print("***********************************************************************************************")
                        lobby()
            elif bomb == "no":
                    t.sleep(1)
                    print("You don't have the pin!")
                    print("BOOM! You're dead")
                    health = 0
                    lives = lives -1
                    print("***********************************************************************************************")
                    if lives == 0:
                        t.sleep(1)
                        print()
                        print("GAME OVER")
                        print("***********************************************************************************************")
                    else:
                        t.sleep(1)
                        print()
                        print("RESTART")
                        print("***********************************************************************************************")
                        lobby()     
        else:
            print()
            print("You have no key")
            t.sleep(1)
            lobby()
    else:
        print()
        print("You decided not to look for a key. Back to lobby")
        lobby()
           
def option3():
    global health
    global lives
    global pin
    print()
    kitchen = input("Do you want to explore cupboard, fridge or drawer? X for lobby")
    if kitchen == "cupboard":
        t.sleep(2)
        print()
        if "pen" in inventorytoget:
            print("You open the cupboard and see a:\n-Pen \nYou put the pen in your inventory")
            inventory.append("pen")
            inventorytoget.remove("pen")
            print()
            print("Inventory :", inventory)
            t.sleep(2)
            print()
            explore = input("you go back to exploring kitchen. Enter to continue")
            option3()
        else:
            print("You have already collected this item")
            lobby()
    elif kitchen == "fridge":
        t.sleep(2)
        print()
        cake = input("You open the fridge and see a cake. Do you want to eat the cake?")
        if cake == "yes":
            t.sleep(2)
            print()
            print("You eat the cake but it tastes funny. You realise it might have been laced with poision")
            t.sleep(2)
            print()
            remedy = input("You need some kind of potion to save yourself. Do you want to check inventory for potion?")
            t.sleep(2)
            if remedy == "yes":
                t.sleep(2)
                print()
                print("Inventory :", inventory)
                if "potion" in inventory:
                    t.sleep(2)
                    print()
                    print("You have the potion! Phew! You take the potion and the effects of the poision are reduced")
                    inventory.remove("potion")
                    t.sleep(2)
                    print()
                    print("This reduces your health by 50 but you get an extra life for your iron gut")
                    t.sleep(2)
                    print("You further examine the cake and see a key inside it. Its a : \nPortal key\nYou add it to your inventory")
                    inventory.append("portal key")
                    health = health -50
                    print()
                    print("Your health is: ",health)
                    lives = lives +1
                    print()
                    print("You have :", lives, "lives left")
                    t.sleep(2)
                    option3()
                    if health <=0:
                        print()
                        print("Your health is too low. You die")
                        t.sleep(1)
                        lives = lives - 1
                        if lives == 0:
                            print()
                            print("GAME OVER")
                            print("***********************************************************************************************")
                        elif lives >0:
                            lobby()
                else:
                    print()
                    print("You have no potion! The poision kills you")
                    t.sleep(4)
                    lives = lives - 1
                    health = 0
                    lobby()
                    if lives == 0:
                        print()
                        print("GAME OVER")
                        print("***********************************************************************************************")
                    else:
                        print()
                        print("RESTART")
                        print("***********************************************************************************************")
                        lobby()
            else:
                print()
                print("You don't want to check for potion. The effects of the poision kills you")
                t.sleep(4)
                lives = lives - 1
                health = 0
                lobby()
                if lives == 0:
                    print()
                    print("GAME OVER")
                    print("***********************************************************************************************")
                else:
                    print()
                    print("RESTART")
                    print("***********************************************************************************************")
                    lobby()
        else:
            print()
            print("Ok, you don't want to eat the cake. Return to the lobby")
            lobby()                                  
    elif kitchen == "drawer":
        print()
        t.sleep(2)
        if "paper" in inventorytoget:
            print("You open the drawer and see a carving of a 4 digit number and a scape of: \n-Paper\nYou take the paper")
            t.sleep(2)
            inventory.append("paper")
            inventorytoget.remove("paper")
            print()
            t.sleep(2)
            print("You need a pen to write down the pin. You check inventory")
            t.sleep(2)
            print()
            print("Inventory :", inventory)
            if "pen" in inventory:
                print()
                t.sleep(2)
                print("You have a pen and write down the pin on the paper in your inventory")
                t.sleep(2)
                pin = "1234"
                print()
                print("The pin is 1234. Its saved for you under pin. You leave the pen")
                inventory.remove("pen")
                t.sleep(2)
                option3()
            else:
                print()
                print("You have no pen. You leave the drawer alone")
                t.sleep(2)
                option3()
        else:
            print("You have collected everything you need to collect from here")
            lobby()
    else:
        lobby()
            

def option4():
    global health
    global lives
    global end
    t.sleep(1)
    print()
    check = input("Do you want to check your inventory to see if you have anything useful to open the door?")
    if check == "yes":
        print("Inventory :", inventory)
        print()
        whichobject = input("What item do you want to use?")
        t.sleep(1)
        if whichobject == "gold key":
            if "gold key" in inventory:
                print()
                print("Excellent, you have a gold key. You try this in the door and it opens!")
                t.sleep(2)
                print()
                print("Inside is a warewolf! Oh no!! You need to check your inventory to see what you have")
                print()
                print("Inventory :", inventory)
                t.sleep(2)
                print()
                fightwarewolf = input("What item do you want to use?")
                if fightwarewolf == "gun":
                    if "gun" in inventory:
                        print()
                        print("Yes, thats probably for the best")
                        print()
                        bullets = input("Which bullets do you want to use?")
                        if "silver" in bullets or "silver bullets" in bullets:
                            if "silver bullets" in inventory:
                                print()
                                print("Yes, you will need silver bullets to fight a warewolf!")
                                t.sleep(1)
                                print()
                                print("You have a gun and silver bullets! You put the bullets in the gun and shoot at the warewolf")
                                t.sleep(2)
                                print()
                                print("The bullet hits the warewolf and the warewolf dies")
                                t.sleep(2)
                                print()
                                print("You look around the room and see a chest on the floor. You open it and find all the treasure you could ever want")
                                t.sleep(1)
                                print()
                                inventory.remove("silver bullets")
                                print("You take the treasure and leave. You have WON the game!")
                                end = "yes"
                                keepgoing = input("Do you want to return to lobby and see if there is more adventure to be had?")
                                if keepgoing == "yes":
                                    print("Return to lobby")
                                    lobby()
                                    t.sleep(2)
                                else:
                                    print()
                                    print("THE END!")
                                    t.sleep(1)
                                    print("***********************************************************************************************")
                        elif bullets == "bullets": 
                            if "bullets" in inventory:
                                t.sleep(2)
                                print()
                                print("You have normal bullets to put in the gun. You load and shoot but this doesn't kill the warewolf")
                                t.sleep(2)
                                print()
                                print("It does give you enough time to close the door and lock it, which you do. Phew!")
                                t.sleep(2)
                                print()
                                print("All this stress has reduced your health by 60")
                                inventory.remove("bullets")
                                health = health -60
                                if health <= 0:
                                    print()
                                    print("Your health is too low to continue. You die")
                                    lives = lives -1
                                    if lives <= 0:
                                        print()
                                        print("THE END")
                                else:
                                    lobby()
                            else:
                                lobby()
                                t.sleep(2)
                else:
                    print()
                    print("Oh dear you don't have a gun and sliver bullets")
                    t.sleep(1)
                    print()
                    print("The warewolf attacks and you die")
                    t.sleep(1)
                    health = 0
                    lives = lives -1
                    if lives == 0:
                        t.sleep(1)
                        print()
                        print("You are out of lives")
                        t.sleep(1)
                        print()
                        print("THE END")
                        print("***********************************************************************************************")
                    else:
                        print("RESTART")
                        lobby()
        else:
            print()
            print("You don't have what you need to open the door")
            t.sleep(1)
            option4()
    else:
        print()
        print("You don't want to look for an item. Return to lobby")
        lobby()
    
def option5():
    print()
    if "bullets" in inventorytoget:
        print("You see a rusty box sitting on a table. You open the table and take: \n-Bullets")
        inventory.append("bullets")
        inventorytoget.remove("bullets")
        print()
        print("You notice a lift. The lift says insert gold coins")
        print()
        goldcoin = input("Do you want to check if you have a gold coin to insert in the lift?")
        if goldcoin == "yes":
            print()
            print("Inventory :", inventory)
            if "gold coin" in inventory:
                print()
                print("You have gold coins! Brilliant!  You put a gold coin into the lift coin drop")
                inventory.remove("gold coin")
                lifttoattic()
            else:
                print()
                print("You have no gold coins. You return to lobby")
                lobby()
        else:
            print("You have collected everything you need to collect from here")
            lobby()
    else:
        print()
        print("You notice a lift. The lift says insert gold coins")
        print()
        goldcoin = input("Do you want to check if you have a gold coin to insert in the lift?")
        if goldcoin == "yes":
            print()
            print("Inventory :", inventory)
            if "gold coin" in inventory:
                print()
                print("You have gold coins! Brilliant!  You put a gold coin into the lift coin drop")
                inventory.remove("gold coin")
                lifttoattic()
            else:
                print()
                print("You have no gold coins. You return to lobby")
                lobby()
        else:
            print("You don't want to look for a coin. Return to lobby")
            lobby()

def lifttoattic():
    global health
    global end
    print()
    print("Once the coin has been inserted you hear the lift moving.  The door soon opens and you get in")
    t.sleep(1)
    print()
    print("The lift takes you up to the attic")
    t.sleep(1)
    print()
    brasskey = input("There is a door but it is looked.\nDo you want to look in inventory for a key?")
    if brasskey == "yes":
        t.sleep(1)
        print()
        print("Great, you have the brass key")
        inventory.remove("brass key")
        t.sleep(1)
        print()
        if end == "yes":
            print("You open the door and enter the room.  Inside you see a machine says deposit a diamond.")
            diamond = input("Do you want to check to see if you have a diamond?")
            if diamond == "yes":
                print("Inventory :", inventory)
                if "diamond" in inventory:
                    print("You have a diamond!")
                    t.sleep(2)
                    insertdia = input("Do you want to insert the diamond?")
                    if insertdia == "yes":
                        t.sleep(2)
                        print("You insert the diamond into the machine")
                        print("This opens a metal door")
                        inventory.remove("diamond")
                        print("You enter the room and see a packet of sweets. You eat them and it increases your health by 100")
                        health = health + 100
                        portal = input("You look around further and find a portal.  Do you have a portal key?")
                        if portal == "yes":
                            if "portal key" in inventory:
                                print("You have used the portal key and are transported to a different universe. Start level 2")
                                ##add code here
                            else:
                                print("No portal key. Return to lobby")
                                lobby()
                        else:
                            print("You dont want to look for a portal key. Return to lobby")
                            lobby()
                    else:
                        print("Ok, keep the diamond. You go back down the lift to the lobby")
                        lobby()
                else:
                    print("You have no diamond.  You return to lobby")
                    lobby()
            else:
                print("You don't want to check for a diamond. You return to lobby")
                lobby()
        else:
            print("You haven't completed all elements of the game.  Come back later")
            lobby()
    else:
        print("You have no brass key. \nYou go back down the lift to the lobby")
        lobby()
         
def lobby():
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("***********************************************************************************************")
    print("You enter the door which going to the lobby of the house")
    print()
    print("In your inventory is :", inventory)
    print("You have :", lives, "lives")
    print("Your health is: ", health)
    t.sleep(1)
    print()
    print("Looking around you see a staircase, a door on the left, a door on the right and a door to the basement.")
    groundfloor()
    print()
    print("What do you want to do? \n1 Go up stairs\n2 Left door\n3 Right door\n4 Basement\n5 Explore lobby")
    selection = input("Enter choice")
    if selection == "1":
        print("***********************************************************************************************")
        t.sleep(1)
        print()
        print("You go up the stairs to the first floor. \nHere there are 3 rooms")
        t.sleep(1)
        firstfloor()
        option1()
    elif selection  == "2":
        print("***********************************************************************************************")
        t.sleep(1)
        print()
        print("You have selected the left door")
        t.sleep(1)
        print()
        print("You enter a room with a safe")
        option2()
    elif selection  == "3":
        print("***********************************************************************************************")
        t.sleep(1)
        print()
        print("You have selected the right door")
        t.sleep(1)
        print()
        print("Through the right door you see the kitchen. \nThe kitchen looks pretty old and dusty. \nYou look around and see a cupboard, a fridge and a drawer")
        option3()
    elif selection == "4":
        print("***********************************************************************************************")
        t.sleep(1)
        t.sleep(1)
        print()
        print("You have selected the basement")
        t.sleep(1)
        print("***********************************************************************************************")
        print()
        print("You go down the stairs to the basement and see a door. \nYou try to open the door but it is locked")
        option4()
    elif selection  == "5":
        print("***********************************************************************************************")
        t.sleep(1)
        print()
        print("You have decided to explore the lobby")
        option5()
    else:
        print()
        print("You haven't selected a valid option.  Restart lobby")
        lobby()
        
def adventure():
    print("Welome to adventure game")
    print()
    print("You see a house. The door is open. Do you want to go in?")
    door = input("")
    if "yes" in door or "YES" in door or "Y" in door or "y" in door:
        t.sleep(2)
        lobby()
    elif "no" in door or "NO" in door or "N" in door or "n" in door:
        print("Goodbye")
    else:
        print()
        print("You have typed in the incorrect text")
        adventure()

    
def groundfloor():
    print("Ground Floor map")
    print("________________________________________________________________")
    print("|                                            |                   |__________|                                 |")
    print("|                                            |                   |__________|                                 |")
    print("|                                            | Option 4     |__Option 1 _|                                 |")
    print("|                                            |                   |__________|                                 |")
    print("|                                            |                   |__STAIRS__|                                 |")
    print("|                Option 2               |__________|__________|        Option 3             |")
    print("|                                            |                                      |                                 |")
    print("|                                            |                                      |                                 |")
    print("|                                            |             Lobby                |                                 |")    
    print("|                                           |~|            Option 5           |~|                              |")
    print("|                                           |  |                                    |~|                              |")
    print("|                                           |  |                                    |~|                              |")
    print("_______________________ |~|___________________ |~|________________|")

def firstfloor():
    print("First Floor map")
    print("________________________________________________________________")
    print("|                                            |                                      |                                 |")
    print("|                                            |                                      |                                 |")
    print("|                                            |          Red Door              |                                 |")
    print("|                                            |                                      |                                 |")
    print("|                                            |                                      |                                 |")
    print("|                Green Door          |_____|~________~|____ |      Orange Door        |")
    print("|                                            |                                      |                                 |")
    print("|                                            |                                      |                                 |")
    print("|                                            |         ___________         |                                 |")    
    print("|                                           |~|       |__________|         |~|                              |")
    print("|                                           |  |       |__________|         |  |                              |")
    print("|                                           |  |       |__________|         |  |                              |")
    print("_______________________ |~|____|__________| ____ |~|________________|")


adventure()
