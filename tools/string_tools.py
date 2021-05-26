# string tools

class StringTools:
    def __init__(self, val):
        print("val", val)
        self.val = val

    def upper(self): 
        str = self.val
        str = str.upper()
        return str

    def lower(self): 
        str = self.val
        str = str.lower()
        return str