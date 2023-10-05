# Dictionary
# The left element is the key, and the second one, is the key value
dictionary_of_names = {'Carlos': 19, 'Mariana': 14, 'Shock': 5}
print(dictionary_of_names)

# Accessing trough the key element
print(dictionary_of_names['Carlos'])

# Accessing using the get() method
print(dictionary_of_names.get('Shock'))

# Tuple

# Creating a tuple using simple values
my_name = ('Carlos', 'Reyes')
print('Tuple using string:', my_name)

# Creating a tuple using a list
list_of_names = ["Carlos", "Mariana", "Charly"]
tuple_of_list_of_names = tuple(list_of_names)
print('Tuple using a list', tuple_of_list_of_names)

# Accessing to the tuple elements using the index
print(my_name[0])
print(tuple_of_list_of_names[-1])


# Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # We first create an empty list
    simple_list = LinkedList()
    simple_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    simple_list.head.next = second

    # The next item after the list.head will be the second, so we define it like this, and we do so for the 3 element
    second.next = third

    simple_list.print_list()

'''
   After creating list.head, second, and third,
   Three nodes have been created.
   We have references to these three blocks as head,
   second and third

   list.head     second             third
       |             |                 |
       |             |                 |
   +----+------+     +----+------+     +----+------+
   | 1 | None  |     | 2 | None  |     | 3 | None  |
   +----+------+     +----+------+     +----+------+
'''


