with open('devices.txt', 'r') as file:
    content = file.read()
status_list = eval(content)

#for i in status_list:
    #x = i[0]
    #if len(i) > 1 and len(i[1]) > 0:
        #print(i[1][1])
        #print(len(i[1][1]))

#mighty_dict = {}

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
    for i in status_list:
        province = i[0]
        print(province)

    print("please enter one of these cities")
    x = str(input())
    dict_general = dictionaryer(status_list)
    print(dict_general.get(x).keys())
    print("please select a switch")
    y = str(input())
    print(dict_general[x][y])
    print("\n")
    print("The full dictonary")
    print(dict_general)

finder()
