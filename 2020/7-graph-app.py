# class BagNode():

#     def __init__(self, data, children=None):

#         self.data = data
#         self.children = children or []

#     def __repr__(self):
#         return '<Node {data}>'.format(data=self.data)


# class BagGraph():

#     def __init__(self):
#         self.nodes = set()
    
#     def __repr__(self):
#         return f'<BagGraph: { {n.name for n in self.nodes} }>'
    
#     def add_bag(self, bag):
#         self.nodes.add(bag)
    
#     def set_bag_child(self, parent_bag, child_bag):
#         parent_bag.adjacent.add(child_bag)


if __name__ == '__main__':

    # make a dict of colors -> colors that can contain them
    
    bags_dict = {}

    for line in data:

        "drab silver bags contain no other bags."

        words = line.split()

        if words[4] != 'no':
            parent_bag = ' '.join(words[:2])
            child_bags = ' '.join(line[4:]).split(',')

            for child_bag in child_bags:
                #  " 5 bright gold bags" -> "5 bright gold bags"
                child_bag = ' '.join(child_bag.strip().split()[1:3])

                if child_bag in bags_dict:
                    bags_dict[child_bag].append(parent_bag)
                else:
                    bags_dict[child_bag] = [parent_bag]
    
    # we have to avoid cycles
    # initialize queue with 'shiny gold'

    queue = ['shiny gold']
    bags_seen = set()
    # while queue not empty
    while len(queue) > 0:     # while queue
    # check if first item in queue is in set
        if queue[0] not in bags_seen:
            # if not, loop throught values in bag_dict 
            for bag in bags_dict[queue[0]]:
                # for each value, check if in set
                if bag not in bags_seen:
                    # if not, append value to queue
                    queue.append(bag)
                    # pop first item off queue and add to set
                    bags_seen.add(queue.pop(0))