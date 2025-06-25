# Create a Book Class

# Attributes:

# title, author, year.

# Method:

# get_description() — Returns a formatted description like:

# "The book 'Title' by Author was published in Year."

# Test it: Create a book and print its description.
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def description(self):
        print(f"Thee Book '{self.title}' by {self.author} was Published In {self.year}")        
t=input("Enter The Title Of Book:-")
a=input("Enter The Name Of Author:-")
y=int(input("Enter The Year Of Publication:-"))
b=Book(t,a,y)
b.description()