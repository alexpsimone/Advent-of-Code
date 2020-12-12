data = open('3-data.txt')

map_orig = []

for line in data:
    line = line.rstrip()
    map_orig.append(line)

num_lines = len(map_orig)
horiz_needed = num_lines / 2 + 1
num_reps_needed = round(horiz_needed/len(map_orig[0])) + 1

for count in range(len(map_orig)):
    map_orig[count] = map_orig[count]*num_reps_needed

horiz_position = 1
tree_count = 0

for line in map_orig[2::2]:

    
    if line[horiz_position] == '#':
        tree_count += 1
    horiz_position += 1
    # print(horiz_position, tree_count)

print(tree_count)



