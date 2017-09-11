import argparse
from . import __version__

def neydi(query):
    return ' '.join(query)

def get_parser():
    parser = argparse.ArgumentParser(
        description='my sweet unforgetable commands')
    parser.add_argument('query', metavar='QUERY', type=str,
                        nargs='*', help='shows what you want')
    parser.add_argument(
        '-v', '--version', help='shows the last version of neydi', action='store_true')
    return parser


def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        print(__version__)

    if not args.query:
        parser.print_help()
        return

    result = neydi(args.query)
    print(result)


if __name__ == '__main__':
    command_line_runner()
