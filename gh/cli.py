import argparse
import os
import sys

from github import Github

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
    assert len(sys.argv) > 1

    base_url = os.getenv('GH_BASE_URL')

    if base_url:
        gh = Github(base_url=base_url)
    else:
        gh = Github()
    cmd = sys.argv[1]

    parser = argparse.ArgumentParser(description='cmd')

    commands[cmd](gh, parser, sys.argv[2:])
