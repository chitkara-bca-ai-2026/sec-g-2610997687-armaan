print("=" * 50)
print("          DATA CONVERSION UTILITY")
print("=" * 50)

# Taking input from user
product_name = input("Enter Product Name : ")
price = float(input("Enter Price       : "))
quantity = int(input("Enter Quantity    : "))

# Calculate total price
total_price = price * quantity

# Convert total amount into string
amount_str = str(total_price)

# Type Casting Summary
print("\n" + "=" * 50)
print("             TYPE CASTING SUMMARY")
print("=" * 50)

print("Variable       Value       Python Type")
print("-" * 50)

print("product_name  ", product_name, "   ", type(product_name))
print("price         ", price, "   ", type(price))
print("quantity      ", quantity, "   ", type(quantity))
print("total_price   ", total_price, "   ", type(total_price))
print("amount_str    ", amount_str, "   ", type(amount_str))

# Display Invoice
print("\n" + "=" * 50)
print("                 TAX INVOICE")
print("=" * 50)

print("Product Name   :", product_name)
print("Price per Unit : Rs.", price)
print("Quantity       :", quantity)
print("-" * 50)
print("Invoice Total  : Rs.", amount_str)

print("=" * 50)