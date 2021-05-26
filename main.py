from tools.string_tools import StringTools


def main(): 
    st = StringTools("Hello World")
    print("Input: ", st.val)
    print("lower: ", st.lower())
    print("upper: ", st.upper())

if __name__ == "__main__":
    main()