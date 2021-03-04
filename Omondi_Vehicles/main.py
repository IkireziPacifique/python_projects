#Author Pacifique Linda IKIREZI
#Question 1 Vehicle Renting Business

# Calling the parent class
from vehicle import Vehicle

# Calling child classes
from car import Car
from moto import Moto

# Creating an empty list
all_vehicles = []

# Adding in attributes
all_vehicles.append(Vehicle("Suzuki", "SWIFT", 2019, "2020", 250, "RAE095A", 5))
all_vehicles.append(Vehicle("Pruis", "Prime", "2017", "2018", 1000, "RAE194A", 10))
all_vehicles.append(Vehicle("RAV4", "Hybrid", "2019", "2020", 100 , "RAE064A", 2))
all_vehicles.append(Vehicle("Jeep_Wrangler", "Sahara", "2016", "2017", 1000, "RAE994A", 5))
all_vehicles.append(Vehicle("G_Wagon", "G 63 AMG", "2015", "2017",2000, "RAE124A", 5))

loop = True
while (loop):
    print("\nHELLO OMONDI,PLEASE CHOOSE THE VEHICLE YOU WANT: "
          "\n1. CAR"
          "\n2. MOTOR")
    print("----------------------------------------------------------------------")
    choose = int(input("Please enter the number of the vehicle you want to see: "))
    # operations for car
    print("\nPLEASE CHOOSE THE OPERATION YOU WANT TO PERFORM: ")
    if choose == 1:
        print("1. Insert New Car")
        print("2. Delete Car")
        print("3. Rent Car")
        print("4. See all available cars")
        print("5. Check the  carbon footprint of a car")
        print("6. Go ahead or Stop")
        # User input the operation they want to make
        operation = int(input("\nPlease enter the number of the operation you want to perform: "))
        if operation:
            if operation == 1:
                new = Car()
                new.add_vehicle(all_vehicles)
            elif operation == 2:
                delete = Car()
                delete.delete_vehicle(all_vehicles)
            elif operation == 3:
                rent = Car()
                rent.rent_vehicle(all_vehicles)
            elif operation == 4:
                view = Car()
                view.view_vehicle(all_vehicles)
            elif operation == 5:
                check = Car()
                check.carbon_footprint(all_vehicles)
            elif operation == 6:
                nooperation = Car()
                nooperation.no_operation()
            else:
                print('UNKNOWN INPUT, PLEASE TRY AGAIN \n')
        else:
            print('THE INPUT IS INVALID, PLEASE ENTER NUMBER')

    #operations for motor
    elif choose == 2:
        print("1. Insert New Motor")
        print("2. Delete Motor")
        print("3. Rent Motor")
        print("4. See all available Motor")
        print("5. Check the  carbon footprint of a motor")
        print("6. Go ahead or Stop")
        # User input the operation they want to make
        operation = int(input("\nPlease enter the number of the operation you want to perform: "))
        if operation:
            if operation == 1:
                new = Moto()
                new.add_vehicle(all_vehicles)
            elif operation == 2:
                delete = Moto()
                delete.delete_vehicle(all_vehicles)
            elif operation == 3:
                rent = Moto()
                rent.rent_vehicle(all_vehicles)
            elif operation == 4:
                view = Moto()
                view.view_vehicle(all_vehicles)
            elif operation == 5:
                check = Car()
                check.carbon_footprint(all_vehicles)
            elif operation == 6:
                nooperation = Car()
                nooperation.no_operation()
            else:
                print('UNKNOWN INPUT, PLEASE TRY AGAIN \n')
        else:
            print('THE INPUT IS INVALID, PLEASE ENTER NUMBER')
