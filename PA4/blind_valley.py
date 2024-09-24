import sys

""" function to check whether sum of "H" in lines is equal to given nums or not."""


def h_line(liste, restrict_nums):
    for i in range(len(liste)):
        if restrict_nums[0][i] != "-1" and str(liste[i].count("H")) != restrict_nums[0][i]:
            return False
    return True


""" function to check whether sum of "B" in lines is equal to given nums or not."""


def b_line(liste, restrict_nums):
    for i in range(len(liste)):
        if restrict_nums[1][i] != "-1" and str(liste[i].count("B")) != restrict_nums[1][i]:
            return False
    return True


""" function to check whether sum of "H" in columns is equal to given nums or not."""


def h_column(liste, restrict_nums):
    for i in range(len(liste[0])):
        if restrict_nums[2][i] != "-1" and str([j[i] for j in liste].count("H")) != restrict_nums[2][i]:
            return False
    return True


""" function to check whether sum of "B" in columns is equal to given nums or not."""


def b_column(liste, restrict_nums):
    for i in range(len(liste[0])):
        if restrict_nums[3][i] != "-1" and str([j[i] for j in liste].count("B")) != restrict_nums[3][i]:
            return False
    return True


""" function to control selected cell is valid or not by looking its neighbours."""


# when function is looking neighbours it compares the value which is "H" or "B".
def valid_neighbor(liste, row, col, value):
    # left neighbour
    if col - 1 >= 0 and liste[row][col - 1] == value:
        return False

    # up neighbour
    elif row - 1 >= 0 and liste[row - 1][col] == value:
        return False

    # right neighbour
    elif col < len(liste[row]) - 1 and liste[row][col + 1] == value:
        return False

    # down neighbour
    elif row < len(liste) - 1 and liste[row + 1][col] == value:
        return False
    return True


""" function that checks if the numbers on the board are valid according to the given number constraint."""


def control(liste, restrict_nums):
    count = 0
    for current_row in liste:
        for cell in current_row:
            if cell not in ["H", "B", "N"]:
                count += 1
    if count <= 0:
        if not h_line(liste, restrict_nums) or not b_line(liste, restrict_nums) or not h_column(liste,
                                                                                                restrict_nums) or not b_column(
            liste, restrict_nums):
            return False
    return True


# Solver function that solves function and realizes backtracking algorithm to solve puzzle.
def backtrack_solver(liste, row, col, restrict_nums):
    # variables holds lenght of row and column.
    int1 = len(liste)
    int2 = len(liste[0])

    # Base condition if function reach end of the function control the grid is valid by means of restrict_nums(given nums).
    # If the board is valid  return True, else return False.
    if row == int1 - 1 and (col >= int2 - 1):
        if (not h_line(liste, restrict_nums) or not b_line(liste, restrict_nums)
                or not h_column(liste, restrict_nums) or not b_column(liste, restrict_nums)):
            return False
        else:
            return True
    # if the function reaches end of the row, add 1 to row and assign 0 to column number.
    if col >= len(liste[0]):
        row += 1
        col = 0

    # "L" condition.
    # If selected cell is "L" firstly it tries "H" and "B" case.
    if liste[row][col] == "L":
        # initial numbers to back original numbers in case of all numbers are possibilties are wrong. Backtrack situation.
        initial1 = liste[row][col]
        initial2 = liste[row][col + 1]

        # try "H" and "B" case.
        liste[row][col] = "H"
        liste[row][col + 1] = "B"

        # control that is selected cell and the right cell valid by means of neighbourhood.
        # else function tries "B"- "H" case. And apply same steps in "B"-"H" case.

        success = valid_neighbor(liste, row, col, "H")  # checks "L" cell
        succestry2 = valid_neighbor(liste, row, col + 1, "B")  # checks "R" cell

        if success and succestry2 and backtrack_solver(liste, row, col + 2, restrict_nums):
            return True

        else:
            # try "B" and "H" case.
            liste[row][col] = "B"
            liste[row][col + 1] = "H"

            # control that is selected cell and the right cell valid by means of neighbourhood.
            # else function tries "N"- "N" case.
            success2 = valid_neighbor(liste, row, col, "B")  # checks "L" cell
            successtry5 = valid_neighbor(liste, row, col + 1, "H")  # checks "R" cell

            if success2 and successtry5 and backtrack_solver(liste, row, col + 2, restrict_nums):
                return True

            else:
                # if "H"-"B" and "B"-"H" cases are wrong try "N"-"N" case.
                liste[row][col] = "N"
                liste[row][col + 1] = "N"

                success4 = backtrack_solver(liste, row, col + 2, restrict_nums)

                # Control the nums is valid or not for restritct_nums with control function.
                # if it is not valid return False.
                if not success4 or not control(liste, restrict_nums):
                    # if all possibilities are wrong change the cell's with original cell's and return False.
                    liste[row][col] = initial1
                    liste[row][col + 1] = initial2
                    return False

    # "U" condition.
    # If selected cell is "U" firstly it tries "H" and "B" case.
    elif liste[row][col] == "U":
        # initial numbers to back original numbers in case of all numbers are possibilties are wrong.
        initial1 = liste[row][col]
        initial2 = liste[row + 1][col]

        # try "H" and "B" case.
        liste[row][col] = "H"
        liste[row + 1][col] = "B"

        # control that is selected cell and the right cell valid by means of neighbourhood.
        # else function tries "B"- "H" case. And apply same steps in "B"-"H" case.
        success = valid_neighbor(liste, row, col, "H")  # checks "U" cell
        succestry3 = valid_neighbor(liste, row + 1, col, "B")  # checks "D" cell

        if success and succestry3 and backtrack_solver(liste, row, col + 1, restrict_nums):
            return True

        else:
            # try "B" and "H" case.
            liste[row][col] = "B"
            liste[row + 1][col] = "H"

            # control that is selected cell and the right cell valid by means of neighbourhood.
            # else function tries "N"- "N" case.

            success3 = valid_neighbor(liste, row, col, "B")  # checks "U" cell
            succestry4 = valid_neighbor(liste, row + 1, col, "H")  # checks "D" cell

            if success3 and succestry4 and backtrack_solver(liste, row, col + 1, restrict_nums):
                return True

            else:
                # if "H"-"B" and "B"-"H" cases are wrong try "N"-"N" case.
                liste[row][col] = "N"
                liste[row + 1][col] = "N"

                success4 = backtrack_solver(liste, row, col + 1, restrict_nums)

                # Control the nums is valid or not for restritct_nums with control function.
                # if it is not valid return False.
                if not success4 or not control(liste, restrict_nums):
                    # if all possibilities are wrong change the cell's with original cell's and return False.
                    liste[row][col] = initial1
                    liste[row + 1][col] = initial2
                    return False

    return backtrack_solver(liste, row, col + 1, restrict_nums)


# function to write board to open.txt and turn it into string.
# if there is no answer it returns "No solution!".
def print_solution(valley_board, c, out):
    count = 0
    k = len(valley_board)
    if c == False:
        out.write("No solution!")
    else:
        for row in valley_board:
            count = count + 1
            out.write(" ".join(row))
            if count < len(valley_board):
                out.write("\n")


def main():
    # file was opened and inputs were entered intoe 2 files as restrict_nums and board_blind_vally.
    file = open(sys.argv[1], "r")
    text = file.readlines()
    file.close()

    new_text = []
    new_text_final = []
    for i in text:
        if "\n" in i:
            new_text.append(i[:-1])
        else:
            new_text.append(i)
    for j in new_text:
        new_text_final.append(j.split())
    # restrict_nums list consist  given numbers.
    # board_blind_valley list consist original letters.
    restrict_nums = new_text_final[:4]
    board_blind_valley = new_text_final[4:]

    # call function in 0,0 position.
    row = 0
    col = 0
    c = backtrack_solver(board_blind_valley, row, col, restrict_nums)

    out = open(sys.argv[2], "w")
    print_solution(board_blind_valley, c, out)
    out.flush()
    out.close()


if __name__ == '__main__':
    main()