import json

class Game:
    def __init__(self, level=1, score=0):
        self.level = level
        self.score = score

    def to_dict(self):
        """
        Convert the Game object to a dictionary for serialization.
        """
        return {
            "level": self.level,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, game_dict):
        """
        Create a Game object from a dictionary (used for deserialization).
        """
        return cls(game_dict["level"], game_dict["score"])

    def __repr__(self):
        return f"Game(level={self.level}, score={self.score})"


class MyCollection:
    def __init__(self):
        self.items = []

    def add(self, item):
        """
        Add an item (Game object) to the collection.
        """
        self.items.append(item)

    def to_dict(self):
        """
        Convert the collection of Game objects to a list of dictionaries for serialization.
        """
        return [item.to_dict() for item in self.items]

    @classmethod
    def from_dict(cls, collection_dict):
        """
        Create a MyCollection object from a list of dictionaries (deserialization).
        """
        collection = cls()
        for item_dict in collection_dict:
            collection.add(Game.from_dict(item_dict))
        return collection

    def save_state(self, filename):
        """
        Serialize the collection and save it to a file.
        """
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load_state(cls, filename):
        """
        Load the collection from a file and return a MyCollection object.
        """
        with open(filename, 'r') as file:
            collection_dict = json.load(file)
            return cls.from_dict(collection_dict)

    def __repr__(self):
        return f"MyCollection({self.items})"


# Example usage:
def main():
    # Create a new collection and add some Game objects
    collection = MyCollection()
    collection.add(Game(level=1, score=100))
    collection.add(Game(level=2, score=200))

    # Save the collection to a file
    collection.save_state("collection.json")

    # Load the collection from the file
    loaded_collection = MyCollection.load_state("collection.json")
    print("Restored collection:", loaded_collection)

if __name__ == "__main__":
    main()
