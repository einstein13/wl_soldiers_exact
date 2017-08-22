# def get_min_attack(tribe=1, level=0):
#     if level < 0:
#         return 0
#     if tribe == 1: # Barbarians
#         if level > 5:
#             return 0
#         return 12.0+8.5*level
#     elif tribe == 2: # Empire
#         if level > 4:
#             return 0
#         return 13.0+8.0*level
#     elif tribe == 3: # Atlanteans
#         if level > 5:
#             return 0
#         return 12.0+8.0*level
#     elif tribe == 4: # Frisians
#         if level > 6:
#             return 0
#         return 13.0+10.0*level
#     elif tribe == 5: # Amazons
#         if level > 2:
#             return 0
#         return 12.0+6.5*level
#     return 0

# def get_max_attack(tribe=1, level=0):
#     if level < 0:
#         return 0
#     if tribe == 1: # Barbarians
#         if level > 5:
#             return 0
#         return 16.0+8.5*level
#     elif tribe == 2: # Empire
#         if level > 4:
#             return 0
#         return 15.0+8.0*level
#     elif tribe == 3: # Atlanteans
#         if level > 5:
#             return 0
#         return 16.0+8.0*level
#     elif tribe == 4: # Frisians
#         if level > 6:
#             return 0
#         return 15.0+10.0*level
#     elif tribe == 5: # Amazons
#         if level > 2:
#             return 0
#         return 16.0+6.5*level
#     return 0

# def get_defense(tribe=1, level=0):
#     if level < 0:
#         return 0
#     if tribe == 1: # Barbarians
#         if level > 0:
#             return 0
#         return 1.0 - 0.03
#     elif tribe == 2: # Empire
#         if level > 0:
#             return 0
#         return 1.0 - 0.05
#     elif tribe == 3: # Atlanteans
#         if level > 2:
#             return 0
#         return 1.0 - (0.06 + 0.08*level)
#     elif tribe == 4: # Frisians
#         if level > 2:
#             return 0
#         return 1.0 - (0.05 + 0.20*level)
#     elif tribe == 5: # Amazons
#         if level > 2:
#             return 0
#         return 1.0 - (0.05 + 0.10*level)
#     return 0

# def get_evade(tribe=1, level=0):
#     if level < 0:
#         return 0
#     if tribe == 1: # Barbarians
#         if level > 2:
#             return 0
#         return 0.75 - 0.15*level
#     elif tribe == 2: # Empire
#         if level > 2:
#             return 0
#         return 0.7 - 0.16*level
#     elif tribe == 3: # Atlanteans
#         if level > 2:
#             return 0
#         return 0.7 - 0.17*level
#     elif tribe == 4: # Frisians
#         if level > 0:
#             return 0
#         return 0.75
#     elif tribe == 5: # Amazons
#         if level > 3:
#             return 0
#         return 0.7 - 0.15*level
#     return 0

# def get_health(tribe=1, level=0):
#     if level < 0:
#         return 0
#     if tribe == 1: # Barbarians
#         if level > 3:
#             return 0
#         return 130.0 + 28.0*level
#     elif tribe == 2: # Empire
#         if level > 4:
#             return 0
#         return 130.0 + 21.0*level
#     elif tribe == 3: # Atlanteans
#         if level > 1:
#             return 0
#         return 135.0 + 40.0*level
#     elif tribe == 4: # Frisians
#         if level > 2:
#             return 0
#         return 120.0 + 50.0*level
#     elif tribe == 5: # Amazons
#         if level > 3:
#             return 0
#         return 130.0 + 23.0*level
#     return 0

from fractions import Fraction

def get_min_attack(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1: # Barbarians
        if level > 5:
            return 0
        return 12 + Fraction(17, 2) * level
    elif tribe == 2: # Empire
        if level > 4:
            return 0
        return 13 + 8 * level
    elif tribe == 3: # Atlanteans
        if level > 5:
            return 0
        return 12 + 8 * level
    elif tribe == 4: # Frisians
        if level > 6:
            return 0
        return 13 + 10 * level
    elif tribe == 5: # Amazons
        if level > 2:
            return 0
        return 12 + Fraction(13, 2) * level
    return 0

def get_max_attack(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1: # Barbarians
        if level > 5:
            return 0
        return 16 + Fraction (17, 2) * level
    elif tribe == 2: # Empire
        if level > 4:
            return 0
        return 15 + 8 * level
    elif tribe == 3: # Atlanteans
        if level > 5:
            return 0
        return 16 + 8 * level
    elif tribe == 4: # Frisians
        if level > 6:
            return 0
        return 15 + 10 * level
    elif tribe == 5: # Amazons
        if level > 2:
            return 0
        return 16.0 + Fraction(13, 2) * level
    return 0

def get_defense(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1: # Barbarians
        if level > 0:
            return 0
        return 1 - Fraction(3, 100)
    elif tribe == 2: # Empire
        if level > 0:
            return 0
        return 1  - Fraction(5, 100)
    elif tribe == 3: # Atlanteans
        if level > 2:
            return 0
        return 1 - (Fraction(6, 100) + Fraction(8, 100) * level)
    elif tribe == 4: # Frisians
        if level > 2:
            return 0
        return 1 - (Fraction(5, 100) + Fraction(20, 100) * level)
    elif tribe == 5: # Amazons
        if level > 2:
            return 0
        return 1 - (Fraction(5, 100) + Fraction(10, 100) * level)
    return 0

def get_evade(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1: # Barbarians
        if level > 2:
            return 0
        return Fraction(75, 100) - Fraction(15, 100) * level
    elif tribe == 2: # Empire
        if level > 2:
            return 0
        return Fraction(70, 100) - Fraction(16, 100) * level
    elif tribe == 3: # Atlanteans
        if level > 2:
            return 0
        return Fraction(70, 100) - Fraction(17, 100) * level
    elif tribe == 4: # Frisians
        if level > 0:
            return 0
        return Fraction(75, 100)
    elif tribe == 5: # Amazons
        if level > 3:
            return 0
        return Fraction(70, 100) - Fraction(15, 100) * level
    return 0

def get_health(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1: # Barbarians
        if level > 3:
            return 0
        return 130 + 28 * level
    elif tribe == 2: # Empire
        if level > 4:
            return 0
        return 130 + 21 * level
    elif tribe == 3: # Atlanteans
        if level > 1:
            return 0
        return 135 + 40 * level
    elif tribe == 4: # Frisians
        if level > 2:
            return 0
        return 120 + 50 * level
    elif tribe == 5: # Amazons
        if level > 3:
            return 0
        return 130 + 23 * level
    return 0
