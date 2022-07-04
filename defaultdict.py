from collections import defaultdict

with open('colours.txt', 'r') as file:

    colours_list = []
    for line in file:
        colours_list.append(line.split()[1])

    colours_count = defaultdict(int)
    for colour in colours_list:
        colours_count[colour] += 1

print(colours_count)

