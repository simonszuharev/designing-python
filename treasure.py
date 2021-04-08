# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Please, use commas to separate the numbers")
# 🚨 Don't change the code above 👆

position_index = position.split(", ")

map[int(position_index[0])-1][int(position_index[1])-1] = "X"
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")