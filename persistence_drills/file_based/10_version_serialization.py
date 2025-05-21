import json

class GameV1:
    """
    Version 1 of the Game class, has basic attributes level and score.
    """
    def __init__(self, level=1, score=0):
        self.level = level
        self.score = score

    def save_state(self, filename):
        """
        Save the current state of the game to a file in JSON format.
        """
        game_state = {
            "level": self.level,
            "score": self.score,
            "version": 1  # Include version information
        }
        with open(filename, 'w') as file:
            json.dump(game_state, file)

    @classmethod
    def load_state(cls, filename):
        """
        Load a game state from a file and restore the game object.
        """
        with open(filename, 'r') as file:
            game_state = json.load(file)

        # Handle versioning: if the game state is version 1, create an instance of GameV1
        if game_state.get('version') == 1:
            return cls(game_state['level'], game_state['score'])
        else:
            raise ValueError("Unsupported game state version")

    def __repr__(self):
        return f"GameV1(level={self.level}, score={self.score})"


class GameV2:
    """
    Version 2 of the Game class, adds an inventory attribute.
    """
    def __init__(self, level=1, score=0, inventory=None):
        self.level = level
        self.score = score
        self.inventory = inventory if inventory is not None else []

    def save_state(self, filename):
        """
        Save the current state of the game to a file in JSON format.
        """
        game_state = {
            "level": self.level,
            "score": self.score,
            "inventory": self.inventory,
            "version": 2  # Update version to 2
        }
        with open(filename, 'w') as file:
            json.dump(game_state, file)

    @classmethod
    def load_state(cls, filename):
        """
        Load a game state from a file and restore the game object.
        Handle both version 1 and version 2.
        """
        with open(filename, 'r') as file:
            game_state = json.load(file)

        # Handle versioning: Check if the saved version is 1 or 2
        if game_state.get('version') == 1:
            # If the game state is version 1, create a GameV2 instance, adding an empty inventory
            return cls(game_state['level'], game_state['score'], inventory=[])
        elif game_state.get('version') == 2:
            return cls(game_state['level'], game_state['score'], game_state['inventory'])
        else:
            raise ValueError("Unsupported game state version")

    def __repr__(self):
        return f"GameV2(level={self.level}, score={self.score}, inventory={self.inventory})"


# Example usage:
def main():
    # Create and save a GameV1 instance
    game_v1 = GameV1(level=3, score=500)
    game_v1.save_state("game_state_v1.json")

    # Load the saved GameV1 state and create a GameV2 object
    restored_game_v2 = GameV2.load_state("game_state_v1.json")
    print("Restored Game object from v1:", restored_game_v2)

    # Now, save a GameV2 instance
    game_v2 = GameV2(level=5, score=1000, inventory=["sword", "shield"])
    game_v2.save_state("game_state_v2.json")

    # Load the GameV2 state
    restored_game_v2 = GameV2.load_state("game_state_v2.json")
    print("Restored Game object from v2:", restored_game_v2)

if __name__ == "__main__":
    main()
