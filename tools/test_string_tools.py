from tools.string_tools import StringTools

def test_upper_case():
    st = StringTools("Hello world")
    assert st.upper() == 'HELLO WORLD'

    
def test_lower_case():
    st = StringTools("Hello world")
    assert st.lower() == "hello world"
