with open('/Users/erenuludag/PycharmProjects/staj/venv/devices.txt', 'r') as file:
    content = file.read()
status_list = eval(content)

def dictionaryer(status_list):
    dict_turkey = {}

    for i in status_list:
        province = i[0]
        switch_interfaces = {}

        if len(i) > 1 and len(i[1]) > 0:
            for k in range(1, len(i)):
                switch_name = i[k][0]
                interfaces = i[k][1:]
                switch_interfaces[switch_name] = interfaces

        dict_turkey[province] = switch_interfaces

    return dict_turkey

def finder():
    dict_general = dictionaryer(status_list)
    provinces = [i[0] for i in status_list]

    print("Available cities:")
    for province in provinces:
        print(province)

    while True:
        x = input("Please enter one of the cities: ")
        if x in dict_general:
            break
        else:
            print("Invalid input. Please try again.")

    switch_names = dict_general.get(x, {}).keys()

    print(f"Available switches in {x}:")
    for switch_name in switch_names:
        print(switch_name)

    while True:
        y = input("Please select a switch: ")
        if y in switch_names:
            break
        else:
            print("Invalid input. ")

    print("Interface status: ")
    print(dict_general[x][y])


def dict_to_list(the_list):
    transformed_list = []
    for province, switches in the_list.items():
        transformed_list.append(province)
        for switch, interfaces in switches.items():
            transformed_list.append(switch)
            for interface in interfaces:
                transformed_list.append(interface)

    return transformed_list

new_list = dict_to_list(dictionaryer(status_list))
print(new_list)

def status_controller(dict_of_something):
    for i in dict_of_something:
        for j in dict_of_something.get(i):
            if len(dict_of_something.get(i).get(j)[0]) > 0:
                for k in range(len(dict_of_something.get(i).get(j)[0])):
                    if len(dict_of_something.get(i).get(j)[0][k]) >= 4:
                        if dict_of_something.get(i).get(j)[0][k][2] == "disabled" and dict_of_something.get(i).get(j)[0][k][3] == "enabled":
                            print(dict_of_something.get(i).get(j)[0][k])



print(dictionaryer(status_list))
new_list = dict_to_list(dictionaryer(status_list))
print(new_list)
status_controller(dictionaryer(status_list))
finder()
