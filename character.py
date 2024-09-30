
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
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item + ", it scuttles away and is quickly out of sight")
            return True
        else:
            print(self.name + " leaps onto your face, as you try to pull it off your vision fades to black.")
            return False
        
