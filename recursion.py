def fibonacci_memo(n, memo=None):
    # If the value is already calculated, return it
    if memo is None:
        memo = {}
    # If the value is not calculated, calculate it and store it
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result
    
    return result


def catalan_recur(n: int) -> int:
    # Base Case
    if n <= 1:
        return 1 
    # Recursive Case
    result = 0 
    for i in range(n):
        result += catalan_recur(i) * catalan_recur(n-i-1)

    return result


def catalan_memo(n, memo=None):
    # If the value is already calculated, return it
    if memo is None:
        memo = {}
    # If the value is not calculated, calculate it and store it
    if n in memo:
        return memo[n]
    # Recursion
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += catalan_memo(i, memo) * catalan_memo(n-i-1, memo)
        memo[n] = result
        return result


def catalan_tabu(n):
    # Base Case
    if n == 0:
        return 1 
    # Table to store results of subproblems
    table = [None] * (n+1)
    # Initialise first value in table
    table[0] = 1
    # Fill entries in table using recursive formula
    for i in range (2, n+1):
        table[i] = 0
        for j in range(i):
            table[i] += catalan_memo(j) * catalan_memo(i-j-1)
    return table[n]


print(catalan_recur(3))
print(catalan_memo(3))
print(catalan_tabu(3))

