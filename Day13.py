import numpy as np
with open("Day13.txt", "r") as f:
    bus_file = f.read()
busses = bus_file.split('\n')

frequencies = busses[1].split(',')

solution_found = False
multiplier = int(100000000000000 / int(frequencies[0]))
while solution_found == False:
    for i in range(1, len(frequencies)):
        start_time = int(frequencies[0]) * multiplier
        if frequencies[i] == 'x':
            continue
        else:
            print(f'Start_Time= {start_time}')
            print(f'Frequency= {frequencies[i]}, Item: {i}')
            print(f'Offset: {int(frequencies[i])*(int(start_time/int(frequencies[i]))+1)-start_time}')
            if int(frequencies[i]) * (int(start_time / int(frequencies[i])) + 1) - start_time == i:
                solution_found = True
                continue
            else:
                solution_found = False
                break

    if solution_found == True:
        print(start_time)
    multiplier += 1


