"""Test Sample"""
import importlib
from src_{{cookiecutter.package_name}}.entrypoint import run


def test_exposed():
    """Test package level exposed apis."""
    package = importlib.import_module('src_{{cookiecutter.package_name}}')
    assert hasattr(package, '__version__')
    assert hasattr(package, '__author__')


def test_welcome_message():
    """Test entrypoint function with welcome message"""
    wlc_msg = run()
    assert wlc_msg == "Hello Python Package!"
