inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}


# get UPC from user, handling cases where the input is invalid with try/except
#TODO: Your code goes here
upc_number, disc, price, qty = 0, "None", 0, 0
new_data = []
while True:
    try:
        upc_number = int(input("Enter UPC number: "))
        disc = input("Enter item description: ")
        price = float(input("Enter unit price: "))
        qty = float(input("Enter item quantity: "))
        new_data = [disc, price, qty]
        break
    except Exception as Error:
        print("Unexpected exception: {0:}".format(Error))

# display message, either "updating" or creating" and then item is being updated display the `value` being updated
update = False
for key,value in inventory.items():
    if upc_number == key:
        # Update
        print("Updating item: {:}".format(inventory[upc_number]))
        update = True
        break
if not update:
    # Creating new
    print("New item, creating {:}".format(disc))
    inventory[upc_number] = new_data
else:
    # update dictionary entry
    inventory[upc_number] = new_data

# print header including
print("{:^10} | {:<20} | {:^15} | {:^10}".format("UPC", "Description", "Unit Price", "Quantity"))
print(65 * "-")

# print actual data from the dictionary (See Hint above)
for key,value in sorted(inventory.items()):
    print("{:^10} | {:<20} | {:^15.2f} | {:^10.2f}".format(key, value[0].upper(), value[1], value[2]))
print()
