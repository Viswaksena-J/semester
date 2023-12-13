array = list(map(int,input().split()))
print(array)
no_duplics = set(array)
# # number = int(input())
# def hi(number):
#     for j in number:
#         frequency(j)

# count = 0

# def frequency(array):
#     for i in range(len(array)):
#         if array[i] == number:
#             count = count+1

#     print(count)   
# hi(no_duplics)
for i in no_duplics:
    print(f"number: {i} frequency: {array.count(i)}")
