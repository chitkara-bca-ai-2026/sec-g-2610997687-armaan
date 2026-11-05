import math

print("=" * 45)
print("       ENGINEERING CALCULATION TOOL")
print("=" * 45)

# Accept numerical value
value = float(input("Enter a numerical value: "))

# Accept exponent
exponent = float(input("Enter an exponent: "))

# Accept decimal measurement
decimal_value = float(input("Enter a decimal measurement: "))

# Perform calculations
power = math.pow(value, exponent)
square_root = math.sqrt(value)
ceil_value = math.ceil(decimal_value)
floor_value = math.floor(decimal_value)

# Display results
print("\n--- Results ---")
print(f"Value                 : {value}")
print(f"Exponent              : {exponent}")
print(f"Power (pow)           : {power}")
print(f"Square Root (sqrt)    : {square_root:.4f}")
print(f"Decimal Value         : {decimal_value}")
print(f"Ceil Value            : {ceil_value}")
print(f"Floor Value           : {floor_value}")

print("=" * 45)