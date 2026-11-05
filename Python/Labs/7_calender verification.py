print("=" * 40)
print("      CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

# Take input from the user
year = int(input("Enter year: "))

# Validate the input
if year <= 0:
    print("Error: Please enter a positive year.")
else:
    # Check leap year
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
        feb_days = 29
        total_days = 366

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
        feb_days = 28
        total_days = 365

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
        feb_days = 29
        total_days = 366

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
        feb_days = 28
        total_days = 365

    # Display results
    print("\n" + "=" * 40)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", total_days, "days")
    print("Days in February:", feb_days, "days")
    print("Reason:", reason)
    print("=" * 40)