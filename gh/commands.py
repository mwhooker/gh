def ls(gh, parser, args):
    """ls <repo>
    
    TODO: flags for controlling output
    """

    parser.add_argument('resource', help="name of user or organization.")
    parser.add_argument('--org', action='store_true',
                        help="list repos for an org.")
    args = parser.parse_args(args)
    if args.org:
        repos = gh.get_organization(args.resource).get_repos()
    else:
        repos = gh.get_user(args.resource).get_repos()
    for i in repos:
        print i.clone_url
