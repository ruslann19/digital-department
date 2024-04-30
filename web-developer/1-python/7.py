word_list = input().lower().split(", ")

word_set = set(word_list)

word_list_sorted = sorted(list(word_set))

print(*word_list_sorted, sep=", ")
