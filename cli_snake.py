import time
import keyboard
import sys
import os
import random

def apple(map, positions):
    x = random.randint(0, map_height)
    y = random.randint(0, map_length)
    while [x, y] in positions:
        x = random.randint(0, map_height)
        y = random.randint(0, map_length)
    map[x][y] = "🟥"
    return map

map = [["⬛" for i in range(20)] for y in range(15)]

a, b = -1, 0
x, z = 10, 25

positions = []
count = 0
map_height = len(map) - 1
map_length = len(map[0]) - 1
max_count = 2
map[random.randint(0, map_height)][random.randint(0, map_length)] = "🟥"

a, b = -1, 0

game_over = False

while not game_over:
    if keyboard.is_pressed('w') and a != 1:
        a, b = -1, 0
    elif keyboard.is_pressed('a') and b != 1:
        a, b = 0, -1
    elif keyboard.is_pressed('s') and a != -1:
        a, b = 1, 0
    elif keyboard.is_pressed('d') and b != -1:
        a, b = 0, 1

    x = 0 if x + a > map_height else map_height if x + a < 0 else x + a
    z = 0 if z + b > map_length else map_length if z + b < 0 else z + b

    if [x, z] not in positions:
        if map[x][z] == "🟥":
            max_count += 1
            map = apple(map, positions + [[x, z]])

        if count == max_count:
            map[x][z] = "⬜"
            positions.append([x, z])
            map[positions[0][0]][positions[0][1]] = "⬛"
            positions.pop(0)
        else:
            map[x][z] = "⬜"
            positions.append([x, z])
            count += 1

        for row in map:
            print("".join(row))
        print()

        time.sleep(0.075)
        os.system("cls")
    else:
        game_over = True

os.system("cls")
print("Game over")
sys.exit()
