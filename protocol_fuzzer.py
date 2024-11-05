import random
import subprocess

def generate_expression(depth=0):
    if depth > 3:
        return generate_number()
    expr = generate_term(depth)
    while random.choice([True, False]):
        op = random.choice([' + ', ' - '])
        expr += op + generate_term(depth)
    return expr

def generate_term(depth):
    term = generate_factor(depth)
    while random.choice([True, False]):
        op = random.choice([' * ', ' / '])
        term += op + generate_factor(depth)
    return term

def generate_factor(depth):
    if random.choice([True, False]):
        return '(' + generate_expression(depth + 1) + ')'
    else:
        return generate_number()

def generate_number():
    return ''.join(random.choices('0123456789', k=random.randint(1, 3)))

# Generate and test expressions
for _ in range(10):
    expr = generate_expression()
    try:
        result = subprocess.check_output(['python', 'calculator.py', expr], stderr=subprocess.STDOUT)
        print(f"Input: {expr} Output: {result.decode().strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Input: {expr} Error: {e.output.decode().strip()}")
