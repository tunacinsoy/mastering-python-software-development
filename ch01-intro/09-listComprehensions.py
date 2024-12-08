squares = [x**2 for x in range(1, 11)]
print(squares)

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)


# We want to print the elements of matrix in flattened version
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# Option #1
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)

# Option #2
for row in matrix:
    for num in row:
        print(num)

# Option #3
i = 0
j = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j])


# We want to initialize a dictionary
# Option #1
squares_dict = {x: x**2 for x in range(0, 5)}
print(squares_dict)

squares_dict = {}
# Option #2
for x in range(0, 5):
    squares_dict[x] = x**2


# We want initialize a set variable to hold the lengths of these words
words = ["hello", "world", "python", "programming"]

# Option #1
unique_lengths = {len(word) for word in words}
print(unique_lengths)

# Option #2
unique_lengths = set()
for word in words:
    unique_lengths.add(len(word))
print(unique_lengths)


# Some testing, unrelated to file content
test = {1: "a", 2: "b", 3: "c"}
print(type(test))  # dict

test = {1, 2, 2}
print(type(test))  # set
print(len(test))  # 2
print(test)  # {1, 2}
