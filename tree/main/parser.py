import re


def parse(command):
    """
    :param command:string Get command to parse.
    :return:dict Dictionary of actions to take.
    """
    re_spec = [
        ('show', r'\s*(?:sh|show)\s+(?P<sh_cmd>node_count|leaf_count|height|delta)\s*'),
        ('node',
         r'\s*(?:n|node)\s+(?P<n_n>0|[1-9][0-9]{0,10})\s+'
         r'(?P<n_cmd>type|degree|level|parent|children|siblings|descendant)\s*'),
        ('path', r'\s*(?:p|path)\s+(?P<p_n1>0|[1-9][0-9]{0,10})\s+(?P<p_n2>0|[1-9][0-9]{0,10})\s*'),
        ('save', r'\s*(?:s|save)\s+"(?P<s_f>.+)"(?:\s+(?P<s_m>list|matrix))?\s*'),
        ('help', r'\s*(?:h|help)(?:\s+(?P<h_cmd>show|node|path|save|help|exit))?\s*'),
        ('exit', r'\s*exit|quit|e|q\s*'),
        ('mismatch', r'.')
    ]
    regex = '|'.join('(?P<%s>%s)' % pair for pair in re_spec)  # make a big regex pattern
    m = re.search(regex, command)

    if m is None or m.lastgroup == 'mismatch':
        raise ParsingException(command)  # couldn't match input

    res = {
        'cmd': m.lastgroup  # base property for all commands
    }
    res.update({  # additional properties for each command
                   'show': {'inf': m.group('sh_cmd')},
                   'node': {'node': m.group('n_n'), 'inf': m.group('n_cmd')},
                   'path': {'n1': m.group('p_n1'), 'n2': m.group('p_n2')},
                   'save': {'file': m.group('s_f'), 'mode': m.group('s_m')},
                   'help': {'c': m.group('h_cmd')},
                   'exit': {}
               }[res['cmd']])
    return res


class ParsingException(Exception):
    """
        Raised when a parsing exception occurs.
    """

    def __init__(self, command):
        super(ParsingException, self).__init__('Invalid Command: ' + command)
