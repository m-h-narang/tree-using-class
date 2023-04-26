class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        # self.parent = None

    def add_child(self, child):
        # child.parent = self
        self.children.append(child)

    def get_routes(self, target):
        routes = []
        self._get_routes_helper(target, [self.value], routes)
        return routes

    def _get_routes_helper(self, target, path, routes):
        if self.value == target:
            routes.append(path)
        for child in self.children:
            child_path = path + [child.value]
            child._get_routes_helper(target, child_path, routes)

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)

root.add_child(node2)
root.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node3.add_child(node6)
node3.add_child(node7)
node4.add_child(node8)
node4.add_child(node9)
node5.add_child(node10)
node5.add_child(node11)
node6.add_child(node13)
node7.add_child(node14)

routes = root.get_routes(13)
print(routes) 
