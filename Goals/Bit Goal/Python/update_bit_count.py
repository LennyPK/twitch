import os

amount = os.environ.get('AMOUNT')

# Specify the file path
file_path = 'bit_count.txt'

# Open the file in read mode to retrieve the existing number
with open(file_path, 'r') as file:
    existing_number = int(file.read().strip())

# Add the amount to the existing number
new_number = existing_number + int(amount)

# Open the file in write mode to update the number
with open(file_path, 'w') as file:
    file.write(str(new_number))

print(f"Existing number: {existing_number}")
print(f"Amount to add: {amount}")
print(f"New number: {new_number}")
