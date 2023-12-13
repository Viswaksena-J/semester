inse = int(input())
flag = False
for i in range(2,inse):
    if inse%i == 0:
        flag = True
        break
        
if flag == True:
    print("Not Prime")
else:
    print(" Prime")