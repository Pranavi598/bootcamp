import yaml


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_yaml(self):
        # Convert the object to a dictionary and then to a YAML string
        return yaml.dump({
            'make': self.make,
            'model': self.model,
            'year': self.year
        })

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year})"


def main():
    car = Car("Toyota", "Camry", 2020)

    yaml_data = car.to_yaml()
    print("Serialized Car object to YAML:")
    print(yaml_data)

    # Save to file
    with open("car.yaml", "w") as f:
        f.write(yaml_data)


if __name__ == "__main__":
    main()
