countryNames = []
countryCodes = []

def read_csv(x):
    with open(x) as csv:
        lines = csv.readlines()
        return lines

def parse_csv(x):
    for i in x:
        new_list = i.split(",")
        countryNames.append(new_list[0])
        countryCodes.append(new_list[1])
    return countryNames, countryCodes;

def print_data(x,y):
    print ("- - - - -")
    for i in range(len(countryNames)):
        print ("- - - - -")
        print(x[i])
        print(y[i])

lines = read_csv("/home/student/program4/data.csv")
parse_csv(lines)
print_data(countryNames,countryCodes)