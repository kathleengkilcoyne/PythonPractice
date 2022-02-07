#This test was provided by Test Dome as a Python employment test
#Test was acquired here: https://app.testdome.com/t?GeneratorId=46
#Implement a group_by_owners function that:
#1) accepts a dictionary containing the file owner name for each file
#2) returns a dictionary containing a list of file names for each owner name, in any order.
#For example, for dictionary {'input.txt':'Randy', 'code.py':'Stan', 'Output.txt':'Randy'}
#the group_by_owners function should return {'Randy':['input.txt',''output.txt'], 'stan':['Code.py']}
def group_by_owners(files):
    #create empty dictionary
    v = {}
    for key, value in sorted(files.items()):
        v.setdefault(value, []).append(key)
    return v


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))