number = int(input())

if number > 1:
    for i in range(2,int(number/2)+1):
        if number%i == 0:
            print("Not Prime")
    print("Prime")
else:
    print("Not Prime")