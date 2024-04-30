list = []

COUNT = 5

for i in range(COUNT):
    number = int(input())
    list.append(number)

sorted_list = sorted(list, reverse=True)

for el in sorted_list:
    print(el)
