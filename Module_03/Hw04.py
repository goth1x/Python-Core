def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price -= price * discount

    apply_discount()
    return price

print(discount_price(float(input('Cost of product ')), (float(input('Discount \'from 0 to 1\' ')))))