class BagNode():

    def __init__(self, data, children=None):

        self.data = data
        self.children = children or []

    def __repr__(self):
        return '<Node {data}>'.format(data=self.data)


class BagGraph():

    def __init__(self):
        self.nodes = set()
    
    def __repr__(self):
        return f'<BagGraph: { {n.name for n in self.nodes} }>'
    
    def add_bag(self, bag):
        self.nodes.add(bag)
    
    def set_bag_child(self, parent_bag, child_bag):
        parent_bag.adjacent.add(child_bag)
