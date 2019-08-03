#!/bin/bash

# push to remote repo
git init
git add .
git commit -m 'Initial commit'
git push --set-upstream git@gitlab.com:{{cookiecutter.gitlab_account}}/{{cookiecutter.package_name}}.git master

# install virtual environment
conda env create -f dev_environment.yml
source activate {{cookiecutter.package_name}}_dev_env

# sphinx documentation
cd doc
sphinx-quickstart -q -a "{{cookiecutter.author_name}}" -p "{{ cookiecutter.package_name }}" -v "{{ cookiecutter.package_version}}"
cd