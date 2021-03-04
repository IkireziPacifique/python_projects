#Author = Serge & Linda
# Calling the parent class
from item  import Item


class Film(Item):
    """ This a Film class with the initial Functions
"""
    def __init__(self, title, genre, selling_price, published_year, type, studios, no_item, donor_name=""):
        super().__init__(title, genre, selling_price, no_item, donor_name="")
        self.published_year = published_year
        self.type = type
        self.studios = studios
