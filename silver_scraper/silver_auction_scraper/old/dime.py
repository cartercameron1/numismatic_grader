#dime class
#TODO create class includiding:
    #year
    #silver content
    #relevant functions

class Dime:

    #weight of pre 1964 dime in ounces
    silver_content = .07234

    def __init__(self, _year):
        self.year = _year

    def value(self, _spot_price):
        return self.silver_content * _spot_price

