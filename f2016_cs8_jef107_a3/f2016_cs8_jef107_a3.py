#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: avoid at all cost globals
#


# This function is responsible for processing the file. It opens the file and tests ignores the headers
# "Name, Distance. If the name is in the list, the function will update the record in all three lists by first
# deleting the original entry and re-adding the new entry. If the name is not found, then the new record is added
# to all three lists. This function will return two values: distance and file lines
def processFile(fName):
    file_distance = 0.0
    file_lines = cnt = 0
    try:
        fh = open(fName, 'r')
        # MN: you could have counted the lines just by running a counter in the following for loop
        #     therefore saving some reading from file
        file_lines = len(fh.readlines())
        fh.seek(0)
        for line in fh:
            cnt = 0
            if not "distance" in line:
                #data = fh.readline()
                #file_distance = sum( \
                    #float([item.strip('\n').split(',')[1] for item in data]))
                temp = line.split(',')
                name = (temp[0].strip())
                dist = float(temp[1])
                # if found, update data, not found, append

                if name in name_list:
                    # We have to find the person
                    position = name_list.index(name)
                    # Extract the original data
                    orig_cnt = int(count_list[position])
                    orig_dist = float(distance_list[position])

                    orig_cnt += 1
                    orig_dist += dist

                    # Need to delete the person from all three list in order to
                    # update the record
                    # MN: you could have just update the position in the list with the new value
                    del name_list[position]
                    del distance_list[position]
                    del count_list[position]

                    # Adding the new updated record to all three lists
                    name_list.append(name)
                    distance_list.append(orig_dist)
                    count_list.append(orig_cnt)
                # If name not found, add the name to the three lists: name, distance, and number of times the name
                # appeared (count)
                else:
                    cnt += 1
                    name_list.append(name)
                    distance_list.append(dist)
                    count_list.append(cnt)
                file_distance += dist
        fh.close()
    except FileNotFoundError:
        print('File <', line, '> not found.', end='')
    return file_distance, file_lines

# Initializing the three lists
# MN: you are using these 3 variables as globals
#     DO NOT USE GLOBALS unless it is the only way
name_list = []
count_list = []
distance_list =[]


# Main Program
try:
    # Assigning the specified filename to the masterFile variable. Then opening the file in read mode
    # MN: why not asking the user for the master list file name
    masterFile = "f2016_cs8_a3.data.txt"
    masterListFO = open(masterFile, 'r')

    # Setting up counters
    total_files = total_lines = 0
    total_distance = 0.0

    # Using a for loop to process the files given in the master file
    for fileName in masterListFO:
        total_files += 1
        fileName = fileName.strip()
        # Using the processFile function created above to process the files specified in the master file
        distance, lines = processFile(fileName)

        # Accumulating the distances and the total lines of all the files
        total_distance += distance
        total_lines += lines

    # Creating and formatting the output for the number of input files read, number of lines read
    # and total distance run.
    print('\n', end='')
    print("Number of Input files read".ljust(30), ":", format(total_files, '10'))
    print("Number of lines read".ljust(30), ":", format(total_lines, '10'))
    print('\n', end='')
    print("total distance run".ljust(30), ":", format(total_distance, '10.5f'))
    print('\n', end='')

    # Using the max and min function to find the greatest and least distance ran by individuals.
    # Finding the position of the maximum distance and then finding the corresponding name in order to determine who
    # ran the most and who ran the least.
    print("max distance run".ljust(30), ":", format(max(distance_list), '10.5f'))
    position = distance_list.index(max(distance_list))
    print("  by participant".ljust(30), ":", format(name_list[position], '10'))
    print('\n', end='')


    # Finding the position of the minimum distance and then finding the corresponding name
    print("min distance run".ljust(30), ":", format(min(distance_list), '10.5f'))
    position = distance_list.index(min(distance_list))
    print("  by participant".ljust(30), ":", format(name_list[position], '10'))
    print('\n', end='')


    # Creating and formatting the output for the total number of participants acculmulated from all three
    # files.
    print("Total number of participants".ljust(30), ":", format(len(name_list), '10'))
    cnt = 0

    # Using a for loop to go through all the values in the count list and an if statement to test whether the
    # value is greater than 1. If the value is greater than one, this indicates that the person has multiple records,
    # so he/she is added to the cnt variable. The cnt variable indicates the number of participants with
    # multiple records.
    for i in count_list:
        if i > 1:
            cnt += 1
    print("Number of participants")
    print("  with multiple records".ljust(30), ":", format(cnt, '10'))

    # MN: I would close the file as soon as I'm done with the reading
    masterListFO.close()


    try:
        cnt = 0
        # Creating the outfile that contains the name, total distance, and count for each record from all three
        # files.
        outfile = 'f2016_cs8_jef107_a3.data.output.csv'
        outfileFO = open(outfile, 'w')
        for i in name_list:
            line = name_list[cnt] + ',' + str(count_list[cnt]) + ',' + str(distance_list[cnt])
            outfileFO.write(line)
            outfileFO.write('\n')
            cnt += 1
        outfileFO.close()
    except:
        print('Outfile <', outfileFO, '> Error.', end='')


except FileNotFoundError:

    print('Master File <', masterFile, '> not found.', end='')






