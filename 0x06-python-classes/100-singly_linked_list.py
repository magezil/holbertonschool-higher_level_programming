#!/usr/bin/python3


class Node:
    """Node class is a node of a singly linked list"""
    
    def __init__(self, data, next_node=None):
        """Args:
                data: value of node
                next_node: next Node instance
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data: value of node

        setter validates value is type int

        Raises:
            TypeError: If data is not type int
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node: Node instance of next node in list

        setter validates next_node is valid

        Raises:
            TypeError: If next_node is not a Node instance or None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node and isinstance(value, Node):
            self.next_node = value
        else
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class is a singly linked list"""

    def __init__(self):
        """Initialize private instance variable to None (empty list)"""
        self.__head = None

    def __str__(self):
        """Retruns string version of singly linked list"""
        if not self.__head:
            return "" # return

    def sorted_insert(self, value):
