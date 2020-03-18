'''Lab7.3'''

class Flower:
    '''Represents flower'''
    def __init__(self, color, quantity, price):
        '''
        Flower, str, int, int -> None
        Take colour of flower, quantity and price
        If price or quantity are negative or floats it convert them into positive ints
        '''
        self.color = color
        self.quantity = quantity
        self.price = price

        self.get_quantity()
        self.get_price()
        self.check_price()

    def get_price(self):
        '''
        Flower -> None
        Check price if it isn`t int/float set None for it
        '''
        try:
            self.price = abs(int(self.price))
        except (ValueError, TypeError):
            self.price = None

    def get_quantity(self):
        '''
        Flower -> None
        Check quantity if it isn`t int/float set None for it
        '''
        try:
            self.quantity = abs(int(self.quantity))
        except (ValueError, TypeError):
            self.quantity = None

    def check_price(self):
        '''
        Flower -> None
        If flower doesn`t have petals its trash, so it coast`s nothing
        '''
        if self.quantity == 0 and self.price > 0:
            self.price = 0

    def __eq__(self, other):
        '''
        Check if two flowers are same
        '''
        return bool(self.price == other.price and self.quantity == other.quantity \
        and self.color == other.color)

    def cut_price(self, season):
        '''
        If it isn`t season for flower its price is lower
        '''
        if season != 'high':
            self.price = self.price / 2

class Rose(Flower):
    '''Represents rose'''
    def __init__(self, color, quantity, price, season='high'):
        '''
        Rose, str, int, int, str -> None
        Inherits colour, quantity and price. Has special attribut - season
        '''
        super().__init__(color, quantity, price)
        self.name = 'rose'
        self.season = season
        self.cut_price(self.season)

class Tulip(Flower):
    '''Represents tulip'''
    def __init__(self, color, quantity, price, season='high'):
        '''
        Tulip, str, int, int, str -> None
        Inherits colour, quantity and price. Has special attribut - season
        '''
        super().__init__(color, quantity, price)
        self.name = 'tulip'
        self.season = season
        self.cut_price(self.season)

class Chamomile(Flower):
    '''Represents chamomile'''
    def __init__(self, color, quantity, price, season='high'):
        '''
        Chamomile, str, int, int, str -> None
        Inherits colour, quantity and price. Has special attribut - season
        '''
        super().__init__(color, quantity, price)
        self.name = 'chamomile'
        self.season = season
        self.cut_price(self.season)

class FlowerSet:
    '''Represents flowerset'''
    def __init__(self, flower, quantity):
        '''
        FlowerSet, Flower, int -> None
        Take object of class Flower and it amount
        '''
        self.flower = flower
        self.quantity = quantity
        self.flower_set = self.display_flowers()

    @property
    def get_price(self):
        '''
        FlowerSet -> None
        Multiply amount of flowers on their price and return price of flowerset
        '''
        price = self.flower.price * self.quantity
        return price

    def display_flowers(self):
        '''
        Display name and colour of flower as tuple and price of flowerset
        '''
        return (self.flower.name, self.flower.color), self.get_price

class Bucket:
    '''Represents bucket'''
    def __init__(self):
        '''
        Bucket -> None
        Set price of bucket and dict of flowerset
        '''
        self.price = 0
        self.flowers_dict = dict()

    def add_flower_set(self, flower_set):
        '''
        FlowerSet -> None
        Add flowerset to dictionary
        '''
        self.flowers_dict[flower_set.flower_set[0]] = flower_set.flower_set[1]

    @property
    def get_price(self):
        '''
        Bucket -> int
        Return price of bucket
        '''
        for price in self.flowers_dict.values():
            self.price += price
        return self.price
