

def cross_product(A, D):
    '''
    this function returns a list of cross product of elements of two lists
    taken as a parameter
    '''
    return [a + d for a in A for d in D]




'''
this section labels every square of a sudoku of size 9X9

Rows are labeled as alphabets and columns are labeled numbers

variable square contains the labels of each square/location of the sudoku

dependents section of the code stores the locations in the sudoku whose values 
are generally affected by a particular cell

'''


digits = '123456789'
rows = 'ABCDEFGHI'
columns = digits
squares = cross_product(rows, columns)
dependents_all = ([cross_product(rows, c) for c in columns]+[cross_product(r, columns) for r in rows]+[cross_product(r, c) for r in ('ABC', 'DEF', 'GHI') for c in ('123', '456', '789')])
dependents = dict((s, [u for u in dependents_all if s in u]) for s in squares)
dependents_distinct = dict((s, set(sum(dependents[s], [])) - set([s])) for s in squares)




def state_values(grid):
    
    
    '''
    This function associates values to the labels of each cell of the sudoku.
    '''
    
    values = [v for v in grid if v in digits or v in '0.']
    assert len(values) == 81
    return dict(zip(squares, values))





def initialize_sudoku(grid):
    
    
    """
    This function assigns the initial values assigned to the particular cell of the sudoku
    and assigns all the other cell to all the possible values they can have in their cell
    the function returns false if any contradiction is being observed in the values assigned to the cells
    """
    
    
    values = dict((s,digits) for s in squares)  #has all the values from 1-9

    for square,digit in state_values(grid).items(): 
        if digit in digits and not assign(values, square, digit):   #assigns the initial values to the cell
            return False
    return values





def eliminate(values, square, digit):
    
    
    
    """
    This function removes the digit from the cell
    
    if it has been found that after removing that digit only one digit is left in the cell
    then all the instances of that digit in the dependents are eliminated
    
    if it is found that a value can be kept in a particular location
    in all the possible dependents than that value is assigned there
    
    the function returns false if any contradiction is being observed in the values assigned to the cells
    """
    
    
    
    if digit not in values[square]:
        return values
    
    values[square] = values[square].replace(digit, '')
    
    
    if len(values[square]) == 0:
        return False
    elif len(values[square]) == 1:
        ev = values[square]
        if not all(eliminate(values, associated_squares, ev) for associated_squares in dependents_distinct[square]):
            return False
    
    
    for dependent in dependents[square]:
        possible_places = [sq for sq in dependent if digit in values[sq]]
        if len(possible_places) == 0:
            return False
        elif len(possible_places) == 1:
            if not assign(values, possible_places[0], digit):
                return False
    return values






    
def assign(values, square, digit):
    
    
    
    """
    This function assigns the value to the cell and eliminates other values
    and returns false if contradiction occurs
    """
    
    
    other_values = values[square].replace(digit, '')
    if all(eliminate(values, square, ev) for ev in other_values):
        return values
    else:
        return False






def solve(grid):
    
    
    '''
    this function solves  the sudoku passed as a parameter
    returns values of each of the cell
    returns false if contradiction occures
    '''
    
    return search(initialize_sudoku(grid))






def search(values):
    
    
    
    """
    This function checks the cell with minimum possible values it can accumulate
    and assigns a value from that and checks if the sudoku violates or not
    returns the first uncontradicted sudoku
    returns false if no such sudoku found
    """
    
    
    
    if values is False:
        return False
    

    if all(len(values[square]) == 1 for square in squares):
        return values
    
    
    
    possible_values_count,square = min((len(values[square]), square) for square in squares if len(values[square]) > 1)
    
    return first_sol(search(assign(values.copy(), square, digit)) for digit in values[square])





def first_sol(all_soln):
    
    
    
    """
    The function returns first non contradicting solutions
    of all the possible solutions of sudoku
    """
    
    
    for sol in all_soln:
        if sol:
            return sol
    return False




def display(values):
    
    
    '''
    The function is used to display sudoku
    '''


    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in columns))
        if r in 'CF': 
            print(line)
    print()




def main():
    prob=".2..........7.................5.........................4..............9.......1."
    display(state_values(prob))
    display(solve(prob))


if __name__ == '__main__':
    main()
