"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""
def fibonacci(n):
    #initialize
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci( n - 2)

#test code
n = 6
print(fibonacci(n))
#Time O(n^2)
#2. Top down memorization approach DP (dynamic programming)

def fib_memo(n):
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    return f(n)

#test code
n = 6
print(fib_memo(n))
#Time O(n)
#Space O(n)

#3. Bottom up - Tabulation
def fib_BU(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i -2] + dp[i - 1]
    return dp[n]

#test code
n=6
print(fib_BU(n))
#Time O(n)
#Space O(n)

#Similar approach as BU but save more space issue
def fib_BUS(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev = 0
    cur = 1

    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    return cur

#Time O(n)
#Space O(1) 
#test code
n=6
print(fib_BUS(n))