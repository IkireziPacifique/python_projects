# Calling the parent class
from vehicle import Vehicle

#Creating the child class
class Moto(Vehicle):
    def __init__(self, brand="", model="", release_year=0, aquired_year="", income=0, plate_number="",
                 rental_number=0, helmet=0):
        super().__init__(brand="", model="", release_year=0, aquired_year="", income=0, plate_number="",
                         rental_number=0)
        self.hemet = helmet

    def add_vehicle(self, all_vehicles):
        super().add_vehicle(all_vehicles)
        self.hemet = int(input("Please enter the helmet(s) : "))
        all_vehicles.append(self)
        print('\n CAR SUCCESSFUL INSERTED, AVAILABLE CARS ARE :', len(all_vehicles))

    # method to calculate the carbon footprint
    def carbon_footprint(self, all_vehicles):
        motor_to_check = input("Please enter the plate number of a motor you want: ")
        if motor_to_check:
            for x in all_vehicles:
                if motor_to_check == x.plate_number:
                    years_old = 2020 - x.release_year
                    miles = int(input("Miles it has covered: "))
                    gallon = int(input("gallons per mile: "))
                    grams = int(input("grams: "))
                    calculator = years_old * 10000 * (miles/12) * 2 * (gallon/miles) * 9 * (grams/gallon)
                    print("Carbon Footprint of", x.brand, x.model, "with", x.plate_number,
                          "Plate number is:", calculator)