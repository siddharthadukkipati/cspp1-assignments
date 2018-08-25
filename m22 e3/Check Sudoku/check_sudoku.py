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
    sudoku = list_12
    for i in range(9):
        lis_1 = list_12[i]
        if "".join(lis_1.sort()) != "123456789":
            return False
    for i in range(9):
        lis_1 = []
        for j in range(9):
            lis_1.append(list_12[j][i])
        if "".join(sorted(lis_1)) != "123456789":
            return False

    if "".join(sorted(list_12[0][0]+list_12[0][1]+list_12[0][2]+ list_12[1][0]+ list_12[1][1]+list_12[1][2]+list_12[2][0]+list_12[2][1]+list_12[2][2])) != "123456789":
        return False
    if "".join(sorted(list_12[0][3]+list_12[0][4]+list_12[0][5]+ list_12[1][3]+ list_12[1][4]+list_12[1][5]+list_12[2][3]+list_12[2][4]+list_12[2][5])) != "123456789":
        return False  
    if "".join(sorted(list_12[0][6]+list_12[0][7]+list_12[0][8]+ list_12[1][6]+ list_12[1][7]+list_12[1][8]+list_12[2][6]+list_12[2][7]+list_12[2][8])) != "123456789":
        return False 
    if "".join(sorted(list_12[3][0]+list_12[3][1]+list_12[3][2]+ list_12[4][0]+ list_12[4][1]+list_12[4][2]+list_12[5][0]+list_12[5][1]+list_12[5][2])) != "123456789":
        return False
    if "".join(sorted(list_12[3][3]+list_12[3][4]+list_12[3][5]+ list_12[4][3]+ list_12[4][4]+list_12[4][5]+list_12[5][3]+list_12[5][4]+list_12[5][5])) != "123456789":
        return False  
    if "".join(sorted(list_12[3][6]+list_12[3][7]+list_12[3][8]+ list_12[4][6]+ list_12[4][7]+list_12[4][8]+list_12[5][6]+list_12[5][7]+list_12[5][8])) != "123456789":
        return False
    if "".join(sorted(list_12[6][0]+list_12[6][1]+list_12[6][2]+ list_12[7][0]+ list_12[7][1]+list_12[7][2]+list_12[8][0]+list_12[8][1]+list_12[8][2])) != "123456789":
        return False
    if "".join(sorted(list_12[6][3]+list_12[6][4]+list_12[6][5]+ list_12[7][3]+ list_12[7][4]+list_12[7][5]+list_12[8][3]+list_12[8][4]+list_12[8][5])) != "123456789":
        return False
    if "".join(sorted(list_12[6][6]+list_12[6][7]+list_12[6][8]+ list_12[7][6]+ list_12[7][7]+list_12[7][8]+list_12[8][6]+list_12[8][7]+list_12[8][8])) != "123456789":
        return False
    return True

    num_n = 9
    list_12 = []
    for _ in range(num_n):
        list_12.append(input().split())
    print(check_sudoku(list_12))

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
