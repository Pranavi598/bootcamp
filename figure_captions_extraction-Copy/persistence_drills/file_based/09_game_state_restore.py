import json

class Game:
    def __init__(self, level=1, score=0, inventory=None):
        self.level = level
        self.score = score
        self.inventory = inventory if inventory is not None else []

    def save_state(self, filename):
        """
        Save the current state of the game to a file in JSON format.
        """
        # Create a dictionary representing the game's state.
        game_state = {
            "level": self.level,
            "score": self.score,
            "inventory": self.inventory
        }

        # Serialize the game state to a JSON file.
        with open(filename, 'w') as file:
            json.dump(game_state, file)
        print(f"Game state saved to {filename}.")

    @classmethod
    def load_state(cls, filename):
        """
        Load a game state from a file and restore the game object.
        """
        # Read the saved game state from the file.
        with open(filename, 'r') as file:
            game_state = json.load(file)

        # Create a new Game instance with the loaded state.
        return cls(game_state['level'], game_state['score'], game_state['inventory'])

    def __repr__(self):
        return f"Game(level={self.level}, score={self.score}, inventory={self.inventory})"

# Example usage:
def main():
    # Create a new game instance
    game = Game(level=5, score=1000, inventory=["sword", "shield"])

    # Save the game state to a file
    game.save_state("game_state.json")

    # Create a new game instance (it starts with default values)
    new_game = Game()

    # Load the saved game state into the new instance
    new_game.load_state("game_state.json")
    print("Restored Game object:", new_game)

if __name__ == "__main__":
    main()
