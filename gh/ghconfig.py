import imp
import os.path
from collections import namedtuple

ConfigValue = namedtuple('ConfigValue', ('name', 'description'))

class NotPresentType(object):
    def __repr__(self):
        return "NotPresent"

NotPresent = NotPresentType()
BASE_CONFIG = (
    ConfigValue('token', 'github auth token'),
    ConfigValue('base_url', 'base uri to make api calls to.'),
    ConfigValue('config', 'config file to use.')
)

# TODO: make configurable
def get_from_file(name, path=None):
    """get config value from config file."""

    if path is NotPresent:
        path = '~/.pygh'

    if not hasattr(get_from_file, 'module'):
        path = os.path.expanduser(path)
        with open(path) as f:
            get_from_file.module = imp.load_module(
                'config',
                f,
                path,
                filter(lambda x: x[0] == '.py', imp.get_suffixes())[0]
            )

    return getattr(get_from_file.module, name.upper(), NotPresent)

def get_from_env(name):
    """get config from env.

    looks for upper cased version of ConfigValue.name and prepends GH_ to it.

    """
    return os.getenv("GH_%s" % name.upper(), NotPresent)


def get_config(args):
    """returns a dict of confg parameters.

    gathers sources, in this order, from
    1. ~/.pygh
    2. environment
    3. flags

    """
    config = {}

    for i in BASE_CONFIG:
        val = (
            get_from_file(i.name, args.config),
            get_from_env(i.name),
            getattr(args, i.name, NotPresent)
        )
        for v in val:
            if v == NotPresent:
                continue
            config[i.name] = v

    return config

def add_config_to_parser(parser):
    for c in BASE_CONFIG:
        parser.add_argument('--%s' % c.name, default=NotPresent,
                            help=c.description)
