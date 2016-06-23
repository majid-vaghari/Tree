from main.model import Tree


class InvalidInputError(Exception):
    """
        Raised when input file is not valid.
    """
    def __init__(self):
        super(InvalidInputError, self).__init__("Input File Invalid or doesn't exist.")


def load(filename):
    """
    :param filename:string Name of the adjacency matrix file.
    :return:Tree A tree object.
    """
    try:
        f = open(filename)
    except FileNotFoundError:
        raise InvalidInputError

    adj = f.read().splitlines()  # read all lines from file

    size = len(adj)
    for row in adj:
        if len(row) != size or set(row) != {'0', '1'}:  # check to see if input file is a valid matrix
            raise InvalidInputError

    deg_sum = 0
    for idx, row in enumerate(adj):
        for str_idx, char in enumerate(row):
            if char != adj[str_idx][idx]:  # check to see if the matrix is symmetric
                raise InvalidInputError
            deg_sum += char == '1'

    if (deg_sum / 2) + 1 != size:  # check to see if it's a tree
        raise InvalidInputError

    f.close()

    t = Tree(adj)
    if t.size != len(t.nodes):  # check to see if the graph is connected
        raise InvalidInputError

    return t
