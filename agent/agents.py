import random
tiles = [random.randint(0, 1) for _ in range(8)]
print("Initial Tiles:", tiles)
for i in range(8):
    if tiles[i] == 1:
        print(f"Tile {i}: Dirty → Cleaning")
        tiles[i] = 0
    else:
        print(f"Tile {i}: Already clean → Skipping")
print("Final Tiles:", tiles)