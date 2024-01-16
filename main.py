class Book:
    def __init__(self, title, pages, price):
        self.titles = title
        self.pages = pages
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price is negative")

kniha = Book("Matrix", 450, 10.9)
print(kniha.price)
kniha.price = 20
print(kniha.price)
kniha.price = -10
