# ========The beginning of the class==========

# Class representing a shoe in the inventory.
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initialise the shoe attributes.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Return the cost of the shoe.
    def get_cost(self):
        return self.cost

    # Return the quantity of the shoe.
    def get_quantity(self):
        return self.quantity

    # Return a string representation of a shoe object.
    def __str__(self):
        return (
            f"Country: {self.country} | "
            f"Code: {self.code} | "
            f"Product: {self.product} | "
            f"Cost: {self.cost} | "
            f"Quantity: {self.quantity}"
        )


# =============Shoe list===========

# List used to store all Shoe objects.
shoe_list = []


# ==========Functions outside the class==============


# Read shoe data from inventory.txt and store it in shoe_list.
def read_shoes_data():
    try:
        # Open the inventory file.
        file = open("inventory.txt", "r")

        next(file)  # Skip the header line

        # Read each line and create a Shoe object.
        for line in file:
            country, code, product, cost, quantity = line.strip().split(",")
            shoe = Shoe(country, code, product, int(cost), int(quantity))
            shoe_list.append(shoe)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")


# Capture a new shoe from the user and save it.
def capture_shoes():
    # Ask the user for the shoe details.
    try:
        country = input("Enter shoe country: ")
        code = input("Enter shoe code: ")
        product = input("Enter shoe product: ")
        cost = int(input("Enter shoe cost: "))
        quantity = int(input("Enter shoe quantity: "))

        # Create a new Shoe object and add it to the list.
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        # Update the inventory file with the new shoe.
        file = open("inventory.txt", "w")
        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )

        file.close()
        print("Shoe added successfully.")

    except ValueError:
        print("Error: Invalid input. Cost and quantity must be in numbers.")


# Display all shoes in the inventory.
def view_all():
    for shoe in shoe_list:
        print(shoe)
        print()


# Find the shoe with the lowest quantity and update its stock.
def re_stock():
    # Find the shoe with the smallest quantity.
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the lowest quantity is:\n{lowest_quantity_shoe}")

    answer = (
        input("Do you want to add more quantity for this shoe? (yes/no): ")
        .strip()
        .lower()
    )

    if answer == "yes":
        try:
            additional_quantity = int(input("How many shoes would you like to add? "))
            # Increase the quantity of the selected shoe.
            lowest_quantity_shoe.quantity += additional_quantity

            # Save the updated inventory back to the file.
            file = open("inventory.txt", "w")
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
            file.close()

            print("Quantity updated successfully.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    else:
        print("No changes were made to the inventory.")


# Search for a shoe using its code.
def search_shoe():
    code = input("Enter shoe code to search: ")
    # Check each shoe until a matching code is found.
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"Shoe found:\n{shoe}")
            return
    print("Shoe not found.")


# Calculate and display the total value of each shoe.
def value_per_item():
    for shoe in shoe_list:
        # Calculate value = cost × quantity.
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Product: {shoe.product}, Total Value: {value}")


# Display the shoe with the highest quantity as being on sale.
def highest_qty():
    highest_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print("=== FOR SALE ===")
    print(f"{highest_quantity_shoe}\nThis shoe is now for sale!")


# ==========Main Menu=============

# Load all shoes from the inventory file before displaying the menu.
read_shoes_data()

# Keep showing the menu until the user chooses to exit.
while True:
    # Display the menu and get the user's choice.
    choice = input(
        "Choose an option:\n"
        "1. View all shoes\n"
        "2. Capture new shoe\n"
        "3. Search shoe\n"
        "4. Re-stock shoe\n"
        "5. View value per item\n"
        "6. View shoe with highest quantity\n"
        "0. Exit\n"
        "Enter your choice: "
    )

    if choice == "1":
        view_all()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        search_shoe()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
