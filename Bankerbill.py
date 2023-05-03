import random

names_string = input ("Give me everybody's names, seperated by a coma. \n")

names = names_string.split(", ")

num_items = len(names)

pick = random.randint(0, num_items - 1)
picked = names[pick]

print(f"the person who will pay is {picked}")