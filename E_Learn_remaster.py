from os.path import isfile
from json import dumps, loads
from sys import argv


def learner(file, data):
    if type(data) is list:
        data = dumps(data)

    elif type(data) is dict:
        data = dumps(data)

    elif type(data) is int:
        data = str(data)

    else:
        pass

    if not isfile(file):
        new_data = {data: 5}
        with open(file, "w") as file_write_if_not_exist:
            new_data_final = dumps(new_data)
            file_write_if_not_exist.write(new_data_final)
    else:
        pass

    file_read = open(file, "r").read()
    file_open = loads(file_read)

    memory_list = []
    memory_amount = len(file_open)
    some_number = 0

    for i in file_open:
        memory_list.append(i)

    while True:
        if some_number >= memory_amount:
            break
        elif file_open[memory_list[some_number]] <= 1:
            del file_open[memory_list[some_number]]
            break
        else:
            pass

        some_number = some_number + 1

    for i in file_open:
        file_open[i] = file_open[i] - 1

    if data in file_open:
        
        if file_open[data] >= 70:
            file_open[data] = file_open[data] + 50
        
        else:
            file_open[data] = file_open[data] + 5
    else:
        file_open[data] = 5

    with open(file, "w") as writer:
        writer.write(dumps(file_open))


def retrive(file, memory):

    if type(memory) is list:
        memory = dumps(memory)

    elif type(memory) is dict:
        memory = dumps(memory)

    else:
        memory = str(memory)

    file_read = open(file, "r").read()
    file_final = loads(file_read)

    if memory not in file_final:
        return "I do not remember: " + memory

    else:
        point = file_final[memory]
        final_point = int(point / 3)
        return final_point


if __name__ == "__main__":
    
    try:
        learner(argv[1], argv[2])

    except IndexError:
        pass