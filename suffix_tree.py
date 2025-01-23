class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indices = []

class SuffixTree:
    def __init__(self, sequence):
        self.root = SuffixTreeNode()
        self.sequence = sequence
        self._build_tree()

    def _build_tree(self):
        """Builds the suffix tree for the given sequence."""
        for start_index in range(len(self.sequence)):
            current = self.root
            for char in self.sequence[start_index:]:
                if char not in current.children:
                    current.children[char] = SuffixTreeNode()
                current = current.children[char]
                current.indices.append(start_index)

    def search(self, substring):
        """Search for a substring in the suffix tree and return its starting indices."""
        current = self.root
        for char in substring:
            if char not in current.children:
                return []  # Substring not found
            current = current.children[char]
        return current.indices

    def visualize(self, node=None, depth=0):
        """Visualize the suffix tree structure."""
        if node is None:
            node = self.root
        for char, child in node.children.items():
            print(f"{' ' * depth}{char}: {child.indices}")
            self.visualize(child, depth + 2)
