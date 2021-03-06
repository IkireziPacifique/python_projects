#Author = Serge & Linda
import unittest



from item import Item


class TestAudiobook(unittest.TestCase):
    def test_title(self):
        testtitle = Item('The 100', 'Action', 300, 5)
        self.assertEqual(testtitle.title, "The 100")
        
    def test_genre(self):
        testgenre = Item('The 100', 'Action', 300, 5)
        self.assertEqual(testgenre.genre, 'Action')
    
    def test_noitems(self):
        testnoitem = Item('The 100', 'Action', 300, 5)
        self.assertNotEqual(testnoitem.no_item, 10)
    
    def test_sellingprice(self):
        testsell = Item('The 100', 'Action', 300, 5)
        self.assertEqual(testsell.selling_price, 300)
 
    def testdonor(self):
        testauthor = Item('The 100', 'Action', 300, 5, 'Mary')
        self.assertEqual(testauthor.donor_name, 'Mary')

if __name__ == '__main__':
  unittest.main()
