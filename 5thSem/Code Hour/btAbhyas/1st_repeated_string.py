def first_repeating_character(s):
    char_frequency = {}

    for char in s:
        if char in char_frequency:
            return char
        else:
            char_frequency[char] = 1

    return -1

# Input
T = int(input())

for _ in range(T):
    # Taking input for each test case
    test_case = input()

    # Finding and printing the first repeating character
    result = first_repeating_character(test_case)
    print(result)
