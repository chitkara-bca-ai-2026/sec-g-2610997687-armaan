print("=" * 40)
print("       CLOTHING STORE BILLING SYSTEM")
print("=" * 40)

# Accept customer details
customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# Calculate total cost
total_amount = price * quantity

# Display bill
print("\n" + "=" * 40)
print("                 BILL")
print("=" * 40)

print(f"Customer Name  : {customer_name}")
print(f"Garment Name   : {garment_name}")
print(f"Price per Unit : Rs. {price:.1f}")
print(f"Quantity       : {quantity}")
print(f"Total Amount   : Rs. {total_amount:.1f}")

print("=" * 40)