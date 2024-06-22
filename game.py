class Character:
    def __init__(self, name, strength, intelligence, dexterity):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.inventory = []

    @classmethod
    def create_character(cls):
        print("Character Creation:")
        name = input("Enter your character's name: ")
        strength = int(input("Enter strength (1-10): "))
        intelligence = int(input("Enter intelligence (1-10): "))
        dexterity = int(input("Enter dexterity (1-10): "))
        return cls(name, strength, intelligence, dexterity)

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Dexterity: {self.dexterity}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")

class Story:
    def __init__(self):
        self.paths = {
            "start": self.start,
            "path1": self.path1,
            "path2": self.path2,
        }

    def start(self, character):
        print("You find yourself in a dark forest. Two paths lie ahead.")
        choice = input("Do you take the left path or the right path? (left/right): ")
        if choice == "left":
            self.paths["path1"](character)
        elif choice == "right":
            self.paths["path2"](character)
        else:
            print("Invalid choice. Try again.")
            self.start(character)

    def path1(self, character):
        print("You took the left path and encounter a wild beast!")
        # Implement more story elements and decisions here

    def path2(self, character):
        print("You took the right path and find a hidden treasure chest!")
        puzzle = Puzzle("Solve this riddle to open the chest: What has keys but can't open locks?", "keyboard")
        if puzzle.solve():
            character.add_to_inventory("Golden Key")
        # Implement more story elements and decisions here

class Game:
    def __init__(self, character):
        self.character = character
        self.story = Story()

    def start(self):
        print("Starting the game...")
        self.story.start(self.character)

    def display_character_stats(self):
        self.character.display_stats()

    def show_inventory(self):
        self.character.show_inventory()

class Puzzle:
    def __init__(self, description, solution):
        self.description = description
        self.solution = solution

    def solve(self):
        print(self.description)
        answer = input("Your answer: ")
        if answer.lower() == self.solution.lower():
            print("Correct! Puzzle solved.")
            return True
        else:
            print("Incorrect. Try again.")
            return False

def main():
    print("Welcome to the Text-Based Adventure Game!")
    player = Character.create_character()
    game = Game(player)
    game.start()

if __name__ == "__main__":
    main()
