  # Create an empty list called my_list.
my_list = []

  # Append the following elements to my_list: 10, 20, 30, 40.
my_list = [10, 20, 30, 40]
print(my_list)

  # Insert the value 15 at the second position in the list.
my_list.append(15)
print("After Append:" , my_list)

  # Extend my_list with another list: [50, 60, 70].
my_list = [10, 20, 30, 40]
print("List1:" , my_list)

even_numbers = [50, 60, 70]
print("List2:" , even_numbers)

my_list.extend(even_numbers)

print("List after append:" , my_list)

  # Remove the last element from my_list.
my_list = [10, 20, 30, 40]
my_list.remove(40)
print(my_list)

  # Sort my_list in ascending order.
my_list = [10, 20, 30, 40]

  # Find and print the index of the value 30 in my_list.
my_list = [10, 20, 30, 40]
print(my_list[2])