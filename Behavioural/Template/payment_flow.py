class PaymentFlow:

    def validate_request(self, request):
        pass

    def debit_money(self, amount):
        pass

    def credit_money(self, amount):
        pass

    def calculate_transaction_fee(self, amount, currency):
        pass

    def send_money(self, amount, request, currency):
        """
        This is a template to carry out send money operation using the above tasks in an order.
        """
        self.validate_request(request)
        self.debit_money(amount)
        self.calculate_transaction_fee(amount, currency)
        self.credit_money(amount)


class PaymentToFriend(PaymentFlow):
    """
    This class has its own logic for calculating transaction fees.
    """

    def validate_request(self, request):
        print("Request validated. Success!!")

    def debit_money(self, amount):
        print(f"Amount debited: {str(amount)}")

    def credit_money(self, amount):
        print(f"Amount credited: {str(amount)}")

    def calculate_transaction_fee(self, amount, currency):
        fees = 0 * amount
        print(f"Transaction fees: {currency} {str(fees)}")


class PaymentToMerchant(PaymentFlow):
    """
    This class has its own logic for calculating transaction fees.
    """

    def validate_request(self, request):
        print("Request validated. Success!!")

    def debit_money(self, amount):
        print(f"Amount debited: {str(amount)}")

    def credit_money(self, amount):
        print(f"Amount credited: {str(amount)}")

    def calculate_transaction_fee(self, amount, currency):
        fees = (10 * amount) // 100
        print(f"Transaction fees: {currency} {str(fees)}")
