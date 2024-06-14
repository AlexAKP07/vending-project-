class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.quantity} available)"

class VendingMachine:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for index, product in enumerate(self.products):
            print(f"{index + 1}. {product}")

    def select_product(self, product_number):
        if 0 < product_number <= len(self.products):
            return self.products[product_number - 1]
        else:
            print("Invalid selection.")
            return None

    def buy_product(self, product_number, money):
        product = self.select_product(product_number)
        if product:
            if product.quantity > 0:
                if money >= product.price:
                    product.quantity -= 1
                    change = money - product.price
                    print(f"Dispensing {product.name}. Your change is ${change:.2f}.")
                else:
                    print("Insufficient money. Transaction cancelled.")
            else:
                print(f"Sorry, {product.name} is out of stock.")

def main():
    vm = VendingMachine()
    vm.add_product(Product("Coca-Cola", 1.50, 40))
    vm.add_product(Product("Pepsi",1.50, 40))
    vm.add_product(Product("Lays Chips", 2.00, 20))
    vm.add_product(Product("Candy", 0.75, 30))
    vm.add_product(Product("Hershey", 3.00, 30))
    vm.add_product(Product("M&M",2.50, 30))
    vm.add_product(Product("Oreo",1.50, 30))
    while True:
        print("\nWelcome to the Vending Machine")
        print("1. Display Products")
        print("2. Buy a Product")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            vm.display_products()
        elif choice == "2":
            try:
                product_number = int(input("Enter product number: "))
                money = float(input("Enter money: "))
                vm.buy_product(product_number, money)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "3":
            print("Thank you for using the vending machine. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
