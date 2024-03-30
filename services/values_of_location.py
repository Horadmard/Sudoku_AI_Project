

def value_of_location(*, sudoku: list, location: list) -> list:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(location)
    if not(location == []):
        row = location[0]
        col = location[1]
        
        for i in range(9) :
            number = sudoku[row][i]
            if number in numbers :
                numbers.remove(number)



        for i in range(9) :
            number = sudoku[i][col]
            if number in numbers :
                numbers.remove(number)   


        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3) :
            for j in range(3) :
                number = sudoku[i + start_row][j + start_col]
                if number in numbers :
                    numbers.remove(number)
        

        if numbers == [] :
            return None
        else :
            return numbers
    else:
        return None    
    



    
# test
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# loc = [8,0]
# print(value_of_location(sudoku=board,location=loc))