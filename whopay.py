admins = ["Ahmed", "Osama", "sameh", "Manal" ,"marwa"]
names = input("please type your name").strip().capitalize()

if names in admins:
    print(f"Hello {names} we")
else:
    print("you are Not admin")