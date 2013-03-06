import argparse
import sys

import commands
import ghconfig

commands = {
    'ls': commands.ls
}


"""
TODO:
    commands
        notifications
        issues
            per repo
            globally
            assigned to me / open / etc.
        followers
        following
        leaders
        disciples
        ls
            ls [user|org|issues]?
"""

if __name__ == '__main__':
    parsers = {}

    parser = argparse.ArgumentParser()
    ghconfig.add_config_to_parser(parser)
    subparsers = parser.add_subparsers(help='sub-command help')

    for k in commands:
        parsers[k] = subparsers.add_parser(k)

    # will buy beer for anyone to show me how to do this better.
    cmd = set(commands.keys()).intersection(sys.argv)
    if not cmd or len(cmd) > 1:
        parser.parse_args()
    else:
        cmd = cmd.pop()
        commands[cmd](parser, parsers[cmd])
