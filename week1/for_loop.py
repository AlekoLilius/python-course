# for i in range(10):
#     double = i*2
#     print(double)

# print('End of Code')

# Nested loop
# for i in range(11): # row
#     for j in range(11): # column
#         print(i * j, end=' ')
#     print()

#
##
###
####

# for i in range(1, 5):
#     print(i * '#')

# for i in range(1, 5):
#     for j in range(i):
#         print('#', end='')
#     print()

# for _ in range(10):
#     print('*', end='-')
# print()

#
##
###
##
#

for i in range(3):
    for j in range(i+1):
        print('#', end='')
    print()

for i in range(1, -1, -1):
    for j in range(i+1):
        print('#', end='')
    print()