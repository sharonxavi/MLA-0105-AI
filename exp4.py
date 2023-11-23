from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_chars = set(''.join(words))
    if len(unique_chars) > 10:
        return "Invalid input: More than 10 unique characters"
    
    for perm in permutations('0123456789', len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if '0' not in [mapping[word[0]] for word in words if len(word) > 1]:
            equation = ' + '.join(word.translate(str.maketrans(mapping)) for word in words[:-1]) + f" == {words[-1].translate(str.maketrans(mapping))}"
            if eval(equation):
                return mapping
    return "No solution found"

puzzle = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(puzzle)
if isinstance(solution, dict):
    print("Solution found:")
    for key, value in solution.items():
        print(f"{key} = {value}")
else:
    print(solution)
