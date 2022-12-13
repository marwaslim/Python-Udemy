# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
two_numbers = list(position)
column = int(two_numbers[0])-1
row = int(two_numbers[1])-1

map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")


