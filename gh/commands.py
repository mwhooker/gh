import os

from github import Github


def get_github(args):
    gh_args = {}
    if args.token:
        gh_args['login_or_token'] = args.token
    base_url = os.getenv('GH_BASE_URL')
    if base_url:
        gh_args['base_url'] = base_url

    return Github(**gh_args)

def ls(parser):
    """ls <repo>
    
    TODO: flags for controlling output
    """

    parser.add_argument('resource', help="name of user or organization.")
    parser.add_argument('--org', action='store_true',
                        help="list repos for an org.")
    args = parser.parse_args()
    print args
    gh = get_github(args)
    if args.org:
        repos = gh.get_organization(args.resource).get_repos()
    else:
        repos = gh.get_user(args.resource).get_repos()
    for i in repos:
        print i.clone_url
