from itertools import product
from constraint import Problem


def solve_sudoku():
    # Create a problem instance
    problem = Problem()

    # Define the domain of values (1-9) for each variable (empty cell)
    domain = list(range(1, 10))

    # Create variables for each cell in the Sudoku grid
    variables = list(product('ABCDEFGHI', '123456789'))

    for variable in variables:
        problem.addVariable(variable, domain)

    # Define constraints for rows
    for row in 'ABCDEFGHI':
        problem.addConstraint(lambda *args: len(set(args))
                              == 9, [row + str(i) for i in '123456789'])

    # Define constraints for columns
    for col in '123456789':
        problem.addConstraint(lambda *args: len(set(args))
                              == 9, [''.join((row, col)) for row in 'ABCDEFGHI'])

    # Define constraints for 3x3 blocks
    for block in product('ABC', '123'):
        cells = [row + col for row, col in product(
            'ABCDEFGHI', '123456789') if row in block[0] and col in block[1]]
        problem.addConstraint(lambda *args: len(set(args)) == 9, cells)

    # Find the solution
    solutions = problem.getSolutions()

    if solutions:
        # Print the first solution (there might be more)
        for row in 'ABCDEFGHI':
            print(" ".join(str(solutions[0][row + str(col)])
                  for col in '123456789'))
    else:
        print("No solution found")


if __name__ == '__main__':
    solve_sudoku()
