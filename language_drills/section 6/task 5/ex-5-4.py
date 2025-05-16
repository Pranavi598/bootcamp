def calculate_total_price(prices):
    return sum(prices)

def main():
    item_prices = [10.5, 20, 30.25]
    total_price = calculate_total_price(item_prices)
    print("Total price:", total_price)

if __name__ == "__main__":
    main()
