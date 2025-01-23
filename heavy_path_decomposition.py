class HeavyPathTreeNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.weight = 0
        self.children = []

class HeavyPathDecomposition:
    def __init__(self):
        self.nodes = {}
        self.heavy_paths = {}

    def add_node(self, node_id, parent_id=None, weight=1):
        """Adds a node to the tree."""
        if node_id not in self.nodes:
            self.nodes[node_id] = HeavyPathTreeNode(node_id)
        self.nodes[node_id].weight = weight
        if parent_id:
            if parent_id not in self.nodes:
                self.nodes[parent_id] = HeavyPathTreeNode(parent_id)
            self.nodes[parent_id].children.append(node_id)

    def find_heavy_paths(self):
        """Identify heavy paths by traversing the tree."""
        for node_id in self.nodes:
            if self.nodes[node_id].node_id == 1:  # Assuming node 1 is the root
                self._decompose(node_id)

    def _decompose(self, node_id, path=None):
        if path is None:
            path = []
        path.append(node_id)
        children = self.nodes[node_id].children
        if not children:
            self.heavy_paths[node_id] = path
            return
        heaviest = max(children, key=lambda x: self.nodes[x].weight)
        for child in children:
            if child != heaviest:
                self._decompose(child)
        self._decompose(heaviest, path)

    def display_paths(self):
        """Print heavy paths."""
        for path_id, path in self.heavy_paths.items():
            print(f"Heavy Path for Node {path_id}: {path}")
