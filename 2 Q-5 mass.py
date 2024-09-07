# Conversion factors
LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

# Ask the user for the mass in medieval units
talents = int(input("Enter the number of talents (leiviskä): "))
pounds = int(input("Enter the number of pounds (naula): "))
lots = float(input("Enter the number of lots (luoti): "))

# Convert everything to grams
total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

# Convert grams to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Print the result
print(f"The equivalent mass is {kilograms} kilograms and {grams:.1f} grams.")
