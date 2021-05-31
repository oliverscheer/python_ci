""" some tools """

class StringTools:
    """ some string tools """

    def __init__(self, val):
        print("val", val)
        self.val = val

    def upper(self):
        """ returns upper string """
        return self.val.upper()

    def lower(self):
        """ returns lower string """
        return self.val.lower()
