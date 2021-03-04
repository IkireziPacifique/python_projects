from item import Item


# Creating a child class
class Book(Item):
	def __init__(self, title, genre, selling_price, author_name, published_year, no_item, donor_name=""):
		super().__init__(title, genre, selling_price, no_item, donor_name="")
		self.author_name = author_name
		self.published_year = published_year


