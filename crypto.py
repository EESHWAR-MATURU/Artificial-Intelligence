from constraint import *


def solve_crypto_arithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set("".join(puzzle))

    # Create a problem instance
    problem = Problem()

    # Define domains for the letters (0-9)
    for letter in letters:
        problem.addVariable(letter, range(10))

    # Define the constraint: Sum of the left-hand side equals the right-hand side
    def crypto_constraint(*args):
        left_side = puzzle[:-4]
        right_side = puzzle[-4:]
        left_sum = sum(args[letters.index(letter)] for letter in left_side)
        right_sum = int(
            "".join(str(args[letters.index(letter)]) for letter in right_side))
        return left_sum == right_sum

    problem.addConstraint(crypto_constraint, letters)

    # Find the solution
    solutions = problem.getSolutions()

    if solutions:
        return solutions[0]  # Return the first solution found
    else:
        return None


# Example usage
puzzle = "SEND + MORE == MONEY"
solution = solve_crypto_arithmetic(puzzle)
if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
