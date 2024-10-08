from room import Room
from character import Character
from character import InjuredCharacter
from character import Enemy
from item import Item
from help_file import show_help

# Function to show the start screen
def start_screen():
    
    print("###########################################")
    print("#            Habitat: Extinction          #")
    print("###########################################")
    print("\nType help at any time to access the help menu")
    print("\nPress Enter to start the game...")
    input()  # Wait for the player to press Enter

# Creating Rooms

lab = Room("Laboratory")
airlock = Room("Air Lock")
hab = Room("Habitation Room")
engineering = Room("Engineering Room")
storage = Room("Storage Room")
armory = Room("Armory")  
combat_practice_room = Room("Combat Practice Room")  
surface = Room("Planet's Surface")
medbay = Room("Medical Bay")
thunderhawk = Room ("Thunderhawk Gunship")

# Setting descriptions for each room

lab.description = "A usually spotless science facility lies in ruin, with broken glass strewn across the floor.\nVarious pools of liquid have gathered on the floor, one is a shade of deep red that sends a shudder down your spine."
airlock.description = "A bare metal room with a glass viewport and keypad for exit.\nThrough the glass viewport, all you see is swirling red dust, not an unusual sight on this barren hell-hole."
hab.description = "The centre of the station, it is devoid of its usual hum of everyday life."
engineering.description = "The beating heart of the station. The room thrums with sounds of various life support systems."
storage.description = "Shelves filled with supplies and equipment surround you."
armory.description = "This room is stocked with weapons and armor, designed for the defense of the station. Various firearms and protective gear line the walls."
combat_practice_room.description = "A room designed for training, filled with holographic projections of alien creatures. The walls bear deep gouges and scorch marks as memories of some overenthusiastic training sessions."
medbay.description = "A dimly lit chamber filled with buzzing machinery and the scent of disinfectant."
surface.description = "Despite the dust storms that ravage this continent daily, you make out the silhouette of a Thunderhawk gunship"
thunderhawk.description =" "
# Setting the lock code for the airlock door

surface.lock_code = "7159"  # This area is locked

# Linking Rooms 

hab.link_room(lab, "south")
hab.link_room(engineering, "west")
lab.link_room(hab, "north")
lab.link_room(airlock, "west")
airlock.link_room(lab, "east")
airlock.link_room(surface, "west")  # Link to the surface room
engineering.link_room(hab, "east")
engineering.link_room(combat_practice_room, "north")  # Link to the new Combat Practice Room
combat_practice_room.link_room(engineering, "south")  # Link back to engineering
combat_practice_room.link_room(storage, "east")  # Link to storage
storage.link_room(combat_practice_room, "west")  # Link back to the Combat Practice Room
storage.link_room(armory, "north")
storage.link_room(medbay, "east")  # Link to armory
armory.link_room(storage, "south")  # Link back to storage
medbay.link_room(storage, "west")
surface.link_room(airlock, "east")
surface.link_room(thunderhawk, "north")

# Creating Items
wrench = Item()
wrench.set_description("A long, rusty wrench that takes two hands to swing.")
wrench.set_name("wrench")

clipboard = Item()
clipboard.set_description("A flimsy wooden clipboard with some blood-soaked paper still attached.")
clipboard.set_name("clipboard")

boltgun = Item()  
boltgun.set_description("A powerful boltgun that fires explosive rounds, designed for taking down heavily armored targets.")
boltgun.set_name("Boltgun")

medikit = Item()
medikit.set_description("A medical kit containing supplies to treat minor injuries and stabilize serious wounds.")
medikit.set_name("Medikit")

plasma_rifle = Item()
plasma_rifle.set_description("Blue plasma coil glow along the length of the gun's stock. Although powerful enough to penetrate almost any armour, these highly destructive weapons always carry the chance of overheating with devasting effect.")
plasma_rifle.set_name("Plasma Rifle")

krak_grenade = Item()
krak_grenade.set_description("A devestatingly powerful fragmentation grenade.")
krak_grenade.set_name("Krak Grenade")

# Adding Items to Rooms

hab.set_item(wrench)
lab.set_item(clipboard)
engineering.set_item(boltgun)
medbay.set_item(medikit)  
armory.set_item(plasma_rifle)
storage.set_item(krak_grenade)

# Creating Characters
    
#Enemies
xeno1 = Enemy("Small Insectoid Creature", "It emits an ear-piercing screech, almost forcing you to your knees. It spits a corrosive green acid at you that burns a hole in the wall behind you as you dodge it.")
xeno1.add_multiple_weaknesses("wrench", "combat knife", "boltgun", "plasma rifle")

xeno2 = Enemy("Alien Warrior", "A large, menacing insectoid creature prowls the shadows, ready to attack anyone who dares enter its territory. Walking on four legs it has razor sharp sycthes in place of the front two.")
xeno2.add_multiple_weaknesses("boltgun", "plasma rifle")


xeno3 = Enemy ("Brood Lord", "Like the previous creatures you have encountered this monstrosity bares some resembalance to the insects of old Terra yet it is almost as bug as the gunship you are trying to reach. It's hidous maw opens to reveal hundreds of razor sharp teeth")
xeno3.add_multiple_weaknesses("plasma rifle", "krak grenade")

# Friendly characers
parsus = Character("Parsus", "A frightened chapter serf, with a suspicious look in his eyes.")
parsus.set_conversation('''"Stay back! Whhhaa...Whhaat's happening?"\n*Under other circumstances a serf would be severely reprimanded for speaking to an Astartes this way. Especially you, First Captain Belial, but this case feels like an exception.*''')

apothecary = InjuredCharacter ("Apothecary Uriel", "An equally talented warrior and medic, he sits slumped in the corner, surrouned by alien corpses, his breathin is heavy and blood pours from gashes in his power armour")
apothecary.set_conversation ("Thank the Emperor you appeared when you did, we need to leave iimmediately. There is a shuttle just beyond the airlock which can get us back to the fleet, one of the expeditation crew gave me the airlock door code before he passed its 7159")

nathanael = Character("Brother Sergeant Nathanael", "A sergeant who serves under you in the 1st Company Deathwing. Beneath his usual stoicism, a nervousness shows.")
nathanael.set_conversation('''"Brother Captain, I am pleased to see you still alive; many of our comrades have not been so lucky.\n *He points to a corpse; the power armor it wears has been torn to shreds, with helmet still in place and armor so badly mangled you can't make out which of your 1st company comrades has fallen.*\n"You should take that bolter and gather as many weapons as you can; I think we have a fight on our hands The Tyranids are upon us!."''')

# Setting Characters in Rooms

lab.set_character(parsus)
airlock.set_character(xeno1)
engineering.set_character(nathanael)
combat_practice_room.set_character(xeno2)
medbay.set_character(apothecary)
surface.set_character (xeno3)

# Player Inventory

inventory = []

start_screen()

current_room = hab

previous_room = None  # Initialize previous room

while True:
    print("\n----------------------------------------------------------------")
    
    # Check if the room is locked before allowing any actions
    if current_room.is_locked():
        while current_room.is_locked():  # Stay in this loop until the correct code is entered or the player decides to leave
            lock_code = input("Enter the four-digit code to unlock the door (or type 'back' to return to the previous room): ").lower()

            if lock_code == current_room.lock_code:
                print("The room is now unlocked!")
                current_room.lock_code = None  # Remove the lock code after unlocking
            elif lock_code == "back":
                if previous_room is not None:
                    print("You decide to return to the previous room.")
                    current_room = previous_room  # Move back to the previous room
                else:
                    print("There's no room to return to!")
                break  # Exit the loop after returning to the previous room
            else:
                print("Incorrect code. Try again or type 'back' to leave.")
        continue  # Skip further actions until the room is unlocked or player returns
    
    # Show room details
    current_room.get_details()

    # Check if there is an inhabitant (character/enemy) in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print("---------------------------------------------------------------")
        inhabitant.describe()

    # Show items in the room
    item_in_room = current_room.get_item()
    if item_in_room is not None:
        print(f"You see a {item_in_room.get_name()} here.")

    # Store the current room as the previous room before moving
    previous_room = current_room  # Track the current room before moving to a new one

    # Player Input
    command = input("> ").lower()

    # Move Command
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)  # Move to the new room
    #Endgame Condition
    if current_room == thunderhawk: 
        print("\nYou rush towards the Thunderhawk gunship, your heart pounding in your chest.")
        print("\nAs you board and the engines roar to life, you jump into the gunners seat.")
        print("\nThe ships powerful Stormcannons barely make a scratch in the hoard of Tyranids now overwhelming the outpost.")
        print("\nYou must get news of this incident to Chapter Master Azreal, it will take a company if not the entire chapter to put and end to this invasion!")
        print("\n--- GAME OVER: You have successfully escaped the planet and rejoined the fleet in orbit! ---")
        input("Press Enter to exit the game.")
        break
    
    # Talk Command
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one to talk to here.")
    
    # Fight Command
    elif command == "fight":
        if isinstance(inhabitant, Enemy):
            weapon = input("What will you fight with? > ").lower()

            if any(i.get_name().lower() == weapon for i in inventory):
                if inhabitant.fight(weapon):
                    print(f"You defeated {inhabitant.name}!")
                    current_room.set_character(None)  # Enemy is defeated, remove it from the room

                   
                else:
                    print(f"The {inhabitant.name} defeated you!")
                    input("Press Enter to exit the game.")
                    break
            else:
                print(f"You don't have a {weapon} in your inventory.")
        else:
            print("There's no one to fight here.")

    # Pick Up Item Command
    elif command == "take":
        if item_in_room is not None:
            print(f"You picked up the {item_in_room.get_name()}.")
            inventory.append(item_in_room)
            current_room.set_item(None)  # Remove the item from the room
        else:
            print("There's nothing to take here.")

    # Show Inventory Command
    elif command == "inventory":
        if inventory:
            print("Inventory: " + ", ".join([i.get_name() for i in inventory]))  # Display the names of the items
        else:
            print("Your inventory is empty.")

    # Heal Command
    elif command == "heal":
        if isinstance(inhabitant, InjuredCharacter) and inhabitant.is_injured:
            heal_item = input("What will you use to heal? > ").lower()
            if any(i.get_name().lower() == heal_item for i in inventory):  # Check if the item is in inventory
                inhabitant.heal(heal_item)  # Heal the injured character
                if not inhabitant.is_injured:
                    print(f"{inhabitant.name} has been healed and can now talk.")
            else:
                print(f"You don't have a {heal_item}.")
        else:
            print("There's no one to heal here or they don't need healing.")
    
    # Show Help Menu
    elif command == "help":
        show_help()

    # Unrecognized Command
    else:
        print("I don't know how to do that.")