class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name, str(self.start_time).replace("00", ":00"), str(self.end_time).replace("00", ":00"))

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_to_order = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_to_order.append(menu)
    return available_to_order

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# make class instances
brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)
early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)
dinner = Menu("dinner", { 'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)
arepas_menu = Menu("arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 1000, 2000)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [arepas_place])


# tests
print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# print(flagship_store.menus)
print(flagship_store.available_menus(2000))
print(flagship_store.available_menus(1700))
print(business.franchises)
print(new_business.franchises[0].menus[0].calculate_bill(['pernil arepa']))
# print(arepas_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))


