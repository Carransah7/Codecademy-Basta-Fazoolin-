class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  def availableMenus(self, time):
    availableMenus = []
    for menu in self.menus:
      if time >= menu.startTime and time <= menu.endTime:
        availableMenus.append(menu) 
    return availableMenus
  
class Menu:
  def __init__(self, name, items, startTime, endTime):
    self.name = name
    self.items = items
    self.startTime = startTime
    self.endTime = endTime

  def __repr__(self):
    return str(self.name) + ' menu available from ' + str(self.startTime) + ' - ' + str(self.endTime)
  
  def calculateBill(self, purcahseItems):
    bill = 0
    for purcahsedItem in purcahseItems:
      if purcahsedItem in self.items:
        bill += self.items[purcahsedItem]
    return bill

brunchMenu = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('Brunch', brunchMenu, 1100, 1600)

earlyBirdMenu = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
earlyBird = Menu('Early Bird', earlyBirdMenu, 1500, 1800)

dinnerMenu = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner = Menu('Dinner', dinnerMenu, 1700, 2300)

kidsMenu = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('Kids', kidsMenu, 1100, 2100)

menus = [brunch, earlyBird, dinner, kids] 
flagshipStore = Franchise('1232 West End Road', menus)
newInstallment = Franchise('12 East Mulberry Street', menus)

basta = Business('"Basta Fazoolin" with my Heart', [flagshipStore, newInstallment])

arepasMenu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas = Menu("Take a’ Arepa", arepasMenu, 1000, 2000)
arepasPlace = Franchise('189 Fitzgerald Avenue', [arepas])
arepa = Business("Take a’ Arepa", [arepasPlace])

#print(brunch)
#print(earlyBird)
#print(dinner)
#print(kids)
#print(brunch.calculateBill(['pancakes', 'home fries', 'coffee']))
#print(earlyBird.calculateBill(['salumeria plate', 'mushroom ravioli (vegan)']))
#print(flagshipStore)
#print(flagshipStore.availableMenus(1200))
#print(arepa.franchises[0].menus[0])