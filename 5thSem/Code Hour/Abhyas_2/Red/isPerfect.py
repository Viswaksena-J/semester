import math

def is_perfect_number(n):
    sum_of_divisors = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i

    return sum_of_divisors == n

# Input reading
n = int(input().strip())

# Check if the given number is a perfect number
if is_perfect_number(n):
    print("Yes")
else:
    print("No")
