def print_board(b):
    for row in b:
        print(" | ".join(row))
        print("-" * 9)


def check_win(b, p):
    return (
        any(all(c == p for c in r) for r in b) or
        any(all(b[i][j] == p for i in range(3)) for j in range(3)) or
        all(b[i][i] == p for i in range(3)) or
        all(b[i][2 - i] == p for i in range(3))
    )


def empty_cells(b):
    return [(i, j) for i in range(3) for j in range(3) if b[i][j] == " "]


def full(b):
    return all(c != " " for r in b for c in r)


def minimax(b, is_max):
    if check_win(b, "O"):
        return 1
    if check_win(b, "X"):
        return -1
    if full(b):
        return 0

    scores = []

    for i, j in empty_cells(b):
        b[i][j] = "O" if is_max else "X"
        scores.append(minimax(b, not is_max))
        b[i][j] = " "

    return max(scores) if is_max else min(scores)


def best_move(b):
    best = -2
    move = None

    for i, j in empty_cells(b):
        b[i][j] = "O"
        score = minimax(b, False)
        b[i][j] = " "

        if score > best:
            best = score
            move = (i, j)

    return move


def play():
    b = [[" "] * 3 for _ in range(3)]
    print("You: X | Computer: O")

    while True:
        print_board(b)
        try:
            x, y = map(int, input("Enter row and col (0-2): ").split())
            if b[x][y] != " ":
                raise ValueError
            b[x][y] = "X"
        except:
            print("Invalid! Try again.")
            continue

        if check_win(b, "X"):
            print_board(b)
            print("You win!")
            break

        if full(b):
            print_board(b)
            print("Draw!")
            break

        i, j = best_move(b)
        b[i][j] = "O"

        if check_win(b, "O"):
            print_board(b)
            print("Computer wins!")
            break

        if full(b):
            print_board(b)
            print("Draw!")
            break


if __name__ == "__main__":
    play()
