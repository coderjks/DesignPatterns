from observer_interface import NotificationObserver


class EmailNotificationObserver(NotificationObserver):

    def __init__(self, email, observable):
        self.email = email
        self.observable = observable

    def update(self):
        message = "Hurry !! {0} is in stock.".format(self.observable.product_name)
        EmailNotificationObserver.send_email(self.email, message)

    @staticmethod
    def send_email(email, message):
        print('Sending email to {0} containing message {1}'.format(email, message))
