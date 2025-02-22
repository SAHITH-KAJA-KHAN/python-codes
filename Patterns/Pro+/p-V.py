'''   **********
      ****  ****
      ***    ***
      **      **
      *        *
      *        *
      **      **
      ***    ***
      ****  ****
      **********   '''
n = 5

# # Upper part
# for i in range(n, 0, -1):  # Rows from 5 to 1
#     for j in range(i):  # Print left stars
#         print('*', end='')
#     for j in range(2 * (n - i)):  # Print spaces
#         print(' ', end='')
#     for j in range(i):  # Print right stars
#         print('*', end='')
#     print()  # Move to the next line

# Lower part
# for i in range(1, n + 1):  # Rows from 1 to 5
#     for j in range(i):  # Print left stars
#         print('*', end='')
#     for j in range(2 * (n - i)):  # Print spaces
#         print(' ', end='')
#     for j in range(i):  # Print right stars
#         print('*', end='')
#     print()  # Move to the next line


# n = 5

for i in range(1, 2 * n):  # Loop for rows from 1 to 9 (2*n - 1)
    stars = n - abs(n - i)  # Number of stars on each side
    spaces = 2 * abs(n - i)  # Number of spaces in the middle

    print('*' * stars + ' ' * spaces + '*' * stars)

