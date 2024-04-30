def get_popular_name_from_file(filename):
    names = {}
    with open(filename) as f:
        for line in f:
            name = line.split()[0]
            names[name] = names.get(name, 0) + 1
    
    max_count = max(names.values())

    target_names = []
    for key, value in names.items():
        if value == max_count:
            target_names.append(key)
    
    target_names = sorted(target_names)
    string = ", ".join(target_names)
    return string

# print(get_popular_name_from_file("file.txt"))
