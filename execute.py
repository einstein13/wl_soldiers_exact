from calculations import Simulation

#example soldiers

#Barbarians
bar0 = {'name':'bar_00', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
bar2 = {'name':'bar_02', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
bar7 = {'name':'bar_07', 'tribe':'barbarians', 'attack':3, 'defense':0, 'evade':2, 'health':2} #promoted only for iron
bar9 = {'name':'bar_09', 'tribe':'barbarians', 'attack':5, 'defense':0, 'evade':2, 'health':2} #without last promotion
bar10 = {'name':'bar_10', 'tribe':'barbarians', 'attack':5, 'defense':0, 'evade':2, 'health':3} #fully promoted soldier

#Empire
emp0 = {'name':'emp_00', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
emp2 = {'name':'emp_02', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
emp7 = {'name':'emp_07', 'tribe':'empire', 'attack':2, 'defense':0, 'evade':2, 'health':3} #promoted only for iron
emp9 = {'name':'emp_09', 'tribe':'empire', 'attack':4, 'defense':0, 'evade':2, 'health':3} #without last promotion
emp10 = {'name':'emp_10', 'tribe':'empire', 'attack':4, 'defense':0, 'evade':2, 'health':4} #fully promoted soldier

#Atlanteans
atl0 = {'name':'atl_00', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
atl2 = {'name':'atl_02', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
atl7 = {'name':'atl_07', 'tribe':'atlanteans', 'attack':2, 'defense':1, 'evade':2, 'health':0} #promoted only for iron
atl8 = {'name':'atl_08', 'tribe':'atlanteans', 'attack':4, 'defense':0, 'evade':2, 'health':1} #without last promotion
atl9 = {'name':'atl_09', 'tribe':'atlanteans', 'attack':4, 'defense':1, 'evade':2, 'health':1} #without last promotion
atl10 = {'name':'atl_10', 'tribe':'atlanteans', 'attack':4, 'defense':2, 'evade':2, 'health':1} #fully promoted soldier

#Frisians
fri0 = {'name': 'fri_00', 'tribe': 'frisians', 'attack': 0, 'defense': 0, 'evade': 0, 'health': 0}
fri9 = {'name': 'fri_09', 'tribe': 'frisians', 'attack': 5, 'defense': 2, 'evade': 0, 'health': 2}
fri10 = {'name': 'fri_10', 'tribe': 'frisians', 'attack': 6, 'defense': 2, 'evade': 0, 'health': 2}

#Amazons
amz0 = {'name': 'amz_00', 'tribe': 'amazons', 'attack': 0, 'defense': 0, 'evade': 0, 'health': 0}
#amz9 = {'name': 'amz_09', 'tribe': 'amazonsamazons', 'attack': 5, 'defense': 2, 'evade': 0, 'health': 2}
amz10 = {'name': 'amz_10', 'tribe': 'amazons', 'attack': 2, 'defense': 2, 'evade': 3, 'health': 3}

list_to_test = [bar0, emp0, atl0, bar10, emp10, atl10]
list_to_test = [bar10, emp10, atl10]

stats = Simulation()
stats.add_soldiers_definitions(list_to_test)
# sol = stats.soldiers_list[0]
# sol.attack_min = 100
# sol.attack_max = 110
# sol.defense = 1
# from fractions import Fraction
# sol.evade = Fraction(75, 100)
# sol.health = 150
stats.simulate_all()
stats.print_results()