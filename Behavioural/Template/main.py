from payment_flow import PaymentFlow, PaymentToFriend, PaymentToMerchant

if __name__ == '__main__':
    payment_to_friend: PaymentFlow = PaymentToFriend()
    payment_to_merchant: PaymentFlow = PaymentToMerchant()

    payment_to_friend.send_money(1000, "From Jitendra", "INR")
    payment_to_merchant.send_money(1000, "From Jitendra", "INR")
