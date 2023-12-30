t = int(input())

def sena(t):
    for _ in range(t):
        number = int(input())
        fizzbuzz(number)

array = []

def fizzbuzz(number):
    for i in range(1,number+1):
        if i % 3 ==0:
            if i%3==0 and i%5==0:
                array.append("fizzbuzz")
            else:
                array.append("fizz")
        elif i%5==0:
            if i%3==0 and i%5==0:
                array.append("fizzbuzz")
            else:
                array.append("buzz")
        else:
            array.append(i)
    print(*array,sep='')
    array.clear()

sena(t)