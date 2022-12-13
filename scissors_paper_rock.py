import random

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))
computer_choice = random.randint(0, 2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
stuff = [rock, paper, scissors]


print("Computer chose")
print(stuff[computer_choice])
print(f"You chose:")
print(stuff[user_choice])

if user_choice == computer_choice:
    print("You tie")
elif user_choice < computer_choice:
    print("You loose")
else:
    print("You win")


