def help_string():
    """
        :return:string help for the user.
    """
    return """
Hello.
This is tree parser program used to pars, store and show information about trees.
First, you need to specify a file which contains the adjacency matrix of the tree you want.
Then you will enter a "shell-like" environment that you can execute commands in.
------------------------------

To use this program simply provide the specification file (adjacency matrix) as the first argument...
Or... don't :D it will automatically ask for it.

Usage:
    tree [filepath to adjacency matrix]

Enjoy.\n
    """


def help_command(command):
    """
    :param command:string Get specified command.
    :return:string help for the specified command.
    """
    return {
        '': """
Usage:
    command [options]

list of commands:
    show        Shows information you want.
    node        Shows specific information about the selected node.
    path        Shows the path between two given nodes.
    save        Saves tree in file.
    help        Shows this page.
    exit        Exits the program.

Enter "help <command name>" for detailed information on a specific command.
        """,
        'help': """
Usage:
    help [command name]
Description:
    shows help about the specified command. shows global help page when no command is selected.
        """,
        'show': """
Usage:
    show <tree information>
Tree information can be one of the following:
    node_count      Shows the number of nodes in tree.
    leaf_count      Shows the number of leaf nodes in tree.
    height          Shows tree height (length of the longest path from root to a leaf).
    delta           Shows the maximum degree of the nodes in the tree.
        """,
        'node': """
Usage:
    node <node number> <node information>
Node information can be one of the following:
    type            Shows node type (can be a leaf or internal node).
    degree          Shows node degree (number of attached edges).
    level           Shows node level (distance from root).
    parent          Shows immediate parent of this node.
    children        Shows the list of children.
    siblings        Shows the list of siblings.
    descendant      Shows the list of all descendants.
        """,
        'path': """
Usage:
    path <first node number> <second node number>
Description:
    pick two nodes and the "path" command will show you the path from first node to second node in the tree.
        """,
        'save': """
Usage:
    save "filepath" [save mode]
Description:
    saves the graph in a specified file. FILEPATH MUST BE IN QUOTES.
Save mode can be one of the following:
    list            Saves tree in form of adjacency list (default option).
    matrix          Saves tree in form of adjacency matrix.
        """,
        'exit': """
Usage:
    exit
Description:
    Exits the program.
        """
    }[command]
