# In Python, lists are a super useful data structure. They can hold multiple items that can be accessed via index and they can store a mix of data types. For example:

list = ['a', 'b', 'c', 1, 2, 3]

# Another benefit is that lists can nest other lists!

# A nested list is a list of lists. Yep, you read that right! It's called a nested list because one of the items is another list. For example:

list = ['a', 'b', 'c', [1, 2, 3]]
for i in range(len(list[3])):
    print(list[3][i])
    
# Matrix
# If we create a list of items, and every item is a nested list of the same size, we get what is called a matrix or 2D list (2-dimensional list).

# This is where nested lists become really handy:

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

#or it can also be written as
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
#or
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]

# Each item in the board list is a list of three items. This data is stored like how a table would organize its data into rows and columns. The inner lists are the rows while their items are the columns:

# board[0][0] board[0][1] board[0][2]
# board[1][0] board[1][1] board[1][2]
# board[2][0] board[2][1] board[2][2]

row = 2
column = 1

print(board[row][column])
# Output: x