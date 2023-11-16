test_cases = int(input())
print
for i in range(test_cases):
    T = input()    
    if T == T[0].upper:
        print(T[0])
    else:
        print(T.lower)
