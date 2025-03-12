filename = "sample_text.txt"

content = """Hello world!
This is a sample test file
it contains few lines of text."""

with open(filename, 'w') as file:
    file.write(content)
print(f"Content has beed written to {filename}")

with open(filename, 'r') as file:
    read_content = file.read()

print("Content read from file: ", read_content)


#task 2
import csv

filename = "people.csv"

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charley", "25", "Chicago"],
]

with open(filename, "w", newline="" ) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"DATA has been written to {filename}")

print("Reading DATA from file:", filename)
with open(filename, "r", newline="") as file:
    read_content = file.read()
    print("Content read from file is:\n", read_content)


#task 3

filename = "sample_text.txt"
additional_text = "This line is appended to the file.\n"

with open(filename, "a") as file:
    file.write(additional_text)
print(f"Additional text has been appended to {filename}")

with open(filename, "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)
