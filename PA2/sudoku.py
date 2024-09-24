import sys

#Function searching every row, column and 3x3 squares to find appropriate numbers.
def find_possibilities(board, row, col, num):
    #loop searching the rows.
    for k in range(9):
        if board[row][k] == num:
            return 0

    #loop searching columns.
    for j in range(9):
        if board[j][col] == num:
            return 0

    #loop searching 3x3 squares.
    k = (col // 3) * 3
    s = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[s + i][k + j] == num:
                return 0
    return 1


#Function which finds valid grids for numbers that found by find_possibilites function.
def find_valid_grids(board):
    # Search board and add appropriate numbers to new list possibilities.
    for row in range(9):
        for col in range(9):
            if board[row][col] == "0":
                possibilities = []
                for num in range(1, 10):
                    if find_possibilities(board, row, col, str(num)):
                        possibilities.append(num)
                #Return the possibilities list's first number when find a grid which have one possibility.
                if len(possibilities) == 1:
                    return row, col, possibilities[0]
    #If there is no grid with 1 possibility function returns None.
    return None


#Function to change sudoku board type which is list into string.
def sudoku_board(board):
    birstr = ""
    for row in board:
        birstr += "\n"
        for num in row:
            birstr += num + " "
        birstr = birstr.rstrip()
    return birstr


#Function to solves sudoku and prints Steps, Col and Row numbers and number which put by find_valid_grid function.
def solve_sudoku(board):
    denemestr = ''
    step = 0
    while True:
        # Find a cell with only one possibility and put it into variable called result.
        result = find_valid_grids(board)

        if result is None:
            # If No more cells with only one possibility end loop.
            break

        #Print grid's Row,Column number's and print the number which is put the grid.
        row, col, num = result[0], result[1], result[2]
        board[row][col] = str(num)
        row = row + 1
        col = col + 1
        step += 1
        denemestr += "-"*18
        denemestr += "\nStep {} - {} @ R{}C{}\n".format(step, num, row, col)
        denemestr += "-" * 18
        denemestr += sudoku_board(board)
        denemestr += "\n"
    #Adds 18 dashes at the end of the output.
    denemestr = denemestr + "------------------"
    return denemestr


def main():
    #take input sudoku example from input.txt
    inp = open(sys.argv[1], "r")
    text = inp.read()
    inp.close()

    #turn sudoku example string to list
    liste = text.split("\n")

    #change list into matris
    oburliste = [liste[i].split() for i in range(9)]

    #solve sudoku by using solve_sudoku function and put the result to output_text
    output_text = solve_sudoku(oburliste)

    #print output to output.txt
    out = open(sys.argv[2], "w")
    out.write(output_text)
    out.flush()
    out.close()


if __name__ == '__main__':
    main()
