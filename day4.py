lines = [l.strip() for l in open('input4.txt').readlines()]

numbers_to_draw = [int(n) for n in lines.pop(0).split(',')]

board_lines = [l for l in lines if l]

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

board_numbers = []

for line in board_lines:
    board_numbers += [int(l) for l in line.split(' ') if l]

boards = list(chunks(board_numbers, 25))

def row_is_in_drawn(board, row_index, drawn):
    return all(number in drawn for number in board[row_index * 5:row_index * 5 + 5])

def column_is_in_drawn(board, column_index, drawn):
    return all(number in drawn for number in board[column_index:column_index + 25:5])

def has_row(board, drawn):
    return any(row_is_in_drawn(board, row_index, drawn) for row_index in range(5))

def has_column(board, drawn):
    return any(column_is_in_drawn(board, column_index, drawn) for column_index in range(5))

def board_scores(board, drawn):
    return has_row(board, drawn) or has_column(board, drawn)


def part1():
    drawn_numbers = []

    for drawn_number in numbers_to_draw:
        drawn_numbers.append(drawn_number)

        for board in boards:
            if board_scores(board, drawn_numbers):
                unmarked = [number for number in board if number not in drawn_numbers]
                score = sum(unmarked) * drawn_number
                return score


def part2():
    drawn_numbers = []

    boards_without_wins = boards
    last_winning_board_score = 0

    for drawn_number in numbers_to_draw:
        drawn_numbers.append(drawn_number)

        for board_index, board in enumerate(boards_without_wins):
            if board_scores(board, drawn_numbers):
                unmarked = [number for number in board if number not in drawn_numbers]
                last_winning_board_score = sum(unmarked) * drawn_number
                del boards_without_wins[board_index]
    
    return last_winning_board_score


print("Day 4 part 1:", part1())
print("Day 4 part 2:", part2())