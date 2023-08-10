from observer_interface import NotificationObserver


class SMSNotificationObserver(NotificationObserver):

    def __init__(self, phone_number, observable):
        self.phone_number = phone_number
        self.observable = observable

    def update(self):
        message = "Hurry !! {0} is in stock.".format(self.observable.product_name)
        SMSNotificationObserver.send_sms(self.phone_number, message)

    @staticmethod
    def send_sms(phone_number, message):
        print('Sending sms notification to {0} containing message {1}'.format(phone_number, message))
