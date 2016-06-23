from sys import argv

from main import action
from main.load import load, InvalidInputError
from main.model import NodeNotFoundError
from main.parser import parse, ParsingException

if __name__ == '__main__':  # main function
    filename = ''  # getting filename from user
    if len(argv) == 2:
        if argv[1] in ['h', 'help', '--help', '-h', '--usage']:  # show help message if user asked for it
            print(action.help_string())
            exit(0)
        filename = argv[1]
    else:
        filename = input('Please enter filename: ')

    t = None
    try:
        t = load(filename)  # trying to load tree
    except InvalidInputError as e:
        print(str(e))
        exit(1)  # sets exit code to 1

    cmd = ''
    while cmd != 'exit':  # reading input till user decides to exit
        try:
            command = input('>> ')
        except EOFError:
            exit(0)
        else:
            try:
                res = parse(command)  # parsing the command
                cmd = res['cmd']
                print({
                          'show': lambda: action.show(t, res['inf']),
                          'node': lambda: action.node(t, res['node'], res['inf']),
                          'path': lambda: action.path(t, res['n1'], res['n2']),
                          'save': lambda: action.save(t, res['file'], res['mode']),
                          'help': lambda: action.hlp(res['c']),
                          'exit': lambda: 'bye.'
                      }[cmd]())  # calling the proper function based on user input
            except (ParsingException, NodeNotFoundError) as e:
                print(str(e))  # display an error
