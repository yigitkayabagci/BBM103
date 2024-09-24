import sys

""" Recursive function that finds suitable neighboring numbers and replaces them with "a"."""
def find_appropriate_a(gamelist, rownum, colnum):
    # rowlenght which represents long of row.
    global rowlenght
    # a_counter variable to find score.
    global a_counter

    a_counter += 1
    original_value = gamelist[rownum][colnum]
    gamelist[rownum][colnum] = "a"
    """Recursive function to call find_appropriate_a function when find a valid number."""
    def discover_numbers(ax, ay):
        if 0 <= ax < len(gamelist) and 0 <= ay < rowlenght and gamelist[ax][ay] == original_value and gamelist[ax][ay] != "a":
            find_appropriate_a(gamelist, ax, ay)
    
    # Call discover_neighbors function for every direction.

    discover_numbers(rownum, colnum-1)
    discover_numbers(rownum, colnum+1)
    discover_numbers(rownum-1, colnum)
    discover_numbers(rownum+1, colnum)

    return gamelist


"""number list for upside function."""
number = []
for ab in range(101):
    number.append(ab)

# Variable to control function (upside).
ctupside = 0
""" Function that replaces "a" with the number above to make numbers with spaces below them fall below."""
def upside(gamelist):
    # rowlenght which represents long of row.
    global rowlenght
    global ctupside
    global number
    ctupside = ctupside + 1
    if ctupside > 400:
        return gamelist
    else:
        for row in range(1, len(gamelist)):
            for col in range(rowlenght):
                if gamelist[row][col] == "a" and gamelist[row - 1][col] in str(number):
                    gamelist[row][col], gamelist[row - 1][col] = gamelist[row - 1][col], gamelist[row][col]
                    upside(gamelist)
                else:
                    continue
    return gamelist


""" Function that converts a list to a string visualizes the game board. 
also candy_crush function converts all "a" to " " when visualizing the board."""
def candy_crush(board):
    birstr = ""
    for row in board:
        birstr += "\n"
        for num in row:
            birstr += num + " "
        birstr = birstr.rstrip()

    new_str = ""
    for char in birstr:
        if char == 'a':
            new_str += ' '
        else:
            new_str += char

    return new_str

# Function that shifts the numbers in the game by deleting rows and columns consisting only of "a"
def adjust_final_places(gamelist):
    long_ofcol = len(gamelist)
    long_ofrow = len(gamelist[0])

    ctmover = 0
    while ctmover < long_ofcol:
        row_is_all_a = True
        for element in gamelist[ctmover]:
            if element != "a":
                row_is_all_a = False
                break

        if row_is_all_a:
            gamelist.pop(ctmover)
            long_ofcol -= 1
        else:
            ctmover = ctmover + 1

    num = 0
    while num < long_ofrow:
        column_is_all_a = True
        for i in range(long_ofcol):
            if gamelist[i][num] != "a":
                column_is_all_a = False
                break

        if column_is_all_a:
            for row in gamelist:
                row.pop(num)
            long_ofrow -= 1
        else:
            num += 1

    return gamelist


# Part for opening input file and put the input numbers in final_result_list.
inp = open(sys.argv[1], "r")
text = inp.read()
inp.close()

trylist = text.split("\n")
long = len(trylist)
final_result_list = [trylist[i].split() for i in range(long)]

""" Function to check if the game is over or not."""
def kontrol(gamelist):
    """ if countwhile is bigger than 0, there are some possibilities for playing game."""
    countwhile = 0
    # if all columns and rows deleted, return False and print Game over in final while statement.
    if gamelist == []:
        return False
    c = len(gamelist[0])
    row_count = len(gamelist)

    for r_element in range(row_count):
        for c_element in range(c):
            selected_number = gamelist[r_element][c_element]
            if selected_number == "a":
                continue
            else:
                if r_element > 0 and selected_number == gamelist[r_element - 1][c_element]:
                    countwhile += 1
                if r_element < row_count - 1 and selected_number == gamelist[r_element + 1][c_element]:
                    countwhile += 1
                if c_element > 0 and selected_number == gamelist[r_element][c_element - 1]:
                    countwhile += 1
                if c_element < c - 1 and selected_number == gamelist[r_element][c_element + 1]:
                    countwhile += 1

    return countwhile


""" Function that checks whether the value entered has a neighbor next to it or not."""
def has_same_neighbor(board, rownum, colnum):
    rowlong, collong = (len(board), len(board[0]))

    if 0 <= rownum < rowlong and 0 <= colnum < collong:
        selected_number = board[rownum][colnum]

        possible_movements = [(rownum - 1, colnum), (rownum + 1, colnum), (rownum, colnum - 1), (rownum, colnum + 1)]

        for neighbor_row, neighbor_col in possible_movements:
            if (0 <= neighbor_row < rowlong and 0 <= neighbor_col < collong and
                    board[neighbor_row][neighbor_col] == selected_number):
                return False

    return True


rowlenght = len(final_result_list[0])
print(candy_crush(final_result_list))
print("\nYour score is: 0")

finalscore = 0
a_counter = 0

# While loop that contains all functions and all variables also, take inputs and print outputs.
while True:
    if kontrol(final_result_list) > 0:
        # take input from user and split it.
        a, b = input("\nPlease enter a row and a column number: ").split()
        a = int(a)
        b = int(b)
        alast = a - 1
        b_last = b - 1

        # if statement which controls if the numbers is in the bounds or not.
        if alast < 0 or alast >= len(final_result_list) or b_last < 0 or b_last >= len(final_result_list[0]):
            print("\nPlease enter a correct size!")
            continue

        # con variable to keep selected number.
        con = final_result_list[alast][b_last]

        rowlenght = len(final_result_list[alast])
        # if statement for whether selected grid is empty or not.
        if final_result_list[alast][b_last] == "a":
            print("\nPlease enter a correct size!")
            continue

        # if statement to check if the same number is around or not.
        if has_same_neighbor(final_result_list, alast, b_last):
            print("\nNo movement happened try again")
            print(candy_crush(final_result_list))
            print("\nYour score is: {}".format(finalscore))
            continue

        final_result_list = find_appropriate_a(final_result_list, alast, b_last)

        # part for find score and put in it finalscore variable.
        score = int(con) * int(a_counter)
        finalscore = int(score) + int(finalscore)

        # upside and adjust_final_places function to arrange final list.
        final_result_list = upside(final_result_list)
        final_result_list = adjust_final_places(final_result_list)

        # reset counting.
        a_counter = 0
        ctupside = 0

        # print final board and finalscore.
        print(candy_crush(final_result_list))
        print("\nYour score is: {}".format(finalscore))
    else:
        print("\nGame over")
        break
