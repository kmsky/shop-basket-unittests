class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __hash__(self):
        return hash((self.name, self.price))


    def __eq__(self, other):
        return (self.name, self.price) == (other.name, other.price)


    def __repr__(self):
        return "Item({}, {})".format(self.name, self.price)


class Basket:
    def __init__(self):
        self.basket = {}


    def add(self, product, amount=1):
        if amount > 0:
            if product in self.basket:
                already_in = self.basket.get(product)
                self.basket[product] = already_in + amount

            else:
                self.basket[product] = amount
        else:
            return "Can't add this amount of products"

        return self.basket


    def delete(self, product, amount=1):
        try:
            if amount < self.basket.get(product):
                already_in = self.basket.get(product)
                self.basket[product] = already_in - amount

            elif amount == self.basket.get(product):
                self.basket.pop(product)

            else:
                return "Not enough products in basket"

            return self.basket

        except TypeError:
            return "Object was not added to basket"


    def sum_price(self):
        summary = 0
        for product, amount in self.basket.items():
            summary += product.price * amount

        return summary


    def print_content(self):
        for product, amount in self.basket.items():
            print("{} {} PLN, quantity: {} = {}".format(product.name, product.price, amount, product.price * amount))
        print("------------------------------------")
        print("= {}".format(self.sum_price()))
