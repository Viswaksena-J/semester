n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

missing_numbers = []

for num in b:
    if num not in a:
        missing_numbers.append(num)
print(*missing_numbers)

