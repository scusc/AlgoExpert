def twoColorable(edges):
    colors = [None]*len(edges)
    colors[0] = True
    for node, connectedNodes in enumerate(edges):
        if node in connectedNodes:
            return False
        if colors[node] is None:
            colors[node] = True
        for connectedNode in connectedNodes:
            if colors[connectedNode] is None:
                colors[connectedNode] = not colors[node]
            elif colors[connectedNode] == colors[node]:
                return False
    return True 

