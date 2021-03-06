import requests
import argparse
from . import __version__

from neydi._internals import _log

API = 'http://localhost:5000/api'


def neydi(query):
    return ' '.join(query)


def get_parser():
    parser = argparse.ArgumentParser(
        description='my sweet unforgetable commands (I forgot)')
    parser.add_argument('query', metavar='QUERY', type=str,
                        nargs='*', help='shows what you want')
    parser.add_argument('-n', '--new-user',
                        help='registers a new user', type=str)
    parser.add_argument(
        '-v', '--version', help='shows the last version of neydi', action='store_true')
    return parser


def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        print(__version__)

    if args.new_user:
        import os.path
        if os.path.isfile('p-key.pem'):
            _log('error', 'You are already registered!')
            return

        data = {"email": args.new_user}
        response = requests.post(f'{API}/new', json=data)
        # todo: check http response types
        # print(response.status_code)
        key_file = open("p-key.pem", 'w+')
        content = {
            'token':response.json()['token'],
            'key':response.json()['private-key']
        }
        import json
        json.dump(content, key_file)
        key_file.close()

        _log('info','''Hurrey! You are registered! Now, you can start to request for some cool commands. 

If you don\'t know what you are able to do, you can call \'neydi -h\' first''')
        return

    if not args.query:
        parser.print_help()
        return

    result = neydi(args.query)
    print(result)


if __name__ == '__main__':
    command_line_runner()
