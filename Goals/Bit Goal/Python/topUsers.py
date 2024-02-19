import os

filename = os.environ.get('FILENAME')

name_to_max_number = {}

# Read the file and update the maximum numbers for each name
with open(filename, 'r') as file:
    for line in file:
        parts = line.split()

        # Check if the line has enough parts
        if len(parts) >= 2:
            name = parts[0]
            # Extract the number within the brackets
            number = int(parts[1][1:-1])

             # Update the maximum number for each name
            if name not in name_to_max_number:
                name_to_max_number[name] = number
            else:
                name_to_max_number[name] += number  # Add to the existing number

# Remove the entry for "h3artworm" if it exists
if "h3artworm" in name_to_max_number:
    del name_to_max_number["h3artworm"]

# Sort names based on the highest numbers in descending order
sorted_names = sorted(name_to_max_number.keys(), key=lambda x: name_to_max_number[x], reverse=True)

# Write the sorted names back to the file
with open(filename, 'w') as file:
    for name in sorted_names:
        max_number = name_to_max_number[name]
        file.write(f"{name} ({max_number})\n")
