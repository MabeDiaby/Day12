# ################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# # print(potion_strenght) WILL ERROR

# # Global Scope
# player_health = 12
# def drink_potions():
#     potion_strength = 2
#     print(player_health)
# drink_potions()

# # There is no Block Scope within if/while/for functions
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# #Modifying Global Scope
# enemies = 1

# def increase_enemies():
#     # global enemies #AVOID DOING THIS
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enimes = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.14159

def calc():
    PI