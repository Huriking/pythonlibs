import random
tiles = [random.randint(0, 1) for _ in range(8)]
print("Initial Tiles:", tiles)
# Store only dirty tile indices (i.e., model)
dirty_tiles = [i for i, val in enumerate(tiles) if val == 1]
for i in dirty_tiles:
    print(f"Tile {i}: Dirty → Cleaning")
    tiles[i] = 0
print("Final Tiles:", tiles)