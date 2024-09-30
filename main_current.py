from room import Room
from character import Character
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

# Setting Room Descriptions
lab.set_description("A usually spotless science facility lies in ruin, with broken glass strewn across the floor.\nVarious pools of liquid have gathered on the floor, one is a shade of deep red that sends a shudder down your spine.")
airlock.set_description("On the floor of the bare metal room lies an enviro-suit which has been torn to shreds.\nThrough the glass viewport, all you see is swirling red dust, not unusual at this time during the Martian year.")
hab.set_description("The centre of the station, it is devoid of its usual hum of everyday life.")

# Linking Rooms
hab.link_room(lab, "south")
lab.link_room(hab, "north")
lab.link_room(airlock, "west")
airlock.link_room(lab, "east")

# Creating Items
wrench = Item()
wrench.set_description("A long, rusty wrench that takes two hands to swing.")
wrench.set_name("wrench")

clipboard = Item()
clipboard.set_description("A flimsy wooden clipboard with some blood-soaked paper still attached.")
clipboard.set_name("clipboard")

# Adding Items to Rooms
lab.set_item(wrench)
airlock.set_item(clipboard)

# Creating Characters
xeno1 = Enemy("monstrous creature", "It emits an ear-piercing screech, almost forcing you to your knees.")
xeno1.set_weakness("wrench")

dave = Character("Dave", "A frightened coworker, with a suspicious look in his eyes.")
dave.set_conversation("Stay back! Whhhaa...Whhaat's happening?")

# Setting Characters in Rooms
lab.set_character(dave)
airlock.set_character(xeno1)

# Player Inventory
inventory = []

start_screen()

current_room = hab

# Main Game Loop
while True:
    print("\n----------------------------------------------------------------")
    
    # Show room details
    current_room.get_details()
    
    # Check if there is an inhabitant (character/enemy) in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print("---------------------------------------------------------------")
        inhabitant.describe()
    
    # Show items in the room
    item = current_room.get_item()
    if item is not None:
        print(f"You see a {item.get_name()} here.")
    
    # Player Input
    command = input("> ").lower()
    
    # Move Command
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
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
            if weapon in inventory:
                if inhabitant.fight(weapon):
                    print(f"You defeated {inhabitant.name}!")
                    current_room.set_character(None)  # Enemy is defeated, remove it from the room
                else:
                    print(f"The {inhabitant.name} defeated you!")
                    break
            else:
                print(f"You don't have a {weapon} in your inventory.")
        else:
            print("There's no one to fight here.")
    
    # Pick Up Item Command
    elif command == "take":
        if item is not None:
            print(f"You picked up the {item.get_name()}.")
            inventory.append(item.get_name())
            current_room.set_item(None)  # Remove the item from the room
        else:
            print("There's nothing to take here.")
    
    # Show Inventory Command
    elif command == "inventory":
        if inventory:
            print(f"Inventory: {', '.join(inventory)}")
        else:
            print("Your inventory is empty.")

    # Show Help Menu
    elif command == "help":
        show_help()

    # Unrecognized Command
    else:
        print("I don't know how to do that.")
