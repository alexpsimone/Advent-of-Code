class Tree():

    def __init__(self, root):
        self.root = root

class Node():

    def __init__(self, data, children):

        self.data = data
        self.children = children or []

if __name__ == '__main__':
    data = open('7-data.txt', 'r')

first_bag = data[0]
for line in data:
    # split up the line using space as a delimeter
    words = line.split(' ')
    # the first two words make up the unique key
    key_bag = words[0] + ' ' + words[1]

    bag_node = Node(key_bag)

    if tree:


