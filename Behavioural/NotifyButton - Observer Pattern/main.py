from iphone_observable import IphoneObservable
from email_observer import EmailNotificationObserver
from message_observer import SMSNotificationObserver


if __name__ == "__main__":
    iphone_stock = IphoneObservable('Iphone 15', 5)
    observer1 = EmailNotificationObserver('xya@gmail.com', iphone_stock)
    observer2 = SMSNotificationObserver('9601055029', iphone_stock)
    observer3 = EmailNotificationObserver('Sasdfa@gmmail.com', iphone_stock)

    iphone_stock.add(observer1)
    iphone_stock.add(observer2)
    iphone_stock.add(observer3)

    iphone_stock.set_stock(0)
    iphone_stock.set_stock(10)
