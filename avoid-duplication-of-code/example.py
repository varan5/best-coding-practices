# Avoid dulplication of code
# Use functions to group similar data together and one can use parameters to modify the required changes

# Duplication of code
print('Player 1 data')
print('My name is Varan')
print('My hobby is to play cricket')

print('Player 2 data')
print('My name is Karan')
print('My hobby is to play football')


# Using a function to avoid duplication
def print_player_information(number, name, hobby):
    print(f'Player {number} data')
    print(f'My name is {name}')
    print(f'My hobby is to {hobby}')