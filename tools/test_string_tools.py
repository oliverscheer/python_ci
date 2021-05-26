from tools import string_tools

def test_upper_case():
    st = string_tools.StringTools("Hello world")
    assert st.upper() == 'HELLO WORLD'

    
def test_lower_case():
    st = string_tools.StringTools("Hello world")
    assert st.lower() == "hello world"


# def test_lower_case_fail():
#     st = string_tools.StringTools("Hello world")
#     assert st.lower() == "hello WORLD"