def dfsCycle(node, visited, edges):
    if node in visited:
        return True
    visited.add(node)
    for next in edges[node]:
        if dfsCycle(next, visited, edges):
            return True

    # need to backtrack since we are modifying the visited set
    # and we need to mark the node as not visited again for next iterations
    visited.remove(node)

def cycleInGraph(edges):
    visited = set()
    for edge in range(len(edges)):
        if dfsCycle(edge, visited, edges):
            return True
    return False