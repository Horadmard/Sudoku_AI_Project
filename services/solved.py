from the_fullest_location import the_fullest_location
from update import update_with_value, update
from values_of_location import value_of_location
from stack import Stack


def solved_sudoku(*, sudoku: list, stack: Stack, stack_answer: Stack) -> list:
   
   tfl =  the_fullest_location(sudoku=sudoku)
   if tfl == None :
      return sudoku
   
   else :
      values = value_of_location(sudoku=sudoku, location=tfl)
      if not (values == None) :  
        for value in values :
           node = [tfl , value]
           stack.push(node)
        last = stack.pop()
        stack_answer.push(last)
        sudoku = update_with_value(sudoku=sudoku, location=last[0] , value=last[1])
        solved_sudoku(sudoku=sudoku, stack=stack,stack_answer=stack_answer)

      else :
        end_answer = stack_answer.pop()
        loc = end_answer[0]    
        sudoku = update(sudoku=sudoku,location=loc)
        solved_sudoku(sudoku=sudoku, stack=stack, stack_answer=stack_answer)



if __name__ == "__main__":
    sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    stack = Stack()
    astack = Stack()
    
    sudoku=solved_sudoku(sudoku=sudoku, stack=stack, stack_answer=astack)
   

   
    for s in sudoku:
        print(s)