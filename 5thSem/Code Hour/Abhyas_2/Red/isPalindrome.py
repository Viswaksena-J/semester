t = int(input())
for _ in range(t):
    number = input()
    print("Yes" if str(number) == str(number)[::-1] else "No")
