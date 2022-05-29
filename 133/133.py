class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solution(node):

    output = Node(node.val)

    visited = []

    def bfs(node=Node, pointer=Node):

        global visited
        visited.append(node.val)

        if node.val in visited:
            pass
        else:
            for neighbor in pointer.neighbors:
                node.neighbors.append(Node(neighbor.val))

                bfs()

        return None

    return None

