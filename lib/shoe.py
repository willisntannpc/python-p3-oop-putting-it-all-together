#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def __repr__(self):
        return f"Shoe(brand={self.brand}, size={self.size}, color={self.color})"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value <= 0:
            raise ValueError("Size must be positive")
        self._size = value
