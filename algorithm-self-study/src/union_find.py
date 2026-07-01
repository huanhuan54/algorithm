class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.component_size = [1] * size
        self.components = size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)

        if first_root == second_root:
            return False

        if self.component_size[first_root] < self.component_size[second_root]:
            first_root, second_root = second_root, first_root

        self.parent[second_root] = first_root
        self.component_size[first_root] += self.component_size[second_root]
        self.components -= 1
        return True

    def connected(self, first, second):
        return self.find(first) == self.find(second)

    def count_components(self):
        return self.components
