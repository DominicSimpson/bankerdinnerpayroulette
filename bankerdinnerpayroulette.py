import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
randomly_chosen_name = names[random_index]

print(f"{randomly_chosen_name} is going to buy the meal today!")
