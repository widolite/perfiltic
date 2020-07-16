# 1. initial_input = '[1, 0, 0], [0, 1, 1],[1, 1, 0]:1'
# 2. initial_input = '[1, 0, 0], [0, 1, 1],[1, 1, 0]:2'

# 1. Output - 0, 1, 0,0, 0, 1,1, 1, 1
# 2. Output - 0, 0, 0,1, 0, 1,0, 1, 1

from sys import stdin


def game_of_life(board):
    # Finding Neighbors for a giving cell.
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    rows = len(board)
    cols = len(board[0])

    # Iterate through board cell by cell.
    for row in range(rows):
        for col in range(cols):

            live_neighbors = 0
            for neighbor in neighbors:

                r = (row + neighbor[0])
                c = (col + neighbor[1])

                if (rows > r >= 0) and (cols > c >= 0) and abs(board[r][c]) == 1:
                    live_neighbors += 1

            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = -1
            if board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 2

    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board


def process_input(input):
    params = input.split(":")
    return board_next_step(params[0], params[1])


def board_next_step(initial_board, steps):
    # su código va acá
    new_output_format = '{}, {}, {},{}, {}, {},{}, {}, {}'
    turns = int(steps)
    initial_input = initial_board
    cleaning_input = [int(x) for x in initial_input.split(":")[0] if x not in ", []"]
    initial_board = list()
    temp_cel_list = list()
    global state
    for cell in cleaning_input:
        temp_cel_list.append(cell)
        if len(temp_cel_list) == 3:
            initial_board.append(temp_cel_list)
            temp_cel_list = list()
    for turn in range(turns):
        state = game_of_life(initial_board)
    formatted_output = list()
    for cells in state:
        for cell in cells:
            formatted_output.append(str(cell))
    initial_board = new_output_format.format(*"".join(formatted_output))
    return initial_board


if __name__ == '__main__':
    # tener cuidado en python con los newlines
    for lineinput in stdin:
        print(process_input(lineinput))
