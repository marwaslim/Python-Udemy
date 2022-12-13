# Import the random module here
import random
# Split string method
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
items = len(names)

choice_first = random.randint(0, items -1)
print(f'random index returned was: {choice_first}')
who_pay = names[choice_first]
print(who_pay + " will pay")