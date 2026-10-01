# Basic arithmetic
print(15 + 7) # → 22
print(15 - 7) # → 8
print(15 * 7) # → 105
# Division always gives float in Python 3
print(7 / 2) # → 3.5 (float)
print(4 / 2) # → 2.0 (float, not 2!)
# Floor division — rounds DOWN always
print(17 // 5) # → 3 (not 3.4)  gives the integer part only 3 dinxa
print(-17 // 5) # → -4 (rounds DOWN, not towards zero!)
# Modulus — the remainder after floor division
print(17 % 5) # → 2 (17 = 3×5 + 2) gives es the remainder
print(10 % 2) # → 0 (10 divides evenly — no remainder)
print(7 % 2) # → 1 (7 is odd)
# Exponentiation
print(2 ** 10) # → 1024 2 ko power 10
print(64 ** 0.5) # → 8.0 (square root)
print(27 ** (1/3)) # → 3.0 (cube root)







# Basic comparisons
print(10 == 10) # → True
print(10 != 5) # → True
print(10 > 20) # → False

# Chained comparisons — unique to Python, reads like maths
x = 5
print(1 < x < 10) # → True (x is between 1 and 10)
print(0 <= x <= 5) # → True
print(5 < x < 10) # → False (x is not greater than 5)

# String comparisons — lexicographic (letter by letter)
print("apple" < "banana") # → True ('a' < 'b' in Unicode)
print("Python" == "python") # → False (case-sensitive!)

# Comparing booleans with numbers
print(1 == True) # → True (True equals 1 in Python)
print(0 == False) # → True (False equals 0 in Python)
print(1 == "1") # → False (int and str are different types)




# Compound assignment operators
score = 50
score += 10 # score is now 60
score *= 2 # score is now 120
score -= 20 # score is now 100
print(score) # → 100
# Multiple assignment — assign several variables in one line
a = b = c = 0 # all three become 0
print(a, b, c) # → 0 0 0
# Tuple unpacking — assign different values in one line
x, y, z = 1, 2, 3
print(x, y, z) # → 1 2 3
# Swap variables — Pythonic way, no temporary variable needed
a, b = 10, 20
a, b = b, a # swap!
print(a, b) # → 20 10

