# Task 25: Create base class LibraryItem with title.
# Create child classes Book, Magazine, DVD with extra attributes.
# Each class has a display() method.

class LibraryItem:
    def __init__(self, title):
        self.title = title
    def display(self):
        print("Title:", self.title)

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    def display(self):
        super().display()
        print("Author:", self.author)

class Magazine(LibraryItem):
    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue
    def display(self):
        super().display()
        print("Issue:", self.issue)

class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
    def display(self):
        super().display()
        print("Duration:", self.duration)

items = [Book("Python", "Guido"), Magazine("Science", 45), DVD("Inception", "2h")]
for item in items:
    item.display()
