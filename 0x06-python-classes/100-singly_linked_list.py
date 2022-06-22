#!/usr/bin/python3

class Node:
    """Node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
         """Retrieves the data from the node."""
         return self.__data

    @data.setter
    def data(self, value):
         """Sets the data into a node."""
         if not isinstance(value, int):
             raise TypeError("data must be an integer")
         self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list.
    Private instance attribute: head.
    imple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):

