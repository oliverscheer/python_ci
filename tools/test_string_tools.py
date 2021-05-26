""" Tests to test string tools """
from tools import string_tools

def test_upper_case():
    """ Test upper case """
    tool = string_tools.StringTools("Hello world")
    assert tool.upper() == 'HELLO WORLD'


def test_lower_case():
    """ Test lower case """
    tool = string_tools.StringTools("Hello world")
    assert tool.lower() == "hello world"
