# class Tree():

#     def __init__(self, root):
#         self.root = root

# class Node():

#     def __init__(self, data, children):

#         self.data = data
#         self.children = children or []

# if __name__ == '__main__':
#     data = open('7-data.txt', 'r')

# first_bag = data[0]
# for line in data:
#     # split up the line using space as a delimeter
#     words = line.split(' ')
#     # the first two words make up the unique key
#     key_bag = words[0] + ' ' + words[1]

#     bag_node = Node(key_bag)

#     if tree:

if __name__ == '__main__':

    # make a dict of colors -> colors that can contain them
    f = open('in.txt', 'r')
    bags_dict = {}

    for line in f:
        words = line.split()

        if words[4] != 'no':
            parent_bag = ' '.join(words[:2])
            child_bags = ' '.join(words[4:]).split(',')

            for child_bag in child_bags:
                #  " 5 bright gold bags" -> "5 bright gold bags"
                child_bag = ' '.join(child_bag.strip().split()[1:3])

                if child_bag in bags_dict:
                    bags_dict[child_bag].append(parent_bag)
                else:
                    bags_dict[child_bag] = [parent_bag]
    # print(bags_dict['muted white'])

    # we have to avoid cycles

    # initialize queue with 'shiny gold'

    queue = ['shiny gold']
    bags_seen = set()
    # while queue not empty
    while len(queue) > 0:     # while queue
        print(queue)
        # check if first item in queue is in set
        if queue[0] not in bags_seen and queue[0] in bags_dict:
            # if not, loop throught values in bag_dict 
            for bag in bags_dict[queue[0]]:
                # for each value, check if in set
                if bag not in bags_seen:
                    # if not, append value to queue
                    queue.append(bag)
        # pop first item off queue and add to set
        bags_seen.add(queue.pop(0))

    print(len(bags_seen))


