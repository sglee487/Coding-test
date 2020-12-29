class Tree:

    def __init__(self, nodeinfo):
        self.mynode = max(nodeinfo, key=lambda x: x[1])
        leftchildren = [e for e in nodeinfo if e[0] < self.mynode[0]]
        rightchildren = [e for e in nodeinfo if e[0] > self.mynode[0]]

        self.leftchild = None
        if leftchildren:
            self.leftchild = Tree(leftchildren)

        self.rightchild = None
        if rightchildren:
            self.rightchild = Tree(rightchildren)


def travel(node, preorder, lastorder):
    preorder.append(node.mynode)
    if node.leftchild:
        travel(node.leftchild, preorder, lastorder)
    if node.rightchild:
        travel(node.rightchild, preorder, lastorder)
    lastorder.append(node.mynode)


def solution(nodeinfo):
    N = len(nodeinfo)
    preorder = []
    lastorder = []
    root = Tree(nodeinfo)
    travel(root, preorder, lastorder)
    result = []
    result.append([nodeinfo.index(e) + 1 for e in preorder])
    result.append([nodeinfo.index(e) + 1 for e in lastorder])
    return result


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]),[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]])