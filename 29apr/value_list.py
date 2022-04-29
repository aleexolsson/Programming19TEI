import numpy

value_list = []

# Add a function to allow users to ask for help when they need to
def show_help():
    print('Enter a value: ')
    print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP' for additional info.
  Enter 'SHOW' to see your list
  """)

# Create a function that adds an item to the list
def add_to_list(item):
    value_list.append(item)
    print('{} was added to your list!'.format(item))
    print('You have {} items on your list.'.format(len(value_list)))


# Create a function to print all the items in the list
def show_list():
    print('My List:')
    for item in value_list:
        print(item)


show_help()

while True:
    new_item = input('> ')

    # If the user inputs 'DONE' exit the loop
    if new_item == 'DONE':
        break
    # If the user inputs 'HELP' show the help documentation
    elif new_item == 'HELP':
        show_help()
        continue
    # if the user inputs 'SHOW' show the list
    elif new_item == 'SHOW':
        show_list()
        continue

    # Call add_to_list with new item as an argument
    add_to_list(new_item)




show_list()
def Max_min(value_list):
    largest_number = 0
    for item in value_list:
        if item > largest_number:
            largest_number = item
    return largest_number
Max_min()
print('minimum value in the list is:', )