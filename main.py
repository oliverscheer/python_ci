""" test app for pytest and pylint """

from tools.string_tools import StringTools


def main():
    """ converts a text to lower """
    string_tool = StringTools("Hello World")
    print("Input: ", string_tool.val)
    print("lower: ", string_tool.lower())
    print("upper: ", string_tool.upper())

if __name__ == "__main__":
    main()
