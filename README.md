# install virtualenv
Linux
pip3 install virtualenv

# Create virtualenv
Linux
virtualenv "Name"
Example
virtualenv .env

# Activate "virtualenv"
source env/bin/activate

# Install file: Example "requirements.txt"
pip install -r "Name file"
Example
pip install -r requirements.txt

# =====================================================

# install pipenv
Linux
pip3 install pipenv

# Install package in "pipenv"
pipenv install "Name pacake"
Example
pipenv install colorama

# Uninstall package in "pipenv"
pipenv uninstall "Name pacake"
Example
pipenv uninstall colorama

# Install package <dev> in "pipenv"
pipenv install "Name pacake"
Example
pipenv install colorama

# Install file: Example "requirements.txt"
pipenv install -r "Name file"
Example
pipenv install -r requirements.txt

# Graph
pipenv graph

# Bug module
pipenv check

# Install module "Pipfile"
pipenv install

# Update "Pipfile.lock"
pipenv lock

# Ignore "Pipfile" | Install "Pipfile.lock"
pipenv install --ignore-pipfile

# Exit & Enter "Virtual Enviroment"
pipenv shell

# Delete "Virtual Enviroment"
pipenv --rm

# Reset "Virtual Enviroment"
pipenv shell