#Author = Serge & Linda
# Calling the parent class
from item import Item

class Audiobook(Item):
    """ This an Audiobook Class with the initial Function
"""
    def __init__(self, title, genre, selling_price, author_name, published_year, format, no_item, donor_name=""):
        super().__init__(title, genre, selling_price, no_item, donor_name="")
        self.author_name = author_name
        self.published_year = published_year
        self.format = format
    

