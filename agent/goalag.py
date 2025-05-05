import random
tiles = [random.randint(0, 1) for _ in range(8)]
print("Initial Tiles:", tiles)
goal = [0] * 8 # Goal: all tiles clean
for i in range(8):
    if tiles == goal:
        print("Goal achieved: All tiles clean!")
        break
    if tiles[i] == 1:
        print(f"Tile {i}: Dirty → Cleaning")
        tiles[i] = 0
    else:
        print(f"Tile {i}: Already clean → Skipping")
print("Final Tiles:", tiles)