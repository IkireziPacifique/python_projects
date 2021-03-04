# Creating a class
class Vehicle:
    #creating a constructor
    def __init__(self, brand="", model="", release_year=0, aquired_year="", income=0, plate_number="",rental_number=0):
        self.brand = brand
        self.model = model
        self.release_year = release_year
        self.aquired_year = aquired_year
        self.income = income
        self.plate_number = plate_number
        self.rental_number = rental_number
    #Add method
    def add_vehicle(self, all_vehicles):
        print("\nTIME TO INSERT NEW VEHICLE YEEAYY......\n")
        self.brand = input("Please enter the vehicle brand : ")
        self.model = input("Please enter the vehicle model : ")
        self.release_year = input("Please enter the release year : ")
        self.aquired_year = input("Please enter the acquired year : ")
        self.income = int(input("Please enter the vehicle income : "))
        self.plate_number = input("Please enter the vehicle plate number : ")
        self.rental_number = int(input("Please enter the vehicle rental amount : "))
        all_vehicles.append(self)
        print('\n VEHICLE SUCCESSFUL INSERTED, AVAILABLE CARS ARE :', len(all_vehicles))

    # Delete method
    def delete_vehicle(self, all_vehicles):
        print("\n TIME TO DELETE VEHICLE......")
        plate_no = input("Please enter the plate number of the vehicle you want to delete : ")
        if plate_no:
            for x in all_vehicles:
                if x.plate_number == plate_no:
                    all_vehicles.remove(x)
                    print('The vehicle has been sucessful deleted : ', x.brand)
        else:
            print('\nTHE INPUT IS INVALID, PLEASE ENTER NUMBER\n')

    # Rent method
    def rent_vehicle(self, all_vehicles):
        print("\n YEEEAAY WE ARE RENTING A VEHICLE....")
        to_rent = input("Please input the Plate Number of a vehicle you want to rent: ")
        if to_rent:
            for x in all_vehicles:
                if to_rent == x.plate_number:
                    x.rental_number = x.rental_number + 1
                    money_made = int(input("Enter the money made: "))
                    x.income = x.income + money_made
                    print("you have successfully rented " , x.brand, )
        else:
            print('\nTHE INPUT IS INVALID, PLEASE ENTER NUMBER\n')

    # view method
    def view_vehicle(self, all_vehicles):
        print("\n ALL AVAILABLE VEHICLES...... :", len(all_vehicles), "\n")
        number = 0
        for i in all_vehicles:
            number = number + 1
            print('\nCAR ', number , '\n', '---------------')
            print('VEHICLE BRAND : ', i.brand)
            print('VEHICLE MODEL : ', i.model)
            print('VEHICLE RELEASE YEAR : ', i.release_year)
            print('VEHICLE AQUIRED YEAR : ', i.aquired_year)
            print('VEHICLE INCOME YEAR : ', i.income)
            print('VEHICLE PLATE NUMBER: ', i.plate_number)
            print('VEHICLE RENTAL NUMBER : ', i.rental_number)

    # Exit function
    def no_operation(self):
        question = input("Do you want to make an Operation Y/N: ")
        if question.upper() == 'N':
            exit()
        elif question.upper() == 'Y':
            print("Let's Continue")