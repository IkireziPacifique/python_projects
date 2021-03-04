#Author = Serge & Linda
# Creating a class
class Item():
    """ This a Item class  with  the initial functions
"""
    def __init__(self, title, genre, selling_price, no_item, donor_name=""):
        self.title = title
        self.genre = genre
        self.selling_price = selling_price
        self.no_item = no_item
        self.donor_name = donor_name
    
    """ This method sell allows to sell Item
"""

    def sell(self):
        Item_needed = input(" Choose the Item you want to buy:  ")
        print('The price is ' + str(self.selling_price))
        self.no_item -= 1
        print('Item Sold')
        
    """ This Lend method allows to lend Item
"""
    def lend(self):
        Item_needed = input(" Choose the Item you want to buy:  ")
        print('Lending ' + self.title)
        self.no_item -= 1
        print('Item Lended')
        
    """ This View method allow to view Item in the Library
"""
    
    def View(self):
        print(" ==== Item Viewed ====")
        

