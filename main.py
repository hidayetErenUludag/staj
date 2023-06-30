with open('/Users/erenuludag/PycharmProjects/staj/venv/devices.txt', 'r') as file:
    content = file.read()
status_list = eval(content)

#for i in status_list:
    #x = i[0]
    #if len(i) > 1 and len(i[1]) > 0:
        #print(i[1][1])
        #print(len(i[1][1]))

#mighty_dict = {}

def dictionaryer(list):
    for i in list:
        x = i[0]
        if len(i) > 1 and len(i[1]) > 0:
            dict_name = x
            for k in range(1, len(i)-1):
                if len(i[k][1]) > 0:
                    print(i[k][0])

dictionaryer(status_list)