def get_stock(fruit):
    """
    Returns the number of the given fruit in Sophia's inventory.
    """
    inventory = {
        "apple": 50,
        "banana": 25,
        "pear": 1000,
        "orange": 30
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit_name = input("Enter a fruit: ")
    count = get_stock(fruit_name)
    if count > 0:
        print(f"The fruit is in stock! Quantity: {count}")
    else:
        print("The fruit is not in stock.")

if __name__ == '__main__':
    main()
