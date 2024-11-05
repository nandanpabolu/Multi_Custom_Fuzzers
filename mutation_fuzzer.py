import random
import subprocess

# Seed inputs
seed_inputs = [
    "1 + 2",
    "3 * (4 - 5)",
    "(6 / 2) + 8",
    "9 - (7 * 2)",
    "((1 + 3) * 2) / 4"
]

operators = ['+', '-', '*', '/']
digits = [str(i) for i in range(10)]
mutations = operators + digits + ['(', ')', ' ', '@', '#']

def mutate_expression(expr):
    expr_list = list(expr)
    mutation_type = random.choice(['insert', 'delete', 'replace'])
    pos = random.randint(0, len(expr_list) - 1)

    if mutation_type == 'insert':
        char = random.choice(mutations)
        expr_list.insert(pos, char)
    elif mutation_type == 'delete' and len(expr_list) > 1:
        expr_list.pop(pos)
    elif mutation_type == 'replace':
        char = random.choice(mutations)
        expr_list[pos] = char

    return ''.join(expr_list)

# Run mutations
for _ in range(10):
    seed = random.choice(seed_inputs)
    mutated_expr = mutate_expression(seed)
    try:
        result = subprocess.check_output(['python', 'calculator.py', mutated_expr], stderr=subprocess.STDOUT)
        print(f"Input: {mutated_expr} Output: {result.decode().strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Input: {mutated_expr} Error: {e.output.decode().strip()}")
