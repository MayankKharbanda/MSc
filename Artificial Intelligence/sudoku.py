def cellidgenerator(X, Y):
    "Takes cross product of row id and column id"
    return [x + y for x in X for y in Y]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
cellids = cellidgenerator(rows, cols)
unitList = (
    [cellidgenerator(rows, c) for c in cols] + #generates column units
    [cellidgenerator(r, cols) for r in rows] + #generates row units
    [cellidgenerator(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')] #generates 9 box units
)
units = dict((s, [u for u in unitList if s in u]) for s in cellids)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in cellids)

### Parsing a Grid

def grid_values(grid):
    "Convers grid to a dictionary of {square: character} with '0' or '.' for not filled"
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(cellids, chars))

def parse_grid(grid):
    """
    Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected.
    """
    #Create a Dictionary where we assign each square all possible digits
    values = dict((s,digits) for s in cellids)

    #Assign proper values to those squares in Values Dict that already had value in grid.
    for s,d in grid_values(grid).items():
        #only doing this for non-empty elements of the grid
        if d in digits and not assign(values, s, d):
            return False #could not assign d to square s
    return values


### Constraint Propagation

def eliminate(values, s, d):
    """
    eliminate d from values[s], and propagate when values <= 2
    Return values, except retrun False if contradiction is detected
    """
    if d not in values[s]:
        return values #Already eliminated
    values[s] = values[s].replace(d, '')
    
    #if square only has one value, then eliminate that value from its peers
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
    #if a unit has only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values
    
def assign(values, s, d):
    """
    Assign values[s] with d, that is eliminating from values[s] all 
    except d and propagate it to its peers. 
    Return values, except retrun False if contradiction is detected
    """
    
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
    
    
def solve(grid):
    return search(parse_grid(grid))



def search(values):
    #check if a contradiction was found
    if values is False:
        return False
    #check if already solved
    if all(len(values[s]) == 1 for s in cellids):
        return values
    #choose the unfilled square with fewest remaining possible values
    n,s = min((len(values[s]), s) for s in cellids if len(values[s]) > 1)
    #recursively call search after assigning s to d(do this for each d in values[s])
    return some(search(assign(values.copy(), s, d)) for d in values[s])


#returning first of multiple true solution
def some(seq):
    for e in seq:
        if e:
            return e
    return False


# display sudoku
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in cellids)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)
    print()



def main():
    sudoku=input("Write grid for sudoku:-")
    display(solve(sudoku))

if __name__ == '__main__':
    main()