class FriedChicken:
    def __init__(self, name, flavor, crispy_level, size, price):
        # Constructor（建構子）：初始化物件屬性
        self.name = name
        self.flavor = flavor
        self.crispy_level = crispy_level
        self.size = size
        self.price = price

    def display_info(self):
        # 顯示炸雞的屬性資訊
        print(f"Name: {self.name}")
        print(f"Flavor: {self.flavor}")
        print(f"Crispy Level: {self.crispy_level}")
        print(f"Size: {self.size}")
        print(f"Price: {self.price}")

    def increase_crispiness(self, amount):
        # 增加炸雞的脆度屬性
        self.crispy_level += amount
        print(f"Crispy level increased by {amount}.")

    def change_flavor(self, new_flavor):
        # 更改炸雞的風味屬性
        self.flavor = new_flavor
        print(f"Flavor changed to {new_flavor}.")

    def calculate_discounted_price(self, discount_percent):
        # 計算折扣後的價格
        discounted_price = self.price - (self.price * discount_percent / 100)
        print(f"Discounted Price: {discounted_price}")

# 建立四個炸雞物件
chicken1 = FriedChicken("Original", "Spicy", 5, "Large", 50)
chicken2 = FriedChicken("BBQ", "Sweet", 3, "Medium", 40)
chicken3 = FriedChicken("Honey Mustard", "Mild", 4, "Small", 30)
chicken4 = FriedChicken("Teriyaki", "Savory", 2, "Extra Large", 60)

# 分別呼叫三個副函式
chicken1.display_info()
chicken1.increase_crispiness(2)
chicken1.calculate_discounted_price(10)

print("\n")

chicken2.display_info()
chicken2.change_flavor("Sour")
chicken2.calculate_discounted_price(15)

print("\n")

chicken3.display_info()
chicken3.increase_crispiness(1)
chicken3.calculate_discounted_price(5)

print("\n")

chicken4.display_info()
chicken4.change_flavor("Spicy Garlic")
chicken4.calculate_discounted_price(20)
