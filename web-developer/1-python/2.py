sum = 0
str = input()

while str != "":
    number = int(str)
    if number % 2 == 0:
        sum += number
    str = input()

print(sum)
