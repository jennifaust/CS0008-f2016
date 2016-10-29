# name          : Jenni Faust
# email         : jef107@pitt.edu
# date          : 10/29/16
# class         : CS0008-f2016
# instructor    : Max Novelli (man8@pitt.edu)
#
# Python, Assignment 2


# Creating the processFile(fh) Function which handles the file object to be read. It returns two values:
# total number of lines file read and the total distance of each record.
def fh(infile):
    TempD = TempL = 0
    try:
        FO = open (infile, 'r')
        # Giving instructions after file has been opened. First want to take off the extra space added at the end of the field.
        for line in FO:
            line = line.rstrip ("\n")
            # Extracting the distance from the two fields
            Temp = line.split(",")
            Dist = float(Temp[1])
            # TempL adds the lines and TempD adds the distances obtained from the files.
            TempL += 1
            TempD += Dist

        FO.close()
    except FileNotFoundError:
        TempL = -1
        print("File [", infile, "] not found. Please retry.")
    # Returning the accumulated values of lines and distance.
    return TempL, TempD

# Creating the printKV Function. This function prints the key, value and optional key length in a consistent format.
def printKV(key, value, klen = 0):
    colon = ":"
    # For string, use 20 spaces.
    if isinstance(value, str):
        FS = '20'
        colon = ""
    # For float, use 10 spaces and 3 decimal places.
    elif isinstance(value, float):
        FS = '10.3f'
    # For integer, use 10 spaces.
    else:
        FS = '10'
    print(key.ljust(klen), colon, format(value, FS))
    return

# This is the main program. It asks for the user to enter the file name. The program then uses the two functions
# created above to calculate the partial distance run, partial number of lines, total distance run and total number
# of lines and prints these values in a consistent format.

# This statement gives instructions to the user.
print("Enter the file name to be read or type quit, q or press the enter key to end.")

# This statement initiates the while loop
file = 'start'

# TTempL = Total number of lines accrued from all the files entered. TTempD = Total amount of distance accrued from
# all the files entered into the program. These variables are defined below.
TotalLines = TotalDist= 0
txtlen = 30

# The while loop which continues as long as the enter key, quit, or q is not entered by the user.
while file != "quit" and file !="q" and file !='':

    # Asks for user input.
    file = input("\nFile to be read: ")
    file = file.strip()
    if (file == "quit") or (file == "q") or (file ==''):
        break
    FileLines, FileDist = fh(file)
    # If line is less than zero, this means file was not found.
    if FileLines > 0:
        printKV("Partial Total # of lines", FileLines, txtlen)
        printKV("Partial distance run", FileDist, txtlen)

        TotalLines += FileLines
        TotalDist += FileDist

# Make sure we processed some files
if TotalLines > 0:
        printKV("\nTotals", '')
        printKV("Total # of lines", TotalLines, txtlen)
        printKV("Total distance run", TotalDist, txtlen)
else:
        print("Program terminated without processing any files.")





