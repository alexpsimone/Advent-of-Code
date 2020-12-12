data = open('6-data.txt')

customs = []
custom_set = set()
running_sum = 0

for line in data:
    line = line.rstrip()
    customs.append(line)

# check each line in the dataset
for line in customs:
# if the line has letters, then add the string to a set
    if line != '':
        for letter in line:
            custom_set.add(letter)
        # print(line, custom_set)
    else:
        # if the line is blank, then find the length (??) of the set
        # add this set to a running sum
        running_sum += len(custom_set)
        # print(len(custom_set), running_sum)
        # then empty the existing set
        custom_set = set()

print(f'running_sum: {running_sum}')


# work in a moving window of 2 lines
# create 2 sets with those 2 lines
# find the intersection of the sets, and make it equal to the 2ns set or something
# if one of the lines is empty, then don't perform the set math
# instead, find the length of the intersection, and reset it to empty

list_of_strings = []
list_of_sets = []
running_total = 0

for line in customs:

    if line != '':
        list_of_strings.append(line)
    else:
        print('*********************************************')
        
        set_intersection = set()
        set_intersection.update(list_of_strings[0])
        for line_in_list in list_of_strings[1:]:
            newset = set()
            newset.update(line_in_list)
            set_intersection = set_intersection.intersection(newset)
            
        running_total += len(set_intersection)
        print(list_of_strings, set_intersection, running_total)
        
        list_of_strings = []


        




        


