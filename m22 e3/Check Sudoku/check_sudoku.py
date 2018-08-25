'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in range(9):
        l = lst[i]
        if "".join(l.sort()) != "123456789":
            return False
    for i in range(9):
        l = []
        for j in range(9):
            l.append(lst[j][i])
        if "".join(sorted(l)) != "123456789":
            return False

    if "".join(sorted(lst[0][0]+lst[0][1]+lst[0][2]+ lst[1][0]+ lst[1][1]+lst[1][2]+lst[2][0]+lst[2][1]+lst[2][2]))!= "123456789":
        return False
    if "".join(sorted(lst[0][3]+lst[0][4]+lst[0][5]+ lst[1][3]+ lst[1][4]+lst[1][5]+lst[2][3]+lst[2][4]+lst[2][5]))!= "123456789":
        return False  
    if "".join(sorted(lst[0][6]+lst[0][7]+lst[0][8]+ lst[1][6]+ lst[1][7]+lst[1][8]+lst[2][6]+lst[2][7]+lst[2][8]))!= "123456789":
        return False 
    if "".join(sorted(lst[3][0]+lst[3][1]+lst[3][2]+ lst[4][0]+ lst[4][1]+lst[4][2]+lst[5][0]+lst[5][1]+lst[5][2]))!= "123456789":
        return False
    if "".join(sorted(lst[3][3]+lst[3][4]+lst[3][5]+ lst[4][3]+ lst[4][4]+lst[4][5]+lst[5][3]+lst[5][4]+lst[5][5]))!= "123456789":
        return False  
    if "".join(sorted(lst[3][6]+lst[3][7]+lst[3][8]+ lst[4][6]+ lst[4][7]+lst[4][8]+lst[5][6]+lst[5][7]+lst[5][8]))!= "123456789":
        return False
    if "".join(sorted(lst[6][0]+lst[6][1]+lst[6][2]+ lst[7][0]+ lst[7][1]+lst[7][2]+lst[8][0]+lst[8][1]+lst[8][2]))!= "123456789":
        return False
    if "".join(sorted(lst[6][3]+lst[6][4]+lst[6][5]+ lst[7][3]+ lst[7][4]+lst[7][5]+lst[8][3]+lst[8][4]+lst[8][5]))!= "123456789":
        return False
    if "".join(sorted(lst[6][6]+lst[6][7]+lst[6][8]+ lst[7][6]+ lst[7][7]+lst[7][8]+lst[8][6]+lst[8][7]+lst[8][8]))!= "123456789":
        return False
    return True

    n = 9
    lst = []
    for _ in range(n):
        lst.append(input().split())
    print(check(lst))

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
    