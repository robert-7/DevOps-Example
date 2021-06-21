# Setup

The steps below are should help you get set up on an Ubuntu system.

```bash
# install python 3 and dependencies
sudo apt update
sudo apt install -y \
    build-essential \                           # essentials for building
    libmysqlclient-dev \                        # needed for connecting to a mysql client
    libssl-dev libffi-dev \                     # handling TLS communication and function calls
    python3 python-dev python3-pip python3-venv # all the python goodies
    upx                                         # needed for pyinstaller

# ensure python 3 is the default python version
ALIASES="~/.bashrc"
cat >> ${ALIASES} << EOF

# python3 alias
alias python=python3
EOF
source ${ALIASES}
python --version

# clone repo
git clone git@github.com:robert-7/DevOps-Example.git
cd DevOps-Example

# set up virtualenv
python -m venv '.venv'
source .venv/bin/activate

# install requirements
pip install -r requirements.txt

# set up pre-commit so basic linting happens before every commit
pre-commit install
pre-commit run --all-files

# spinning up the environment requires docker and docker-compose:
# install docker: https://docs.docker.com/engine/install/ubuntu/
# install docker-compose: https://phoenixnap.com/kb/install-docker-compose-on-ubuntu-20-04
```

## Recurring

To deactivate or reactivate your virtual environment, simply run:

```bash
deactivate                # deactivates virtualenv
source .venv/bin/activate # reactivates virtualenv
```
