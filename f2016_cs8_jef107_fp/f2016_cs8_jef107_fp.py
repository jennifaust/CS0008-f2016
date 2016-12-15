#
#
# name       : Jenni Faust
# email      : jef107@pitt.edu
# date       : 2016/12/15
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Final Project
#
# Description:
# A customer needs to process a number of text files (called data files) that contain names and
# distance run by study participants.


class DataFile:

    def __init__(self):
        # Initializing the two dictionaries
        self.name_dist_KV = {}
        self.name_count_KV = {}

        # Initializing these two variables
        self.file_distance = 0.0
        self.file_lines = self.cnt = 0

    # Getting the max value from the name_dist_KV dictionary
    def getmax_name_dist_KV_value(self):
        return max(self.name_dist_KV.values())

    # Getting the name of the person with the max distance
    def getmax_name_dist_KV_key(self):
        return max(self.name_dist_KV, key=self.name_dist_KV.get)

    # Getting the min value from the name_dist_KV dictionary
    def getmin_name_dist_KV_value(self):
        return min(self.name_dist_KV.values())

    # Getting the name of the person with the min distance
    def getmin_name_dist_KV_key(self):
        return min(self.name_dist_KV, key=self.name_dist_KV.get)

    # Returns the number of names in the dictionary
    def getlen_name_dist_KV(self):
        return len(self.name_dist_KV)


    def get_name_dist_KV_multiplecnt(self):
        self.cnt = 0

        # Using a for loop to go through all the values in the count list and an if statement to
        # test whether the value is greater than 1. If the value is greater than one, this
        # indicates that the person has multiple records, so he/she is added to the cnt
        # variable. The cnt variable indicates the number of participants with multiple records.
        for self.k, self.v in self.name_count_KV.items():
            if self.v > 1:
                self.cnt += 1
        return self.cnt

    # Returning a string with all the names
    def get_name_dist_KV_keys(self):
        return self.name_dist_KV.keys()

    # Looking up the name and returning the distance
    def get_name_dist_KV_value(self, key):
        return self.name_dist_KV[key]


    # Looking up the name and returning the count
    def get_name_count_KV_value(self, key):
        return self.name_count_KV[key]

    # Processing all the records in the file and extracting the names and the distances. Counting the occurrance
    # if the name appears more than once
    def processFile(self, fName):
        self.__fName = fName
        try:
            self.fh = open(self.__fName, 'r')
            self.file_lines = len(self.fh.readlines())
            self.fh.seek(0)
            for self.line in self.fh:
                self.cnt = 0
                if not "distance" in self.line:
                    #data = fh.readline()
                    #file_distance = sum( \
                        #float([item.strip('\n').split(',')[1] for item in data]))
                    self.temp = self.line.split(',')
                    self.name = (self.temp[0].strip())
                    self.dist = float(self.temp[1])
                    # if found, update data, not found, append

                    if self.name in self.name_dist_KV:
                        # We have to find the person
                        # position = name_list.index(name)
                        # Extract the original data
                        self.orig_cnt = int(self.name_count_KV[self.name])
                        self.orig_dist = float(self.name_dist_KV[self.name])

                        self.orig_cnt += 1
                        self.orig_dist += self.dist

                        # Need to delete the person from all three list in order to
                        # update the record
                        del self.name_dist_KV[self.name]
                        del self.name_count_KV[self.name]

                        # Adding the new updated record to all three lists
                        self.name_dist_KV[self.name] = self.orig_dist
                        self.name_count_KV[self.name] = self.orig_cnt
                    # If name not found, add the name to the three lists: name, distance, and number of times the name
                    # appeared (count)
                    else:
                        self.cnt += 1

                        self.name_dist_KV[self.name] = self.dist
                        self.name_count_KV[self.name] = self.cnt

                    self.file_distance += self.dist
            self.fh.close()
        except FileNotFoundError:
            print('File <', self.line, '> not found.', end='')
        return self.file_distance, self.file_lines



def main():

    # Main Program
    try:
        # Assigning the specified filename to the masterFile variable. Then opening the file in read mode
        masterFile = "f2016_cs8_fp.data.txt"
        masterListFO = open(masterFile, 'r')

        # Setting up counters
        total_files = total_lines = 0
        total_distance = 0.0

        # Create an object from the DataFile class
        my_file = DataFile()

        # Using a for loop to process the files given in the master file
        for fileName in masterListFO:
            total_files += 1
            fileName = fileName.strip()
            # Using the processFile function created above to process the files specified in the master file
            distance, lines = my_file.processFile(fileName)

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
        print("max distance run".ljust(30), ":", format(my_file.getmax_name_dist_KV_value(), '10.5f'))
        # position = distance_list.index(max(distance_list))
        print("  by participant".ljust(30), ":", format(my_file.getmax_name_dist_KV_key(), '10'))
        print('\n', end='')


        # Finding the position of the minimum distance and then finding the corresponding name
        print("min distance run".ljust(30), ":", format(my_file.getmin_name_dist_KV_value(), '10.5f'))
        # position = distance_list.index(min(distance_list))
        print("  by participant".ljust(30), ":", format(my_file.getmin_name_dist_KV_key(), '10'))
        print('\n', end='')


        # Creating and formatting the output for the total number of participants acculmulated from all three
        # files.
        print("Total number of participants".ljust(30), ":", format(my_file.getlen_name_dist_KV(), '10'))

        print("Number of participants")
        print("  with multiple records".ljust(30), ":", format(my_file.get_name_dist_KV_multiplecnt(), '10'))

        masterListFO.close()

        try:
            cnt = 0
            # Creating the outfile that contains the name, total distance, and count for each record from all three
            # files.
            outfile = 'f2016_cs8_jef107_fp.data.output.csv'
            outfileFO = open(outfile, 'w')

            key_list = my_file.get_name_dist_KV_keys()

            #print("key_list >>> ", key_list, "<<<<")

            for key in sorted(key_list):
            #for key in key_list:
                # line = str(k) + ',' + str(name_count_KV[k]) + ',' + str(v)
                line = str(key) + ',' + str(my_file.get_name_count_KV_value(key)) + ',' + str(my_file.get_name_dist_KV_value(key))
                #print("count >>>> ", str(my_file.get_name_count_KV_value(key)), "<<<<<")
                #print("dist >>>>", str(my_file.get_name_dist_KV_value(key)), "<<<<<")


                outfileFO.write(line)
                outfileFO.write('\n')
                cnt += 1
            outfileFO.close()
        except:
            print('Outfile <', outfileFO, '> Error.', end='')


    except FileNotFoundError:

        print('Master File <', masterFile, '> not found.', end='')
main()






