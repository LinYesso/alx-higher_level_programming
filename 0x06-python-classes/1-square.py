#!/usr/bin/python3
class Square:
    """That represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data size."""
        self.__size = size
