import random

# Objective function f(x)
def f(x):
    return -x**2 + 5*x + 10

# Hill Climbing Algorithm
def hill_climbing():
    # Set initial values
    current_node = random.uniform(-10, 10) # Current node (initial state): random value between -10 to 10
    step_size = 0.1 # Step size
    max_iterations = 1000 # Maximum iterations
    iteration = 0 # Iteration counter

    # Loop until max iterations are reached
    while iteration < max_iterations:
        # Calculate the current score
        current_score = f(current_node)

        # Evaluate the scores of neighboring nodes
        left_node = current_node - step_size
        left_score = f(left_node)

        right_node = current_node + step_size
        right_score = f(right_node)

        # Move to the neighboring node with the highest score
        if left_score > current_score:
            current_node = left_node
        elif right_score > current_score:
            current_node = right_node
        else:
            break # We have reached the top

        # Increment iteration counter
        iteration += 1

    return current_node

# Print the maximum value of f(x) found by Hill Climbing
print("Maximum value of f(x):", f(hill_climbing()))
