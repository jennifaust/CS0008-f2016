#
# name          : Jenni Faust
# email         : jef107@pitt.edu
# date          : 9/30/16
# class         : CS0008-f2016
# instructor    : Max Novelli (man8@pitt.edu)
#
# Description:
# Gas Milage
# Python, Assignment 1
# Notes: N/A

# Asking user for preferred system
system = int(input("Would you like to use USC or the Metric System? Please enter 1 for \n"
                   "USC system or 2 for Metric system."))

# If the user uses USC system
if system == 1:

# Asking the user for the distance and gasoline using USC units
    distance = int(input("How many miles did you drive?"))
    gasoline = int(input("How many gallons of gasoline did you use?"))

# Converting the distance and gasoline to Metric system
    distanceKilo = distance * 1.60934
    gasolineLiters = gasoline * 3.78541

# Gas consumption for USC system
    fuelconsumption = distance/gasoline

# Gas consumption for Metric system - 1/100 Km
    fuelconsumptionMetric = (gasolineLiters/distanceKilo) * 100

# Formatting table for USC users
    print("                                 {0}               {1}".format("USC", "Metric"))
    print("Distance____________:", format(distance, '14.3f'), "miles", \
          format(distanceKilo, '14.3f'), "Km" )
    print("Gas_________________:", format(gasoline, '14.3f'), "gallons", \
          format(gasolineLiters, '12.3f'), "Liters")
    print("Consumption_________:", format(fuelconsumption, '14.3f'), "mpg", \
          format(fuelconsumptionMetric, '16.3f'), "1/100Km")

# Printing Gas Consumption Rating for USC Users
    if fuelconsumptionMetric > 20:
        print('''
Gas Consumption Rating : Extremely Poor
            ''')
    elif 15 < fuelconsumptionMetric <= 20:
        print('''
Gas Consumption Rating : Poor
            ''')
    elif 10 < fuelconsumptionMetric <=15:
        print('''
Gas Consumption Rating : Average
            ''')
    elif 8 < fuelconsumptionMetric <= 10:
        print('''
Gas Consumption Rating : Good
            ''')
    elif fuelconsumptionMetric <= 8:
        print('''
Gas Consumption Rating : Excellent
            ''')
    else:
        print("Error")

# If user uses the Metric system
elif system == 2:

# Asking the user for the distance and gasoline using metric units
    distanceM = int(input("How many kilometers did you drive?"))
    gasolineM = int(input("How many liters of gasoline did you use?"))

#Converting the distance and gasoline to USC system
    distanceUSC = distanceM/1.60934
    gasolineUSC = gasolineM/3.78541

# Gas consumption for USC system
    fuelconsumptionUSC = distanceUSC/gasolineUSC

# Gas consumption for Metric system - 1/100km
    fuelconsumptionM = (gasolineM/distanceM)*100

# Formatting table for Metric users
    print("                                 {0}               {1}".format("USC", "Metric"))
    print("Distance____________:", format(distanceUSC, '14.3f'), "miles", \
          format(distanceM, '14.3f'), "Km" )
    print("Gas_________________:", format(gasolineUSC, '14.3f'), "gallons", \
          format(gasolineM, '12.3f'), "Liters")
    print("Consumption_________:", format(fuelconsumptionUSC, '14.3f'), "mpg", \
          format(fuelconsumptionM, '16.3f'), "1/100Km")

# Printing Gas Consumption Rating
    if fuelconsumptionM > 20:
        print('''
Gas Consumption Rating : Extremely Poor
            ''')
    elif 15 < fuelconsumptionM <= 20:
        print('''
Gas Consumption Rating : Poor
            ''')
    elif 10 < fuelconsumptionM <=15:
        print('''
Gas Consumption Rating : Average
            ''')
    elif 8 < fuelconsumptionM <= 10:
        print('''
Gas Consumption Rating : Good
            ''')
    elif fuelconsumptionM <= 8:
        print('''
Gas Consumption Rating : Excellent
            ''')
    else:
        print("Error")
else:
    print("Please enter either 1 or 2 for USC or Metric system respectively.")