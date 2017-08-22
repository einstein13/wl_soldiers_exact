from math import factorial
from fractions import Fraction

from soldiers import Soldier

print_warnings = False
print_partial_results = False

# math functions
def binomial(n, k):
    # binomial coefficient
    # how many times you can pick k elements from n-element set
    if n < k:
        if print_warnings:
            print('W: Binomial: n < k (%d, %d)' % (n, k))
        return 0
    if n < 1 or k < 0:
        if print_warnings:
            print('W: Binomial: n OR k (%d, %d)' % (n, k))
        return 0
    return factorial(n)// (factorial(k) * factorial(n-k))

def round(number, points):
    base = 10**points
    bigger = number*base
    if bigger - int(bigger) >= 0.5:
        bigger += 1
    return 1.0 * int(bigger)/base

# probabilities:
def kill_after_hit_points(hit_min, hit_max, sum_of_points, number_of_hits):
    # return probability of kill after given number of hits

    # hit_min - minimum amount of points gained in one hit
    # hit_max - maximum amount of points gained in one hit
    # number_of_hits - how many hits are given. Each hit is betweeen hit_min and hit_max
    # sum_of_points - target number of points gained in all (number_of_hits) hits
    # sum_max_hit - maximal sum of points (within number_of_hits hits)
    # sum_min_hit - minimal sum of points (within number_of_hits hits)
    # max_min_diff - difference between hit_max and hit_min values, how far are max and min hit
    # points_above_minimal - how many points has to be hit above minimal hits
    # minimal_number_of_hits_above_minimal - minimal number of hits which are above hit_min value


    sum_max_hit = hit_max * number_of_hits
    sum_min_hit = hit_min * number_of_hits
    # impossible to hit with:
    # - maximum hits in each hit (not enough points);
    #   example: hits 1-5, 5 hits, target of 100 points
    # - minimum hits in each hit (target points reached earlier);
    #   example: hits 1-5, 5 hits, target of 2 points
    if sum_of_points > sum_max_hit:
        if print_warnings:
            print("W: KAEH: sum of points (%d, %d, %d)" % (sum_min_hit, sum_of_points, sum_max_hit))
        return 0
    if sum_of_points < sum_min_hit:
        if print_warnings:
            print("W: KAEH: sum of points (%d, %d, %d)" % (sum_min_hit, sum_of_points, sum_max_hit))
        return 1

    max_min_diff = hit_max - hit_min
    points_above_minimal = sum_of_points - sum_min_hit

    minimal_number_of_hits_above_minimal = 0
    itr = 0
    while itr * max_min_diff < points_above_minimal:
        itr += 1
    minimal_number_of_hits_above_minimal = itr

    # can be replaced by ceiling function:
    # ceil(points_above_minimal/max_min_diff)

    # calculating result
    itr = 0
    result = 0
    while itr < minimal_number_of_hits_above_minimal:
        partial = binomial(number_of_hits, itr)
        partial *= (points_above_minimal - itr * max_min_diff) ** number_of_hits
        partial *= (-1) ** itr

        result += partial
        itr += 1

    result = Fraction(result, factorial(number_of_hits))
    result /= max_min_diff ** number_of_hits
    return 1 - result

def kill_after_exact_hit_points(hit_min, hit_max, sum_of_points, number_of_hits):
    # return probability of kill after exact number of hits
    kill_this = kill_after_hit_points(hit_min, hit_max, sum_of_points, number_of_hits)
    kill_before = kill_after_hit_points(hit_min, hit_max, sum_of_points, number_of_hits-1)
    return kill_this - kill_before

def kill_after_hit_probability(probability_of_hit, number_of_death_hits, number_of_all_hits):
    # return probability of kill on last hit possibility
    if number_of_all_hits < number_of_death_hits:
        if print_warnings:
            print("W: SKAH: hits (%d, %d)" % (number_of_death_hits, number_of_all_hits))
        return 0
    probability_of_miss = 1 - probability_of_hit
    number_of_hits_except_last = number_of_death_hits - 1
    number_of_miss = number_of_all_hits - number_of_death_hits
    number_of_all_except_last = number_of_all_hits - 1
    result = binomial(number_of_all_except_last, number_of_hits_except_last)
    result *= probability_of_hit ** number_of_death_hits
    result *= probability_of_miss ** number_of_miss
    return result

def survive_hit_probability(probability_of_hit, number_of_death_hits, number_of_all_hits):
    # return probability of survive all hits
    if number_of_death_hits > number_of_all_hits:
        # nothing can happen bad
        return 1
    probability_of_miss = 1 - probability_of_hit

    result = 0
    for itr in range(number_of_death_hits):
        # itr is in [0, 1, ..., number_of_death_hits-1]
        done_hits = itr
        done_miss = number_of_all_hits - done_hits
        partial = binomial(number_of_all_hits, itr)
        if done_hits > 0:
            partial *= probability_of_hit ** done_hits
        if done_miss > 0:
            partial *= probability_of_miss ** done_miss
        result += partial
    return result


# main class
class Simulation(object):

    soldiers_list = []
    result_matrix = []
    dictionaries_list = []

    def add_soldiers_definitions(self, new_soldiers):
        self.dictionaries_list = new_soldiers
        for soldier in new_soldiers:
            s = Soldier()
            s.set_stats(soldier)
            s.convert_to_fractions()
            self.soldiers_list.append(s)
        return None

    def partial_probability_kill(self, attacker, defender, attacker_hits, defender_hits):
        # probability of kill with attacker_hits and defender_hits number
        attacker_hit_probability = defender.evade
        defender_hit_probability = attacker.evade
        suma = 0 # sum of all probabilities
        best_probability = 0 # best found partial probability
        all_hits = attacker_hits # iterator
        stop_counting = 10**10 # stop factor
        while True:
            p1 = kill_after_hit_probability(attacker_hit_probability, attacker_hits, all_hits)
            p2 = survive_hit_probability(defender_hit_probability, defender_hits, all_hits-1)
            probability = p1 * p2
            if probability > 0:
                if best_probability < probability:
                    best_probability = probability
                if probability * stop_counting < best_probability:
                    break
                suma += probability
            all_hits += 1
        return suma

    def simulate_one(self, attacker, defender):
        attacker_min_hit_number = 0
        attacker_max_hit_number = 0
        attacker_probabilities = {}
        defender_min_hit_number = 0
        defender_max_hit_number = 0
        defender_probabilities = {}

        # define borders: how many attack/defend hits can be gained
        itr = 0
        run = True
        while True:
            probability = kill_after_exact_hit_points(
                    attacker.attack_min, attacker.attack_max,
                    defender.health / defender.defense, itr)
            if probability > 0:
                attacker_probabilities[itr] = probability
            if probability > 0 and run == True:
                run = False
                attacker_min_hit_number = itr
            if probability == 0 and run == False:
                attacker_max_hit_number = itr - 1
                break
            itr += 1

        itr = 0
        run = True
        while True:
            probability = kill_after_exact_hit_points(
                    defender.attack_min, defender.attack_max,
                    attacker.health / attacker.defense, itr)
            if probability > 0:
                defender_probabilities[itr] = probability
            if probability > 0 and run == True:
                run = False
                defender_min_hit_number = itr
            if probability == 0 and run == False:
                defender_max_hit_number = itr - 1
                break
            itr += 1

        probability_sum = 0
        for itr1 in range(attacker_min_hit_number, attacker_max_hit_number + 1):
            for itr2 in range(defender_min_hit_number, defender_max_hit_number + 1):
                partial_probability = attacker_probabilities[itr1]
                partial_probability *= defender_probabilities[itr2]
                partial_probability *= self.partial_probability_kill(attacker, defender, itr1, itr2)
                probability_sum += partial_probability
        return probability_sum

    def simulate_all(self):
        self.result_matrix = []
        for itr1 in range(len(self.soldiers_list)):
            self.result_matrix.append([])
            for itr2 in range(len(self.soldiers_list)):
                result = self.simulate_one(self.soldiers_list[itr1], self.soldiers_list[itr2])
                if print_partial_results:
                    print(float(result))
                self.result_matrix[itr1].append(result)

    def markdown_table(self, matrix):
        length = len(self.dictionaries_list)
        string = "| vs."
        for itr1 in range(length):
            string += " | "+self.dictionaries_list[itr1]['name']
        string += " |\n"
        for itr1 in range(-1, length):
            string += "| --- "
        string += "|\n"
        for itr1 in range(length):
            for itr2 in range(-1,length):
                if itr2 == -1:
                    string += "| " + self.dictionaries_list[itr1]['name']
                else:
                    string += " | " + str(round(matrix[itr1][itr2]*100,1)) + "%"
            string += " |\n"
        return string

    def print_results(self):
        string = "Battles win:\n"
        string += self.markdown_table(self.result_matrix)
        print("\n"+string)
        file = open("out.txt","w")
        file.write(string)
        file.close()
        return 0