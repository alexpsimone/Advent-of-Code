if __name__ == '__main__':
    data = open('10-data.txt', 'r')

# are there ever duplicate values?

# probably want to order the list from smallest to largest
adapters = []

for line in data:
    line.strip()
    adapters.append(int(line))
    adapters.sort()

print(adapters)

# initialize 0 instances of 1-jolt difference
one_jolt_diff = 0
# initialize 0 instances of 1-jolt difference (don't need yet but might for part 2)
two_jolt_diff = 0
# initialize 1 instance of 3-jolt difference, because the built-in adapter has a 3-jolt difference to start
three_jolt_diff = 1

# increment the first adapter difference to the 0 jolt wall adapter
if adapters[0] == 1:
    one_jolt_diff += 1
elif adapters[0] == 2:
    two_jolt_diff += 1
elif adapters[0] == 3:
    three_jolt_diff += 1
else:
    print('***************** something is broken *****************')

# from first (lowest rated) charger to last (highest rated) charger
for count in range(len(adapters)-1):

    # look in a window of 2 chargers
    # calculate difference in joltage rating between the chargers
    difference = adapters[count + 1] - adapters[count]
    # if that difference is 1, the increment the 1-jolt counter, etc
    if difference == 1:
        one_jolt_diff += 1
    elif difference == 2:
        two_jolt_diff += 1
    elif difference == 3:
        three_jolt_diff += 1
    else:
        # if the difference is greater than 3 or less than 1, then send a warning, because something has probably gone wrong.
        print('***************** something is broken *****************')


# return the number of each differences found
print(one_jolt_diff, three_jolt_diff, one_jolt_diff*three_jolt_diff)