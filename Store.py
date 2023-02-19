class fruit:
    def __init__(self, name, color, time_in_days, price, quantity):
        self.name = name
        self.color = color
        self.time_in_days = time_in_days
        self.price = price
        self.quantity = quantity

    def sale(self):
        new_price = self.price
        if self.time_in_days > 3:
            new_price = new_price/2
            print("Today, {name} is at $".format(name = self.name) + str(new_price))
        else:
            print("The best {name} is available at ${price}".format(name = self.name, price = self.price))
    
    def purchase(self, amount_sale):
        if amount_sale > self.quantity:
            print("Error, there are not enough {name} to sell").format(name= self.name)
        else:
            update_quantity = self.quantity - amount_sale
            print("Now there are " + str(update_quantity) + " {name} in the stock".format(name = self.name))

    def __repr__(self):
        return "the {name} is a fruit of color {color}, have {time_in_days} days, you can purchase for ${price}, {quantity} units in stock".format(name = self.name, color = self.color, time_in_days = self.time_in_days, price = self.price, quantity = self.quantity)

    
class drinks:
    def __init__(self, name, type_of_package, content, days_to_expire_date, price, need_refrigeration = True):
        self.name = name
        self.type_of_package = type_of_package
        self.content = content
        self.days_to_expire_date = days_to_expire_date
        self.price = price
        self.need_refrigeretion = need_refrigeration

    def sale(self):
        new_price = self.price
        if self.days_to_expire_date < 2:
            new_price = new_price/3
            print("Today, {name} is at $".format(name = self.name) + str(new_price))
        else:
            print("The best {name} is available at ${price}".format(name = self.name, price = self.price))
    
    def storage(self):
        if self.need_refrigeretion:
            print("Hey, take care, this product {name} need refrigeration, harry up and put in the refrigerator".format(name = self.name))
        else:
            print("You can drink {name} now if you want jajajaja".format(name = self.name))


    def __repr__(self):
        return "the {name} is a drink in presentation of {type_of_package}, have {content} mililiters, and expire in {days_to_expire_date} days, you can purchase for ${price}".format(name = self.name, type_of_package = self.type_of_package, content = self.content, days_to_expire_date = self.days_to_expire_date, price = self.price)

fruit_one = fruit("apple", "green", 4, 2, 20)
fruit_one.sale()
fruit_one.purchase(5)
print(fruit_one)

drink_one = drinks("milk", "box", 1000, 1, 5)
drink_one.sale()
drink_one.storage()
print(drink_one)