def validate_args(func):
    """Decorator to validate arguments for class methods"""
    def wrapper(self, *args, **kwargs):
        if any(arg <= 0 for arg in args):
            raise ValueError("Arguments must be greater than zero")
        return func(self, *args, **kwargs)
    return wrapper

class Product:
    @validate_args
    def set_price(self, price):
        self.price = price
        print(f"Price set to {self.price}")

def main():
    product = Product()
    product.set_price(100)  # Works
    product.set_price(-50)  # Raises ValueError

if __name__ == "__main__":
    main()
