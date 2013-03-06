import argparse
import sys

import commands

commands = {
    'ls': commands.ls
}


"""
TODO:
    config file
        base_url
        oauth token
    base parser
        command
        all env opts
    allow options to be specified over args or env
"""

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--token')
    subparsers = parser.add_subparsers(help='sub-command help')
    command_parser = subparsers.add_parser('ls')

    gh = None

    commands[sys.argv[1]](parser)
