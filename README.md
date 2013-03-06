gh
==

github api cli tool


Command reference
==

`ls <user>`

return list of repositories for `user`


Config
==

Config can either be specified as

1. in a config file. defaults to ~/.pygh
2. from the environment
3. as options to the command

The config is applied in the order above, so options will overwrite file config, etc.

values in the config file and the environment must be all uppercase version of the flags.
i.e. --base_url becomes BASE_URL.

values from the environment additionally have GH_ prepended to them.
i.e. --base_url becomes GH_BASE_URL
