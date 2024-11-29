from collections import deque

class Node():
    
    def __init__(self, val=None, adj=[]):
        self.val = val
        self.adj = adj


def dfs(root):
    if not root:
        return []
    
    stack = [root]
    visited = set()
    result = []

    while stack:
        node1 = stack.pop()
        if node1 not in visited:
            visited.add(node1)
            result.append(node1.val)
            for n in node1.adj:
                stack.append(n)
    
    return result


def bfs(root):
    if not root:
        return []
    
    q = deque([root])
    visited = set()
    result = []

    visited.add(root)

    while q:
        node1 = q.popleft()  # Dequeue the front node
        result.append(node1.val)  # Add the node value to the result
        for n in node1.adj:
            if n not in visited:
                visited.add(n)
                q.append(n)  # Enqueue adjacent nodes to the back
    return result
    
    

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    # Establish connections
    node1.adj = [node5, node4, node2]
    node2.adj = [node1, node7, node3, node6]
    node3.adj = [node2]
    node4.adj = [node1]
    node5.adj = [node1]
    node6.adj = [node2]
    node7.adj = [node2]
    
    print('dfs')
    print(dfs(node1))
    print('bfs')
    print(bfs(node1))