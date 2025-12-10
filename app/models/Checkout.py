class Checkout:
    def __init__(self, shipping_address, Phone_number, payment_method , items):
        self.shipping_address = shipping_address
        self.Phone_number = Phone_number
        self.payment_method = payment_method
        self.items = items
    def order_summary(self):
        subtotal = sum(item.price * item.quantity for item in self.items)
        shipping_fee = 50 if subtotal < 100 else 0
        total = subtotal + shipping_fee
        return{
            "Shipping Address": self.shipping_address,
            "Phone Number": self.Phone_number, 
            "payment Method": self.payment_method,
            "subtotal": subtotal,
            "shipping_fee": shipping_fee,
            "total": total
        }