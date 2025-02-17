import time
import numpy as np
import matplotlib.pyplot as graph  # Renamed plt to graph

# Iterative Fibonacci (fastest for large n)
def fibonacci_iterative(n):
    if n < 2:
        return [0] if n == 1 else [0, 1]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Recursive Fibonacci (inefficient for large n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Memoized Fibonacci (uses caching to speed up recursion)
def fibonacci_memoized(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Matrix exponentiation method (O(log n) time complexity)
def fibonacci_matrix(n):
    def multiply_matrices(A, B):
        return np.dot(A, B).astype(int)

    def matrix_power(matrix, exp):
        result = np.identity(len(matrix), dtype=int)
        while exp:
            if exp % 2:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            exp //= 2
        return result

    if n == 0:
        return 0
    base_matrix = np.array([[1, 1], [1, 0]], dtype=int)
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0, 0]

# Function to generate Fibonacci sequence using different algorithms
def generate_fibonacci(n, method="iterative"):
    if method == "iterative":
        return fibonacci_iterative(n)
    elif method == "recursive":
        return [fibonacci_recursive(i) for i in range(n)]
    elif method == "memoized":
        return [fibonacci_memoized(i) for i in range(n)]
    elif method == "matrix":
        return [fibonacci_matrix(i) for i in range(n)]
    else:
        raise ValueError("Unknown method")

# Function to measure execution time of Fibonacci methods
def measure_time(method, n):
    start = time.time()
    sequence = generate_fibonacci(n, method)
    return sequence, time.time() - start

# Function to plot Fibonacci sequences
def plot_fibonacci(sequences, labels):
    for seq, label in zip(sequences, labels):
        graph.plot(seq, marker='o', linestyle='-', markersize=6, label=label)
    graph.title('Fibonacci Algorithm Comparison')
    graph.xlabel('Index')
    graph.ylabel('Value')
    graph.legend()
    graph.grid(True)
    graph.show()

# Main function
def main():
    n = 20  # Number of Fibonacci numbers to generate
    
    # Measure time and get sequences
    iter_seq, iter_time = measure_time("iterative", n)
    memo_seq, memo_time = measure_time("memoized", n)
    matrix_seq, matrix_time = measure_time("matrix", n)
    
    # Recursive method is slow, only run for small n
    if n <= 20:
        rec_seq, rec_time = measure_time("recursive", n)
    else:
        rec_seq, rec_time = [], float('inf')

    # Print execution times
    print(f"Iterative time: {iter_time:.6f} sec")
    print(f"Memoized time: {memo_time:.6f} sec")
    print(f"Matrix time: {matrix_time:.6f} sec")
    if rec_seq:
        print(f"Recursive time: {rec_time:.6f} sec")

    # Plot results
    plot_fibonacci([iter_seq, memo_seq, matrix_seq], ["Iterative", "Memoized", "Matrix"])

if __name__ == "__main__":
    main()