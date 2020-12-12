# this might be a graph problem
# this also feels quite recursive!

if __name__ == '__main__':
    data = open('7-data.txt', 'r')

bags_dict = {}

# go line by line through the text file
for line in data:
    # split up the line using space as a delimeter
    words = line.split(' ')
    # the first two words make up the unique key
    key_bag = words[0] + ' ' + words[1]

    if words[4] == 'no':
        bags_dict[key_bag] = []
        bags_dict[key_bag].append('no other bags')
    else:
        num_child_bags = int(len(words[4:]) / 4)

        for count in range(num_child_bags):

            if key_bag in bags_dict:
                bags_dict[key_bag].append(words[5 + (4 * count)] + ' ' + words[6 + (4 * count)])
            else:
                bags_dict[key_bag] = []
                bags_dict[key_bag].append(words[5 + (4 * count)] + ' ' + words[6 + (4 * count)])


# now, recurse!
def recurse_bags(bag_name, bags_dict):
    
    gold_bag_exists = False

    if bag_name == 'no other bags':
        return

    # case: "shiny gold"
    elif bag_name == "shiny gold":
        gold_bag_exists = True
    
    else:
        # other cases: see what is contained in the child bags
        bag_children = bags_dict[bag_name]
        for child in bag_children:
            recurse_bags(child, bags_dict)

    return gold_bag_exists

num_options = 0

for bag in bags_dict.keys():
    print(bag)

    gold_bag_exists = recurse_bags(bag, bags_dict)
    if gold_bag_exists:
        num_options += 1
        print(num_options)

