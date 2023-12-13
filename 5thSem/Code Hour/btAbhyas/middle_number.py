# 2
# 20 30 40
# 12 32 11

test_cases = int(input())

for _ in range(test_cases):
    numbers = map(int,input().split())
    sort = sorted(numbers)
    print(sort[len(sort)//2])