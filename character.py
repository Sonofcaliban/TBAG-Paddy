
class Character():
 # Create a character​

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None


    def describe(self):

        print(f"{self.name} appears!")
        print( self.description)


    def set_conversation(self, conversation):
        self.conversation = conversation


    def talk(self):
       if self.conversation is not None:
        print(f"[{self.name}]: {self.conversation}")
       else:
          print(f"[{self.name}] won't talk to you!")


    def fight(self, combat_item):
       print(f"{self.name} doesn't want to fight with you!")
       return True
    
class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weaknesses = []  # Store multiple weaknesses in a list

   
    def add_multiple_weaknesses(self, *item_weaknesses):
        self.weaknesses.extend([item.lower() for item in item_weaknesses])  # Add multiple weaknesses at once
   
   
    def fight(self, combat_item):
        if combat_item.lower() in self.weaknesses:  # Check if the combat item is in the weaknesses list
            print("You deal a mortal wound to the " + self.name + " with the " + combat_item + ", it lets out a final, defiant roar as its body leaks black, acidic ichor.")
            return True
        else:
            print(self.name + " Your vision fades to black. The last thing you see is your battle brothers avenging you and the apothercary leaning over your dying body.")
            return False

class InjuredCharacter(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.is_injured = True  # Start as injured

    # Override the talk method
    def talk(self):
        if self.is_injured:
            print(f"[{self.name}] is too injured to talk right now.")
        else:
            super().talk()  # Use the talk method from the parent class if healed

    # Method to heal the character
    def heal(self, item):
        if item.lower() == "medikit":  # If the item is a Medikit, heal the character
            self.is_injured = False
            print(f"You healed {self.name} with the {item}. They can talk now.")
        else:
            print(f"{self.name} cannot be healed with {item}.")