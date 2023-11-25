sample = input()

modified = ""
for i in sample:
    if i not in "aeiouAEIOU":
       modified += i
print(modified)