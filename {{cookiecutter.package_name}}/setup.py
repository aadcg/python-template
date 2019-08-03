"""Setup {{cookiecutter.package_name}} as a package."""

import setuptools

setuptools.setup(
    name="{{cookiecutter.package_name}}",
    description="{{cookiecutter.package_description}}",
    version="{{cookiecutter.package_version}}",
    url="git@gitlab.com:{{cookiecutter.gitlab_account}}/{{cookiecutter.package_name}}.git",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    packages=["src_{{cookiecutter.package_name}}"],
    # add here the python libraries you need for your program when you're done
    # with the development!
    install_requires=[
        # "pandas==0.23.0",
        # "numpy==1.14.3",
        # "scipy==1.1.0"
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.package_name}}_run=src_{{cookiecutter.package_name}}.entrypoint:run"
        ]
    },
)
