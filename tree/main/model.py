class NodeNotFoundError(Exception):
    def __init__(self, num):
        super(NodeNotFoundError, self).__init__("Couldn't find node #" + num + ".")


class Tree:
    """
        Models a tree.
        Has adjacency matrix along with adjacency list.
        Stores node count and other useful information (such as number of leaf nodes).
        Multiple methods to get data from the tree.
    """
    adj_mtx = []
    adj_list = []
    size = 0
    nodes = []
    l_num = 0
    h = -1
    d = -1

    def __init__(self, adj_mtx):
        """
        Constructor
        :param adj_mtx:list<string> initial adjacency matrix for graph.
        """
        super().__init__()
        self.adj_mtx = adj_mtx
        self.size = len(adj_mtx)
        if self.size > 0:
            self.nodes.append(Node(None, 0))
            self._init_node(adj_mtx[0], self.nodes[0])  # starts to build the tree starting from root node

        for node in self.nodes:  # generate adjacency list
            l = self.find_children(node)
            if node.parent is not None:
                l.append(node.parent)  # finding neighbors
            neighbors = list(map(lambda n: int(n.num), l))
            neighbors.sort()
            neighbors = list(map(lambda n: str(n), neighbors))
            self.adj_list.append('%d %s' % (node.num, (','.join(neighbors))))
        self.adj_list.sort(key=lambda s: int(s[:s.index(" ")]))  # sorting the final list

    def _init_node(self, mtx_row, parent):
        """
        :param mtx_row:string Matrix row corresponding to the current node
        :param parent:Node Parent of this node.
        :return:void
        """
        for idx, val in enumerate(mtx_row):
            if val == '1' and len(list(filter(lambda n: n.num == idx, self.nodes))) == 0:
                node = Node(parent, int(idx))
                self.nodes.append(node)
                self._init_node(self.adj_mtx[int(idx)], node)  # call this function on all neighbors

    def get_node(self, num):
        """
        :param num:int
        :return:Node the node which number is equal to num
        """
        if 0 <= int(num) <= self.size:
            for node in self.nodes:
                if node.num == int(num):
                    return node
        raise NodeNotFoundError(num)

    def num_leaves(self):
        """
        :return:int number of leaf nodes
        """
        if self.l_num != 0:  # storing this number for future reference. (need not to calculate it twice)
            return self.l_num

        for n in self.nodes:
            if n.is_leaf:
                self.l_num += 1

        return self.l_num

    def height(self):
        """
        :return:int height of tree
        """
        if self.h != -1:
            return self.h

        for n in self.nodes:
            l = n.level()
            if l > self.h:
                self.h = l

        return self.h

    def delta(self):
        """
        :return:int maximum degree
        """
        if self.d != -1:
            return self.d

        for n in self.nodes:
            deg = n.deg
            if deg > self.d:
                self.d = deg

        return self.d

    def find_children(self, node):
        """
        :param node:Node the given node
        :return:list<Node> all children of the specified node
        """
        l = []
        for n in self.nodes:
            if n.parent == node:
                l.append(n)
        l.sort(key=lambda e: e.num)
        return l

    def find_siblings(self, node):
        """
        :param node:Node the given node
        :return:list<Node> all siblings of the specified node
        """
        l = []
        for n in self.nodes:
            if n.parent == node.parent:
                l.append(n)
        l.sort(key=lambda e: e.num)
        return l

    def find_descendants(self, node):
        """
        :param node:Node the given node
        :return:list<Node> all descendants of the specified node
        """
        l = []
        for n in self.nodes:
            if n.is_descendant(node):
                l.append(n)
        l.sort(key=lambda e: e.num)
        return l

    def find_path(self, n1, n2):
        """
        :param n1:Node first node
        :param n2:Node second node
        :return:list<Node> find path from first node to second node
        """
        p1 = n1.path_to_root()
        p2 = n2.path_to_root()
        last_node = self.nodes[0]
        while len(p1) > 0 and len(p2) > 0 and p1[-1] == p2[-1]:
            last_node = p1.pop()
            p2.pop()
        p1.append(last_node)
        p = p1
        p.extend(list(reversed(p2)))
        return p


class Node:
    """
        This class models each node of the tree.
        has number (for identification).
        stores its parent node. (None for the root)
        Has methods for easy access.
    """
    num = 0
    parent = None
    is_leaf = True
    deg = 0

    def __init__(self, parent, num):
        """
        :param parent:Node parent of this node.
        :param num:int identification number of this node.
        """
        super().__init__()
        self.parent = parent
        if parent is not None:
            parent.is_leaf = False  # parent node is not a leaf anymore.
            parent.deg += 1  # update parent's degree
            self.deg += 1
        self.num = num

    def level(self):
        """
        :return:int distance from root
        """
        l = 0
        p = self.parent
        while p is not None:
            p = p.parent
            l += 1

        return l

    def is_descendant(self, ancestor):
        """
        :param ancestor:Node another node
        :return:boolean is this node descendant of the specified node
        """
        p = self.parent
        while p is not None:
            if p == ancestor:
                return True
            p = p.parent

        return False

    def path_to_root(self):
        """
        :return:list<Node> path from this node to the root node
        """
        l = [self]
        p = self.parent
        while p is not None:
            l.append(p)
            p = p.parent
        return l
