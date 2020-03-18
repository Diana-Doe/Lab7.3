import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestFlowers(unittest.TestCase):
    """
    Represents test methods for Flower class
    """
    def test_flower_attributes(self):
        """
        Tests Flower class attributes
        """
        # Test attribute types
        flower = Flower('yellow', '23', '250')
        self.assertEqual(flower.quantity, 23)
        self.assertIsInstance(flower.color, str)
        self.assertIsInstance(flower.price, int)

        # Price can not be set for 0 quantity
        flower = Flower('yellow', 0, 120)
        self.assertEqual(flower.price, 0)

        # Price and Quantity should not be negative
        flower = Flower('yellow', -10, -120)
        self.assertEqual(flower, Flower('yellow', 10, 120))

        # Price and Quantity should be only digits
        flower = Flower('yellow', 'ten', 'one twenty')
        self.assertEqual(flower, Flower('yellow', None, None))

    def test_flowers(self):
        """
        Test Rose Tulip and Chamomile classes
        """
        # Test Rose class
        # 4th attribute is season. When season is low,
        # the price is twice lower then in high season
        # season = 'high' should be set by default
        rose = Rose('red', 10, 150, 'low')
        self.assertEqual(rose, Rose('red', 10, '75'))
        self.assertIsInstance(rose, Flower)

        # Test Tulip class
        tulip = Tulip('red', -10, -150, 'low')
        self.assertEqual(tulip, Tulip('red', 10, 75))

        # Test Chamomile class
        chamomile = Chamomile('blue', 'ten', -150, 'high')
        self.assertEqual(chamomile, Chamomile('blue', None, 150))

    def test_flower_set(self):
        """
        Test FlowerSet class
        """
        rose = Rose('red', 10, 15)
        flowers = FlowerSet(rose, 101)

        self.assertEqual(flowers.display_flowers(), (('rose', 'red'), 1515))
        self.assertEqual(flowers.get_price, 1515)

    def test_bucket(self):
        """
        Test Bucket class
        """
        rose = Rose('red', 10, 15)
        rose2 = Rose('white', 12, 12)

        flowers = FlowerSet(rose, 51)
        flowers2 = FlowerSet(rose2, 50)

        # Test for Bucket functionality
        bucket = Bucket()
        bucket.add_flower_set(flowers)
        bucket.add_flower_set(flowers2)

        self.assertEqual(bucket.get_price, 1365)
        self.assertEqual(bucket.flowers_dict, {('rose', 'red'): 765, ('rose', 'white'): 600})


if __name__ == "__main__":
    unittest.main()
