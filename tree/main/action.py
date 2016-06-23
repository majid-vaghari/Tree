from main.help import help_command


def show(tree, cmd):
    """
    :param tree:Tree the tree object parsed from the input file.
    :param cmd:string the info user wants.
    :return:string info user wants
    """
    return {
        'node_count': lambda: str(tree.size),
        'leaf_count': lambda: str(tree.num_leaves()),
        'height': lambda: str(tree.height()),
        'delta': lambda: str(tree.delta())
    }[cmd]()


def node(tree, nd, cmd):
    """
    :param tree:Tree the tree object parsed from the input file.
    :param nd:Node Selected node by user.
    :param cmd:string the info user wants.
    :return:string info user wants
    """
    return {
        'type': lambda n: 'Leaf' if n.is_leaf else 'Internal',
        'degree': lambda n: str(n.deg),
        'level': lambda n: str(n.level()),
        'parent': lambda n: str(n.parent.num),
        'children': lambda n: ', '.join(list(map(lambda c: str(c.num), tree.find_children(n)))),
        'siblings': lambda n: ', '.join(list(map(lambda c: str(c.num), tree.find_siblings(n)))),
        'descendant': lambda n: ', '.join(list(map(lambda c: str(c.num), tree.find_descendants(n)))),
    }[cmd](tree.get_node(nd))


def path(tree, n1, n2):
    """
    :param tree:Tree the tree object parsed from the input file.
    :param n1:Node first node.
    :param n2:Node second node.
    :return:string path from first node to second one.
    """
    return ', '.join(list(map(lambda c: str(c.num), tree.find_path(tree.get_node(n1), tree.get_node(n2)))))


def save(tree, file, mode):
    """
    :param tree:Tree the tree object parsed from the input file.
    :param file:string file path to store tree.
    :param mode:string store adjacency matrix or adjacency list.
    :return:string whether or not the write was successful.
    """
    if mode == 'matrix':
        s = '\n'.join(tree.adj_mtx)
    else:
        s = '\n'.join(tree.adj_list)

    try:
        f = open(file, 'w')
        f.write(s)
        f.close()
    except IOError:
        return 'Error occurred.'
    else:
        return 'Saved.'


def hlp(cmd):
    """
    :param cmd:string command which user wants more information about.
    :return:string help text.
    """
    if cmd is None:
        cmd = ''
    return help_command(cmd)
