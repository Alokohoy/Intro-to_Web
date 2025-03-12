numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()

print( numbers)

#task 2

print("First 3 elements:", numbers[:3])
print("Last 2 elements:", numbers[-2:])
print("List in reverse order:", numbers[::-1])\

#task 3

student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
del student["age"]
print(student.items())
print(student.keys())
print(student.values())

#task 4

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union of sets:", union)

intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)

difference = set1.difference(set2)
print("Difference of sets (set1 - set2):", difference)

#task 5

colors = ("red", "blue", "green", "red", "yellow")

index_of_green = colors.index("green")
print("Index of 'green':", index_of_green)
count_red = colors.count("red")
print("Count of 'red':", count_red)

#task 6

company = {
    "employees": [
        {"name": "Alice", "position": "Developer", "salary": 50000},
        {"name": "Bob", "position": "Webdev", "salary": 40000}
    ]
}

company["employees"].append({"name": "Charlie", "position": "Designer", "salary": 60000})

for employee in company["employees"]:
    print(employee["name"])





