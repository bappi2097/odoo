class Computer:

    def __init__(self) -> None:
        self.__maxprice = 900
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price
    
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.set_max_price(1000)
c.sell()