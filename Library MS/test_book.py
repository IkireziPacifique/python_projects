#Author = Linda & Linda
import unittest


from item import Item


class TestBook(unittest.TestCase):
    def test_title(self):
        testtitle = Item('Nature', 'Documentary', 300, 5)
        self.assertEqual(testtitle.title, "Nature")
        
    def test_genre(self):
        testgenre = Item('The 100', 'Action', 100, 2)
        self.assertEqual(testgenre.genre, 'Action')
    
    def test_noitems(self):
        testnoitem = Item('The 100', 'Action', 300, 9)
        self.assertNotEqual(testnoitem.no_item, 10)
    
    def test_sellingprice(self):
        testsell = Item('The 100', 'Action', 1500, 5)
        self.assertEqual(testsell.selling_price, 1500)
 
    def testdonor(self):
        testauthor = Item('The 100', 'Action', 300, 5, 'Mary & Rose')
        self.assertEqual(testauthor.donor_name, 'Mary & Rose')

if __name__ == '__main__':
  unittest.main()
