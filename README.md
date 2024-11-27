# MADS deployment

## install docker
Yes, docker is supposed to fix the "this runs on my machine" problem.
No, this doesnt mean that this is fixed for installing docker itself...

Please go to the [docker website](https://docs.docker.com) to check how you can install docker on your machine.
However, since we have access to Ubuntu VMs, I added a script that automates installation on a Ubuntu 22.04 server.

### VM instructions
1. Create a 'Ubuntu 22.04' VM with 1 core, 8GB of RAM.
2. Clone this repo
3. run `./install-docker.sh`

Then, setup up your VM as always.
You could use my script from `https://github.com/raoulg/serverinstall/` for that,
which can be run very simply by running
```bash
curl -sSL https://raw.githubusercontent.com/raoulg/serverinstall/refs/heads/master/generalserver.sh | bash
```
to install things like `zsh`, `eza`, `starship`, `rye`  and I add some aliases to the `.zshrc` file.
This script is still experimental, it is very opinionated and subject to frequent changes, but it improves my experience so
it might do the same for you. Of course, you can also make your own script, or do it manually.

## Under construction
Please note that this repository is under construction.
This means that you will find lesson-1, but lesson-2 is not there, yet.
Protip: keep the main branch clean, and if you think you need to modify things, do 
that in your own branch in such a way that you will be able to pull and merge updates:wq



