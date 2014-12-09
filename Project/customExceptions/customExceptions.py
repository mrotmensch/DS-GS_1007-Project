'''

Dec 1, 2014

@author: 

'''

class EmptyStringException(Exception):
    pass

class UnreadableData(Exception):
    pass

class NotInNYException(Exception):
    pass

class InvalidInputException(Exception):
    pass

class Address_not_valid(Exception):
    """This exeption is raised when the address the user provides can either not be converted or was found by the geocoder API to not be valid."""
    pass


    