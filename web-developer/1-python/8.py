word_list = input().split(", ")

frequencies_dict = {}
for el in word_list:
    frequencies_dict[el] = frequencies_dict.get(el, 0) + 1

frequencies_list = []
for key, value in frequencies_dict.items():
    frequencies_list.append((value, key))

top_frequencies = sorted(frequencies_list, reverse=True)

for el in top_frequencies[:3]:
    print(f"{el[1]}: {el[0]}")
