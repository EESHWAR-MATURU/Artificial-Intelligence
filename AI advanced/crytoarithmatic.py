import itertools


def solve_cryptarithmetic(puzzle):
    unique_chars = list(set("".join(puzzle)))

    if len(unique_chars) > 10:
        return None

    permutations = itertools.permutations("0123456789", len(unique_chars))

    for perm in permutations:
        char_to_digit = dict(zip(unique_chars, perm))

        if any(char_to_digit[word[0]] == '0' for word in puzzle):
            continue

        int_puzzle = [int("".join(char_to_digit[char]
                          for char in word)) for word in puzzle]

        if int_puzzle[0] + int_puzzle[1] == int_puzzle[2]:
            return char_to_digit

    return None


puzzle = ["SOME", "TIME", "SPENT"]
solution = solve_cryptarithmetic(puzzle)

if solution is not None:
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")
