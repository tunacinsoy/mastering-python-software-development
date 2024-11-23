# FOR LOOP

my_list = [1, 2, 3, 4, 5]

for v in my_list:
    print(f" Just Values: {v}")
print()
# ---------------------------------------------------------------
# Get access to both index and value as you iterate
for i, v in enumerate(my_list):
    print(f"Index is: {i}, Value is: {v}")
print()
# ---------------------------------------------------------------
# Iterate 5 times, starting from 0 to 4 (both inclusively)
for i in range(5):
    print(i)
print()
# ---------------------------------------------------------------
# Iterate in reversed order
for i, v in enumerate(reversed(my_list)):
    print(f"This time in reversed order, both index and values: {5-i}, {v}")
print()

# ---------------------------------------------------------------
mydict = {"name": "Tuna", "surname": "Cinsoy", "age": 99, "city": "Warsaw"}

for k, v in mydict.items():
    print(f"Key {k} has value {v} in mydict.")
print()
# ---------------------------------------------------------------
# WHILE LOOP
count = 5
while count > 0:
    print(f" {count} people are happy!")
    count -= 1
