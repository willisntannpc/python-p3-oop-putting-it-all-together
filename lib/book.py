#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, genre={self.genre})"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    
        