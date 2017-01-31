#Some string manipulation tests

# process a list of course prerequisites into a simple flat list
# some courses at UQ have complex prereqs which I don't want to store so I just
# want to simplify that list even it if means loosing the data
string = "(ECON2010 + 2020) or ((7002 or 7010 or 7011 or 7110) + 7020 or 7021))"
def list_simplifier(string):
    string = string.replace(" or ", " + ")
    for each in ['(',')','}','}']:
        string = string.replace(each, '')
    print(string)

    return string.split(" + ")

list_simplifier(string)