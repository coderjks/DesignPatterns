from observable import StocksObservable


class IphoneObservable(StocksObservable):

    def __init__(self, product_name, stock=0):
        self.product_name = product_name
        self.stock = stock
        self.observers = list()

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify_subscribers(self):
        for observer in self.observers:
            observer.update()

    def set_stock(self, stock_count):
        if self.stock == 0:
            self.notify_subscribers()
        self.stock = stock_count

    def get_stock(self):
        return self.stock
