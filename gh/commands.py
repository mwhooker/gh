from github import Github

import ghconfig


def get_github(args):
    config = ghconfig.get_config(args)
    gh_args = {}
    if 'token' in config:
        gh_args['login_or_token'] = config['token']
    if 'base_url' in config:
        gh_args['base_url'] = config['base_url']

    return Github(**gh_args)

def ls(parser, subparser):
    """ls <repo>

    TODO: flags for controlling output
    """

    subparser.add_argument('resource', help="name of user or organization.")
    subparser.add_argument('--org', action='store_true',
                        help="list repos for an org.")
    args = parser.parse_args()

    gh = get_github(args)
    if args.org:
        repos = gh.get_organization(args.resource).get_repos()
    else:
        repos = gh.get_user(args.resource).get_repos()
    for i in repos:
        print i.clone_url
