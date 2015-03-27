#  Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
# OJ's undirected graph serialization:
#
# Nodes are labeled uniquely.
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
#
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
#     First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
#     Second node is labeled as 1. Connect node 1 to node 2.
#     Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        # Visit the whole graph, store all nodes in a dictionary
        constructed_nodes = {}
        seen_label = []

        new_node = UndirectedGraphNode(node.label)
        new_node.neighbors = node.neighbors
        constructed_nodes[new_node.label] = new_node
        stack = [new_node]
        while stack:
            cur_node = stack.pop()

            # Makr this node as seen
            seen_label.append(cur_node.label)

            # Check all neighbors
            new_neighbors = []
            for ori_neighbor in cur_node.neighbors:
                # Clone all neighbors to cur_node
                if ori_neighbor.label in constructed_nodes:
                    # Use previously constructed node
                    new_neighbor = constructed_nodes[ori_neighbor.label]
                else:
                    # Constrcut a new node
                    new_neighbor = UndirectedGraphNode(ori_neighbor.label)
                    new_neighbor.neighbors = ori_neighbor.neighbors
                    constructed_nodes[new_neighbor.label] = new_neighbor

                # Add into new_neighbors list
                new_neighbors.append(new_neighbor)

                # Push unseen node into stack
                if new_neighbor.label not in seen_label:
                    stack.append(new_neighbor)

            cur_node.neighbors = new_neighbors

        return new_node

node = UndirectedGraphNode(0)
node.neighbors = [node, node]

new_node = Solution().cloneGraph(node)
print id(new_node)
for neighbor in new_node.neighbors:
    print id(neighbor)
