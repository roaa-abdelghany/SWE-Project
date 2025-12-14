
class Checkout:
    def __init__(self, shipping_address, Phone_number, payment_method , subtotal):
        self.shipping_address = shipping_address
        self.Phone_number = Phone_number
        self.payment_method = payment_method
        self.subtotal = float(subtotal)
    def order_summary(self):
        subtotal = self.subtotal
        shipping_fee = 50 if (subtotal < 500 and subtotal!=0) else 0
        total = subtotal + shipping_fee
        return{"Shipping Address": self.shipping_address, "Phone Number": self.Phone_number, "payment Method": self.payment_method,
            "subtotal": subtotal,
            "shipping_fee": shipping_fee,
            "total": total
        }