import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestSquare(unittest.TestCase):
    '''Test for class Flower'''
    def setUp(self):
        '''Create test objects'''
        self.alyssum = Flower('yellow', -4, 20.5) #All negative integers will be change into positive and all floats will be convert into ints
        self.tulip = Tulip('pink', 5, 120)
        self.rose = Rose('black', 10, 150)
        self.rose2 = Rose('yellow', 5, 200, 'hulthemia')
        self.rose3 = Rose.create_rose(175)
        self.chamomile = Chamomile('white', 20, 30, True)
        self.flowerset1 = FlowerSet([self.alyssum, self.tulip, self.rose2])
        self.flowerset2 = FlowerSet()
        self.bucket1 = Bucket([self.flowerset1, self.flowerset2])
        self.bucket2 = Bucket()

    def test_init(self):
        '''Test method init which take 3 attributes: colour of flower (str),
        amount of its petals (int) and its price (int).
        Tulip has special attribute - ribbon, which is bool,
        Rose special attribute - species (Hulthemia, Hesperrhodos, Rosa, etc), which is string,
        Chamonile has special attribute - wild, which is bool'''
        #Lets test some exceptions(when user gives wrong type attributes)
        #Exception for colour
        with self.assertRaises(Exception) as context:
            Flower(4500, 1, 50)
        self.assertTrue('Flower.colour must be an str' in str(context.exception))

        #Exception for petals and price
        with self.assertRaises(Exception) as context:
            Flower('yellow', 'one', 50)
        self.assertTrue('Flower.petals must be an int' in str(context.exception))
        with self.assertRaises(Exception) as context:
            Flower('yellow', 5, True)
        self.assertTrue('Flower.price must be an int' in str(context.exception))

        #Check if user write all values
        self.assertEqual((self.alyssum.colour, self.alyssum.petals, self.alyssum.price),
        ('yellow', 4, 20), "Enter all values!")
        
        #Shows what classmethod create_rose does
        self.assertEqual((self.rose3.colour, self.rose3.petals, self.rose3.price, self.rose3.species),
        ('red', 40, 175, 'hulthemia'))
        
        #Colour shoul be a string
        self.assertIsInstance(self.alyssum.colour, str, "Colour shoul be a string!")

        #Amount of petals and price should be integers, also they can't be negative or
        #equal to zero
        self.assertIsInstance(self.alyssum.petals, int, "Value is not an integer!")
        self.assertIsInstance(self.alyssum.price, int, "Value is not an integer!")
        self.assertEqual(self.alyssum.price, 20) #All floats will be convert into integers 
        self.assertGreaterEqual(self.alyssum.price, 0, "Value should be a positive integer!")
        self.assertGreaterEqual(self.alyssum.petals, 0, "Value should be a positive integer!")

        #Tulip, Rose, Chamomile are child classes of Flower
        self.assertIsInstance(self.tulip, Flower)
        self.assertIsInstance(self.tulip, Tulip)
        self.assertIsInstance(self.rose, Flower)
        self.assertIsInstance(self.rose, Rose)
        self.assertIsInstance(self.chamomile, Flower)
        self.assertIsInstance(self.chamomile, Chamomile)

        #Check additional attributes of child classes
        self.assertEqual(self.tulip.ribbon, False)
        self.assertEqual(self.rose.species, 'rosa')
        self.assertEqual(self.rose2.species, 'hulthemia')
        self.assertEqual(self.chamomile.wild, True)
    
    def test_flowerset(self):
        '''Test for methods of class Flowerset'''
        #This class has only one attribute, which is list
        self.assertIsInstance(self.flowerset1, FlowerSet)
        self.assertIsInstance(self.flowerset1.flowers, list)
        self.assertEqual(self.flowerset2.flowers, [])

        #Also it has method to add more flowers
        self.flowerset2.get_flower(self.rose)
        self.assertEqual(self.flowerset2.flowers, [self.rose])
        self.assertIsInstance(self.flowerset1.flowers[0], Flower)
        #You may also add list of flowers
        self.flowerset2.get_flower([self.tulip, self.chamomile])
        self.assertEqual(self.flowerset2.flowers, [self.rose, self.tulip, self.chamomile])

        #You can count price of flowerset
        self.assertEqual(self.flowerset1.price(), 340)

    def test_bucket(self):
        '''Test methods of class bucket'''
        #Check attribute of class Bucket
        self.assertIsInstance(self.bucket1, Bucket)
        self.assertIsInstance(self.bucket2.sets, list)
        self.assertEqual(self.bucket1.sets, [self.flowerset1, self.flowerset2])
        self.assertEqual(self.bucket2.sets, [])

        #You can add sets to your bucker (one flowerset or list of them)
        self.bucket1.get_set(self.flowerset1)
        self.bucket2.get_set([self.flowerset1, self.flowerset2])
        self.assertEqual(self.bucket1.sets, [self.flowerset1, self.flowerset2, self.flowerset1])
        self.assertEqual(self.bucket2.sets, [self.flowerset1, self.flowerset2])
        self.assertIn(self.flowerset1, self.bucket1.sets)

        #You can count price of bucket
        self.assertEqual(self.bucket1.price(), 680)

        #Also class Bucket has staticmethod which check(by price) if your girlfriend will like this bucket
        self.assertEqual(Bucket.girlfriend(300), True)
        self.assertEqual(Bucket.girlfriend(299), False)

if __name__ == "__main__":
    unittest.main()
