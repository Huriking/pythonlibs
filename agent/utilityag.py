import random
tiles = [random.randint(0, 1) for _ in range(8)]
print("Initial Tiles:", tiles)
utility = 0
for i in range(8):
    if tiles[i] == 1:
        print(f"Tile {i}: Dirty → Cleaning (Utility +1)")
        tiles[i] = 0
        utility += 1
    else:
        print(f"Tile {i}: Already clean → No utility gain")
print("Final Tiles:", tiles)
print("Total Utility Gained:", utility)