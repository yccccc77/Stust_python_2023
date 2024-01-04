# 定義員工類別
class Employee:
    def __init__(self, name, seniority, work_hours):
        # 初始化員工屬性
        self.name = name
        self.seniority = seniority
        self.work_hours = work_hours

    def get_name(self):
        # 取得員工名字
        return self.name

    def get_seniority(self):
        # 取得員工年資
        return self.seniority

    def get_work_hours(self):
        # 取得員工工作時數
        return self.work_hours

    def calculate_salary(self):
        # 假設每小時薪水為100元，計算月薪
        hourly_rate = 100
        return self.work_hours * hourly_rate

    def increase_work_hours(self, hours):
        # 增加員工工作時數
        self.work_hours += hours

    def increase_seniority(self, years):
        # 增加員工年資
        self.seniority += years


# 定義飲料類別
class Drink:
    def __init__(self, name, price, ice_level, sweetness):
        # 初始化飲料屬性
        self.name = name
        self.price = price
        self.ice_level = ice_level
        self.sweetness = sweetness

    def get_price(self):
        # 取得飲料價格
        return self.price

    def get_ice_level(self):
        # 取得飲料冰塊量
        return self.ice_level

    def get_sweetness(self):
        # 取得飲料甜度
        return self.sweetness

    def modify_name(self, new_name):
        # 修改飲料名稱
        self.name = new_name

    def adjust_sweetness(self, new_sweetness):
        # 調整飲料甜度
        self.sweetness = new_sweetness

    def adjust_price(self, new_price):
        # 調整飲料價格
        self.price = new_price


# 定義冷飲類別，繼承自飲料類別
class ColdDrink(Drink):
    def __init__(self, name, price, ice_level, sweetness):
        # 呼叫父類別的建構子初始化冷飲屬性
        super().__init__(name, price, ice_level, sweetness)


# 定義熱飲類別，繼承自飲料類別
class HotDrink(Drink):
    def __init__(self, name, sweetness):
        # 熱飲的價格和冰塊量為固定值，因此不需在建構子中傳遞，設定為0
        super().__init__(name, 0, 0, sweetness)


# 測試程式碼
employee1 = Employee("John", 5, 40)
print("Employee Name:", employee1.get_name())
print("Seniority:", employee1.get_seniority())
print("Work Hours:", employee1.get_work_hours())
print("Monthly Salary:", employee1.calculate_salary())

employee1.increase_work_hours(5)
employee1.increase_seniority(1)

print("Updated Work Hours:", employee1.get_work_hours())
print("Updated Seniority:", employee1.get_seniority())

drink1 = ColdDrink("Iced Coffee", 50, 3, 2)
print("\nDrink Name:", drink1.name)
print("Price:", drink1.get_price())
print("Ice Level:", drink1.get_ice_level())
print("Sweetness:", drink1.get_sweetness())

drink1.adjust_price(60)
drink1.modify_name("Iced Latte")

print("Updated Price:", drink1.get_price())
print("Updated Drink Name:", drink1.name)

hot_drink = HotDrink("Green Tea Latte", 3)
print("\nHot Drink Name:", hot_drink.name)
print("Sweetness:", hot_drink.get_sweetness())
